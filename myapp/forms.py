# -*- coding:utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _

from models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person