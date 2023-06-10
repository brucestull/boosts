from django.db import models
from django.urls import reverse

from config.settings.common import AUTH_USER_MODEL


class Inspirational(models.Model):
    body = models.TextField(
        help_text="Required.",
        verbose_name="Inspirational Body Text",
    )
    author = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="inspirationals",
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.author.username + " : " + str(self.id) + " - " + self.body[:24]
