from django import template

register = template.Library()

@register.filter(name='censor')
def censor(value):
    swear = ['слово 1', 'слово 2', 'слово 3']
    for word in swear:
        clean_text = value.replace(str(word), '***')
        value = clean_text
    return clean_text
