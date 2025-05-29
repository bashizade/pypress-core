from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    mobile = models.CharField(max_length=11, blank=True, null=True, unique=True)
    national_code = models.CharField(max_length=10, blank=True, null=True, unique=True)
    birth_date = models.DateField(blank=True, null=True)
    father_name = models.CharField(max_length=100, blank=True, null=True)
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        
    def __str__(self):
        return self.username

class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)
    permissions = models.ManyToManyField(Permission, blank=True)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name = _('role')
        verbose_name_plural = _('roles')
        
    def __str__(self):
        return self.name 