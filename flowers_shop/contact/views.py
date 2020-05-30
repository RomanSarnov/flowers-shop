from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Feedback
from .forms import FeedbackForm, NewsletterForm
from django.views import View
from django.conf import settings
from .tasks import send_email_task, send_newsletter
from django.db import IntegrityError


class CreateFeedbackView(View):
    def get(self, request):
        form = FeedbackForm()
        template = "contact/feedback.html"
        context ={'form': form}
        return render(request, template, context)

    def post(self, request):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            copy = form.cleaned_data['copy']
            subject = form.cleaned_data['subject']
            text = form.cleaned_data['text']
            email = form.cleaned_data['email']
            sender = settings.EMAIL_HOST_USER
            if copy:
                send_email_task.delay(subject, text, sender, [email])
            return redirect('shop')
        template = "contact/feedback.html"
        context = {'form': form}
        return render(request, template, context)


class AddNewsletterView(View):
    def post(self, request):
        form = NewsletterForm({'email': request.POST.get('email')})
        if form.is_valid():
            form.save()
            subject = 'Вы подписались на рассылку'
            text = 'Спасибо за подписку!'
            sender = settings.EMAIL_HOST_USER
            recipient = form.cleaned_data['email']
            send_email_task.delay(subject, text, sender, [recipient])
        return redirect(request.POST.get('url_from'))
