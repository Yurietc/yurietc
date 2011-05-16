# -*- coding:utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404

from forms import PersonForm
from models import Person

def startpage(request):


@login_required
def edit_person(request):
    form = PersonForm()
