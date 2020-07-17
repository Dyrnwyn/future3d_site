from django.db import models


class AdMessage(models.Model):
    is_active = models.BooleanField(verbose_name="Включить")
    message = models.TextField(verbose_name="Сообщение")

    class Meta:
        verbose_name = "Всплывающие сообщения"
        verbose_name_plural = "Всплывающие сообщения"