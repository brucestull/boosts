from django.db import models
from django.urls import reverse

from config.settings.common import AUTH_USER_MODEL


class Statement(models.Model):
    body = models.CharField(max_length=500)
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username + " : " + str(self.id) + " - " + self.body[:24]

    def get_absolute_url(self):
        return reverse("boosts:statement_detail", kwargs={"pk": self.pk})
