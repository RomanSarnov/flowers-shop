from django import template
from contact.forms import NewsletterForm

register = template.Library()

@register.inclusion_tag('contact/tags/form.html')
def newsletter_form(request):
    return {'form': NewsletterForm(), 'request': request}

