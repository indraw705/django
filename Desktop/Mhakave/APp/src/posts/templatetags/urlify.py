from urllib import quote_plus
from django import template

register = template.Library()


@register.filter
def urlify(value):
	return qoute_plus(value)