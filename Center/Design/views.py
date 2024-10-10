# myapp/views.py

# Design/views.py

from django.shortcuts import render
from .models import Feature
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.shortcuts import render

# Design/views.py

def home(request):
    return render(request, 'index.html')  # Убедитесь, что это правильно

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')  # Представление для политики конфиденциальности

def terms_of_service(request):
    return render(request, 'terms_of_service.html')  # Представление для условий использования

def faq(request):
    return render(request, 'faq.html')  # Представление для страницы FAQ

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.conf import settings

def contact_submit(request):
    if request.method == 'POST':
        # Извлечение данных из формы
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Отправка письма
        subject = f'Сообщение от {name}'
        message_body = f'От: {name}\nEmail: {email}\nСообщение:\n{message}'
        recipient_list = ['recipient@example.com']  # Укажите получателя

        send_mail(subject, message_body, email, recipient_list)
        return HttpResponse('Сообщение отправлено!')
    
    return render(request, 'contact.html')  # Замените на ваш шаблон