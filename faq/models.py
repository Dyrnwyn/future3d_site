from django.db import models

class Faq(models.Model):
    question = models.CharField(max_length=200, verbose_name="Вопрос")
    answer = models.TextField(verbose_name="Ответ")

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "Часто задаваемые вопросы"
