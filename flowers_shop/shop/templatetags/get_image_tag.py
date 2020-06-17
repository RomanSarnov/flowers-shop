from django import template

register = template.Library()

@register.simple_tag()
def get_image(queryset):
    return queryset[0].image.url