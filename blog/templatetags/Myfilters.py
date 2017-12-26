

from django import template
from django.utils.safestring import mark_safe

register = template.Library()   #register的名字是固定的,不可改变


@register.filter
def Age_of_orchard(t):

    import datetime

    user_create_time=datetime.datetime(year=t.year,month=t.month,day=t.day,hour=t.hour,minute=t.minute,second=t.second)
    ret=datetime.datetime.now()-user_create_time

    # print(ret)
    # print(type(ret))

    return mark_safe(ret)






