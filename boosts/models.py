from django.db import models
from django.urls import reverse

from config.settings.common import AUTH_USER_MODEL


class Statement(models.Model):
    statement = models.CharField(max_length=500)
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.statement[:24]

    def get_absolute_url(self):
        return reverse("boosts:statement_detail", kwargs={"pk": self.pk})
