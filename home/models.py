# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Profesor(models.Model):

    #__Profesor_FIELDS__
    nombre = models.CharField(max_length=255, null=True, blank=True)
    nac = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Profesor_FIELDS__END

    class Meta:
        verbose_name        = _("Profesor")
        verbose_name_plural = _("Profesor")


class Alumnos(models.Model):

    #__Alumnos_FIELDS__
    nombre = models.CharField(max_length=255, null=True, blank=True)
    f_nac = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Alumnos_FIELDS__END

    class Meta:
        verbose_name        = _("Alumnos")
        verbose_name_plural = _("Alumnos")



#__MODELS__END
