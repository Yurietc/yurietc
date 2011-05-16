# -*- coding:utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.views.generic.simple import direct_to_template
from django.http import HttpResponseRedirect

from forms import PersonForm
from models import Person


@login_required
def edit_person(request):
    person = get_object_or_404(Person)
    form = PersonForm(instance=person)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('startpage'))
    return direct_to_template(request, 'myapp/edit_info.html',
                             {
                                'form': form
                             })