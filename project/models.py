from django.db import models


class Base(models.Model):
    created = models.DateTimeField(auto_created=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
