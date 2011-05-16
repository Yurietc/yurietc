# -*- coding:utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

SEX_TYPES = (
    (1, _(u'Male')),
    (2, _(u'Female')),
)

class Person(models.Model):
    first_name = models.CharField(_('First name'), max_length=50)
    last_name =  models.CharField(_('Last name'), max_length=50)
    e_mail = models.EmailField(_('E-mail'), max_length=50)
    phone = models.CharField(_('Phone'), max_length=20)
    sex = models.IntegerField(_(u'Sex'), choices=SEX_TYPES)
    about = models.TextField(_(u'Additional information'), blank=True)

    class Meta:
        verbose_name = _('Person')
        verbose_name_plural = _('Persons')
    
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)