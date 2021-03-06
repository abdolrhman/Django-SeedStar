# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    """docstring for User."""
    first_name = models.CharField(max_length =128)
    last_name = models.CharField(max_length =128)
    email = models.EmailField(max_length =246, unique=True)
