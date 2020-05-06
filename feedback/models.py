from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    email = models.EmailField(verbose_name="e-mail")
    subject = models.CharField(max_length=50, verbose_name="Тема")
    message = models.TextField(max_length=1000, verbose_name="Сообщение")

    class Meta:
        verbose_name_plural = "Сообщения пользователей"
        verbose_name = "Сообщение"
