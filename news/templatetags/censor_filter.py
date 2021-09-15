from django import template

register = template.Library()

censor_list = ['слово1', 'слово2', 'слово3']
value_new = []


@register.filter(name='censor')
def censor(value):
    for word in censor_list:
        value = value.replace(word, '*****')
    return value
