from django import template 

register = template.Library()

@register.filter
def list_display(value):
    value = value.split(',')
    return value 

@register.filter
def is_valid_param(param):
    return param != "" and param != None and param != "None"

@register.filter
def times(number):
    return range(number)
@register.filter
def remain_times(number):
    number = 5-number 
    return range(number)
# register.filter('list_display', list_display)