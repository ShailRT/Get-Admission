from django import template 

register = template.Library()

@register.filter
def list_display(value):
    value = value.split(',')
    return value 

@register.filter
def is_valid_param(param):
    return param != "" and param != None

# register.filter('list_display', list_display)