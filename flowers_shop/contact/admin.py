from django.contrib import admin
from .models import Feedback, Newsletter

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('subject', 'text', 'email', 'copy')

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email',)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Newsletter, NewsletterAdmin)