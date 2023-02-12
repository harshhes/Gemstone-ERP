from django.db import models
from django.utils.translation import gettext_lazy as _


class Timestampedmodel(models.Model):
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Modified at"), auto_now=True)

    class Meta:
        abstract = True