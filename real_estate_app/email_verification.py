from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib import messages
import random
from .models import *


@csrf_exempt
def send_email(request):
    if request.method == 'POST':
        emailId = request.POST.get('email')  
        subject = "test email"
        message = str(random.randint(1000, 9999))
        sender_email = settings.EMAIL_HOST_USER

        try:
            send_mail(subject, message, sender_email, [emailId])
            
            login = LoginDetails(
            Email = emailId,
            Otp = message
            )
            login.save()
            
            # Set session variable
            request.session['emailId'] = emailId
            
            return JsonResponse({'status':'success'})
            
            
        except Exception as e:
            # Log the exception (optional)
            #return JsonResponse({'status': 'error', 'message': f'Error sending email: {str(e)}'})
            return JsonResponse({'error': 'Invalid request'}, status=400)
        
    else:
        #return render(request, 'email_login.html')
        return JsonResponse({"error": "Invalid request"}, status=400)

    
    
    

def otp_verification(request):
    if request.method == 'POST':
        otp_check = request.POST.get('otp')
        emailId = request.session.get('emailId')

        try:
            user = LoginDetails.objects.filter(email=emailId).order_by('-created_at').first()

            stored_otp = user.otp
            print(user)
        
        
            if stored_otp == otp_check:
                print("Otp verified")
                return redirect('index')
            else:
                print("Otp verification failed")
    
        except LoginDetails.DoesNotExist:
            print("User with this email does not exist")

    return redirect('email_login_otp')

def email_login(request):
    return render(request,"email_login.html")

def email_login_otp(request):
    return render(request,"email_login_otp.html")

