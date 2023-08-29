from django import template
import json

register = template.Library()

@register.simple_tag(takes_context=True)
def sec_to_hm(context, seconds, day=''):
    if seconds=='' or seconds is  None:
        return ''
    if type (seconds) == str:
        return seconds
    if seconds>=86400:
        day = 'day'
    minutes = int(seconds/60)
    hours = int(minutes/60)
    day = int(hours/24)
    if day == 'day':
        return("%d.%d2d D" %(day,hours % 24))
    return("%2d:%02d" % (hours,minutes % 60))
    