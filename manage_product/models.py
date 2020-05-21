from django.db import models
import uuid
from datetime import date
import random


def default_date():
    return date.today()


class Worker(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    surname = models.CharField(max_length=50, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=50, verbose_name="Отчество")

    def __str__(self):
        return "%s" % self.surname + " " + self.name

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"


class Town(models.Model):
    town = models.CharField(max_length=50, verbose_name="Город")

    def __str__(self):
        return "%s" % self.town

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


class Email(models.Model):
    email = models.EmailField(default='email@email.ru',
                              verbose_name="e-mail")

    def __str__(self):
        return "%s" % self.email

    class Meta:
        verbose_name = "Электронные почты"
        verbose_name_plural = "электронная почта"


class ProductId(models.Model):
    # функция возвращающая путь и имя изображения с uuid
    def upload_path(self, filename):
        return 'img/' + str(self.product_id) + '_' + filename
    # генерация id для оплаты, последние две цифры года
    # явлаются первыми цифрами id

    def test_pay_id(self, pay_id):
        obj = ProductId.objects.all()
        for i in obj:
            if i.payment_id == pay_id:
                return True
        return False

    def generate_pay_id():
        two_last_number_of_year = str(date.today().year)[2:4]
        random_number = random.randrange(10000000, 99999999)
        pay_id = two_last_number_of_year + str(random_number)
        if ProductId.objects.filter(payment_id=pay_id).exists():
            random_number = random.randrange(10000000, 99999999)
            pay_id = two_last_number_of_year + str(random_number)
            return pay_id
        else:
            return pay_id

    stage_choise = (('new', 'Новый'),
                    ('pay', 'Оплата'),
                    ('in_work', 'Верстка'),
                    ('perfomed', 'Выполнено'))
    template_choise = (('1527', '1527'),
                       ('2032', '2032'),
                       ('2104', '2104'),
                       ('4021', '4021'),
                       ('4030', '4030'))
    organisations = (('school', 'Школа'),
                     ('playschool', 'Детский сад'))
    product_id = models.UUIDField(unique=True,
                                  primary_key=True,
                                  editable=False,
                                  default=uuid.uuid4,
                                  verbose_name="Уникальный ID изделия")
    img = models.ImageField(upload_to=upload_path, null=True,
                            verbose_name="Фото", blank=True)
    img_jpg = models.ImageField(upload_to=upload_path, blank=True,
                                verbose_name="Фото для скачивания",
                                null=True)
    template = models.CharField(max_length=4,
                                choices=template_choise,
                                verbose_name="Номер шаблона")
    payment_id = models.CharField(max_length=10, default=generate_pay_id,
                                  verbose_name="id оплаты", unique=True)
    paid = models.BooleanField(default=False, verbose_name="Оплачено")
    date_opening = models.DateField(auto_now_add=True, null=True,
                                    verbose_name="Дата принятия заказа")
    date_payment = models.DateField(null=True, blank=True,
                                    verbose_name="Дата оплаты")
    date_close = models.DateField(null=True, blank=True,
                                  verbose_name="Дата отправки заказа")
    email = models.ForeignKey(Email, on_delete=models.PROTECT,
                              verbose_name="e-mail клиента",
                              null=True)
    town = models.ForeignKey(Town, blank=True, on_delete=models.PROTECT,
                             verbose_name="Город", null=True)
    organisation = models.CharField(max_length=100, choices=organisations,
                                    verbose_name="Учебное заведение",
                                    default=1)
    organisation_name = models.CharField(max_length=50,
                                         verbose_name="Наименование",
                                         default="1",
                                         blank=True)
    worker = models.ForeignKey(Worker, null=True, on_delete=models.PROTECT,
                               verbose_name="Менеджер", blank=True)
    stage = models.CharField(max_length=10, choices=stage_choise,
                             verbose_name="Статус", default=1)
    product_link = models.CharField(max_length=100,
                                    verbose_name="Ссылка на изделие",
                                    default='link', blank=True)

    class Meta:
        verbose_name_plural = "Изделия"
        verbose_name = "Изделие"
        ordering = ["-template"]
