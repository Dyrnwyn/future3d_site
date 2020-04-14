from django.db import models
import uuid
from datetime import date


def default_date():
    return date.today()


class Email(models.Model):
    email = models.EmailField(default='email@email.ru',
                              verbose_name="e-mail")

    def __str__(self):
        return "%s" % self.email

    class Meta:
        verbose_name = "Электронные почты"
        verbose_name_plural = "электронная почта"


class ProductId(models.Model):

    def upload_path(self, filename):
        return 'img/' + str(self.product_id) + '_' + filename

    stage_choise = (('new', 'Новый'),
                    ('pay', 'Оплата'),
                    ('in_work', 'Верстка'),
                    ('perfomed', 'Выполнено'))
    template_choise = (('1527', '1527'),
                       ('2032', '2032'),
                       ('2104', '2104'),
                       ('4021', '4021'),
                       ('4030', '4030'))
    product_id = models.UUIDField(unique=True,
                                  primary_key=True,
                                  editable=False,
                                  default=uuid.uuid4,
                                  verbose_name="Уникальный ID изделия")
    img = models.ImageField(upload_to=upload_path, verbose_name="Фото")
    template = models.CharField(max_length=4,
                                choices=template_choise,
                                verbose_name="Номер шаблона")
    payment_id = models.CharField(max_length=10, verbose_name="id оплаты")
    paid = models.BooleanField(default=False, verbose_name="Оплачено")
    date_opening = models.DateField(auto_now_add=True,
                                    null=True,
                                    verbose_name="Дата принятия заказа")
    date_payment = models.DateField(null=True, blank=True,
                                    verbose_name="Дата оплаты")
    date_close = models.DateField(null=True, blank=True,
                                  verbose_name="Дата отправки заказа")
    email = models.ForeignKey(Email, null=True, on_delete=models.PROTECT,
                              verbose_name="e-mail клиента")
    stage = models.CharField(max_length=10, choices=stage_choise,
                             verbose_name="Статус", default=1)

    class Meta:
        verbose_name_plural = "Изделия"
        verbose_name = "Изделие"
        ordering = ["-template"]
