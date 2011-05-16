from django.conf.urls.defaults import *
from django.contrib import admin
from django.shortcuts import get_object_or_404
from django.views.generic.simple import direct_to_template
from django.contrib.auth.views import logout_then_login, login

from myapp.views import *
from myapp.models import Person

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    url(r'^/?$', direct_to_template,{
                                     'template': 'myapp/startpage.html',
                                     'extra_context':{
                                                      'Person': get_object_or_404(Person)
                                                     }
                                    }, name='startpage'),
    url(r'^login', login, name='login'),
    url(r'^edit-person/?$', 'myapp.views.edit_person', name='edit_person'),
)
