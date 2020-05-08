from django.db import models


class Menu(models.Model):
    section_number = models.IntegerField(default=1,
                                         verbose_name="Положение в меню")
    section_name = models.CharField(max_length=50, verbose_name="Раздел")
    section_url = models.CharField(max_length=100,
                                   verbose_name="Ссылка на раздел")

    class Meta:
        verbose_name = "Меню сайта"
        verbose_name_plural = "Меню"
