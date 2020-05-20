from django import template

register = template.Library()

@register.filter(name='make_range')
def make_range(value):
    try:
        if value:
            return range(round(value))
        else:
            return range(0)
    except:
        return range(0)
