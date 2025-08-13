from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .models import Appointment
from .forms import AppointmentForm
import requests
import json

class MakingAppointmentView(View):
    def get(self, request):
        form = AppointmentForm()
        return render(request, 'appointments/make_appointment.html', {'form': form})

    def post(self, request):
        form = AppointmentForm(request.POST)
        if form.is_valid():
            # Save appointment first
            appointment = form.save()
            
            # Prepare payment data for Zarinpal v4 API
            zarin_data = {
                'merchant_id': '7bdcfef3-105c-4281-afbe-d03c06cad0fc', 
                'amount': 100000, 
                'callback_url': 'http://localhost:8000/appointments/verify/',
                'description': f'پرداخت نوبت {appointment.name} {appointment.last_name}'
            }
            headers = {"accept": "application/json", "content-type": "application/json"}
            
            try:
                response = requests.post(
                    "https://sandbox.zarinpal.com/pg/v4/payment/request.json", 
                    json=zarin_data, 
                    headers=headers, 
                    timeout=10
                )
                
                if response.status_code == 200:
                    response_data = response.json()
                    print(f"Zarinpal response: {response_data}")
                    
                    # Check for success in v4 API format
                    if response_data.get('data', {}).get('code') == 100:
                        authority = response_data.get('data', {}).get('authority')
                        # Save authority to appointment
                        appointment.authority = authority
                        appointment.save()
                        
                        messages.success(
                            request,
                            f'نوبت شما با موفقیت ثبت شد! شماره تماس: {appointment.phone_number}'
                        )
                        return redirect(f"https://sandbox.zarinpal.com/pg/StartPay/{authority}")
                    else:
                        error_code = response_data.get('data', {}).get('code', 'نامشخص')
                        error_message = response_data.get('data', {}).get('message', 'خطای نامشخص')
                        messages.error(
                            request,
                            f'خطا در پرداخت! کد خطا: {error_code} - {error_message}'
                        )
                else:
                    messages.error(
                        request,
                        f'خطا در اتصال به درگاه پرداخت! کد وضعیت: {response.status_code}'
                    )
                    
            except requests.Timeout:
                messages.error(
                    request,
                    'درخواست پرداخت زمانبندی شده است. لطفاً دوباره تلاش کنید.'
                )
            except requests.ConnectionError:
                messages.error(
                    request,
                    'خطا در اتصال به درگاه پرداخت! لطفاً دوباره تلاش کنید.'
                )
            except Exception as e:
                messages.error(
                    request,
                    f'خطای غیرمنتظره: {str(e)}'
                )
            
            # If payment failed, show success page anyway (appointment is saved)
            return render(request, 'appointments/appointment_success.html', {'appointment': appointment})
        else:
            messages.error(
                request, 
                'خطا در ثبت نوبت! لطفاً اطلاعات وارد شده را بررسی کنید.'
            )
            return render(request, 'appointments/make_appointment.html', {'form': form})
class PayingAppointmentView(View):
    def get(self, request):
        authority = request.GET.get('Authority')
        status = request.GET.get('Status')
        
        if status != 'OK' or not authority:
            messages.error(
                request,
                'پرداخت ناموفق بود! لطفاً دوباره تلاش کنید.'
            )
            return redirect('appointments:book_appointment')
        
        # Find appointment by authority
        appointment = Appointment.objects.filter(authority=authority).first()
        if not appointment:
            messages.error(
                request,
                'نوبتی با این شماره پیدا نشد.'
            )
            return redirect('appointments:book_appointment')
        
        # Verify payment with Zarinpal
        verify_data = {
            'merchant_id': '7bdcfef3-105c-4281-afbe-d03c06cad0fc',
            'amount': 100000,
            'authority': authority
        }
        headers = {"accept": "application/json", "content-type": "application/json"}
        
        try:
            response = requests.post(
                "https://sandbox.zarinpal.com/pg/v4/payment/verify.json", 
                json=verify_data, 
                headers=headers
            )
            
            if response.status_code == 200:
                result = response.json()
                print(f"Verify response: {result}")
                
                # Check for success in v4 API format
                if result.get('data', {}).get('code') == 100:
                    appointment.is_paid = True
                    appointment.save()
                    messages.success(
                        request,
                        'پرداخت با موفقیت انجام شد!'
                    )
                else:
                    error_message = result.get('errors', {}).get('message', 'خطای نامشخص')
                    messages.error(request, f'تایید پرداخت ناموفق: {error_message}')
            else:
                messages.error(request, f'خطا در تایید پرداخت: {response.status_code}')
                
        except Exception as e:
            messages.error(request, f'خطا در پردازش تایید پرداخت: {str(e)}')
        
        return render(request, 'appointments/appointment_success.html', {'appointment': appointment})

    def post(self, request):
        pass