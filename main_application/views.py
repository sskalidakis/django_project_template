import pdb

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


from django.core.mail import send_mail
from .forms import FeedbackForm
from django.http import JsonResponse, HttpResponse
import os.path

import json
import urllib

from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages


def landing_page(request):
    print('Landing page')
    return render(request, 'main_application/landing_page.html')



def contact_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # This can be used to send an email to inform us about the newly submitted feedback.
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email_text = str(username) + ' submitted his/her feedback on the Platform:' + \
                         '\nSubject: "' + str(subject) + '"\nMessage: ' + str(message) + '"\n\n Contact e-mail: ' + str(
                email)

            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'

            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req = urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ''' End reCAPTCHA validation '''

            if result['success']:
                try:
                    form.save()
                    messages.success(request, 'New comment added with success!')
                    print('New comment added with success!')
                except:
                    messages.error(request, 'The feedback could not be stored!')
                    print('The evaluation could not be stored!')
                    return JsonResponse({'status': 'NOT_OK_FORM_NOT_SAVED'})
                try:
                    send_mail(str(username) + "has sent and email to the Platform", email_text, 'noreply@epu.ntua.gr',
                              ['myemail@hotmail.com'],
                              fail_silently=False)
                except:
                    messages.error(request,
                                   'The evaluation was stored but email to the project could not be sent! SMTP server credentials may be wrong!')
                    print(
                        'The evaluation was stored but email to the project could not be sent! SMTP server credentials may be wrong!')
                return JsonResponse({'status': 'OK'})
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
                print('Invalid reCAPTCHA. Please try again.')
                return JsonResponse({'status': 'NOT_OK_INVALID_CAPTCHA'})
