from django import template

register = template.Library()


@register.filter()
def censor(value):
    OBSCENE_WORDS = ['новость', 'редиска', 'болван', ]
    value = value.lower()  # создаём для поиска копию текста в нижнем регистре
    for word in OBSCENE_WORDS:
        if word.find(value):
            value = value.replace(word[1::], "*" * len(word))
            return f'{value}'

