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


class Template(models.Model):
    template_id = models.AutoField(primary_key=True, verbose_name="ID Шаблона")
    template_name = models.IntegerField(verbose_name="Номер шаблона")
    note = models.TextField(max_length=1000, blank=True, verbose_name="Примечание")

    def __str__(self):
        return "%s" % self.template_name

    class Meta:
        verbose_name = "Шаблон"
        verbose_name_plural = "Каталог шаблонов"


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

    # stage_choise = (('new', 'Новый'),
    #                 ('pay', 'Оплата'),
    #                 ('in_work', 'Верстка'),
    #                 ('perfomed', 'Выполнено'))
    # template_choise = (('1527', '1527'),
    #                    ('1530', '1530'),
    #                    ('1613', '1613'),
    #                    ('2032', '2032'),
    #                    ('2104', '2104'),
    #                    ('2105', '2105'),
    #                    ('2110', '2110'),
    #                    ('2202', '2202'),
    #                    ('4010', '4010'),
    #                    ('4018', '4018'),
    #                    ('4021', '4021'),
    #                    ('4030', '4030'),
    #                    ('5023', '5023'),
    #                    ('6021', '6021'),
    #                    ('1322', '1322'),
    #                    ('1602', '1602'))
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
    # template = models.CharField(max_length=4,
    #                             choices=template_choise,
    #                             default='1322',
    #                             verbose_name="Номер шаблона")
    template_name = models.ForeignKey(Template, on_delete=models.PROTECT,
                                      verbose_name="Номер шаблона", null=True,
                                      blank=True)
    payment_id = models.CharField(max_length=10, default=generate_pay_id,
                                  verbose_name="id оплаты", unique=True)
    send_link_for_pay = models.BooleanField(default=False, verbose_name="Письмо на оплату")
    paid = models.BooleanField(default=False, verbose_name="Оплачено")
    created = models.BooleanField(default=False, verbose_name="Сверстанно")
    completed = models.BooleanField(default=False, verbose_name="Изделие отправлено")
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
    # stage = models.CharField(max_length=10, choices=stage_choise,
    #                          verbose_name="Статус", default=1)
    product_link = models.CharField(max_length=100,
                                    verbose_name="Ссылка на изделие",
                                    default='link', blank=True)
    note = models.TextField(max_length=150, null=True, blank=True,
                            verbose_name="Примечание")

    class Meta:
        verbose_name_plural = "Изделия"
        verbose_name = "Изделие"
        # ordering = ["-template"]


class FotoOrder(models.Model):
    def upload_path(self, filename):
        return "order_img/" + filename

    status_choices = (('check', 'Проверка'),
                      ('verified', 'Проверенно'))
    client_email = models.EmailField(verbose_name="Email")
    town = models.CharField(max_length=30, verbose_name="Город")
    ed_institution = models.CharField(max_length=50,
                                      verbose_name="Номер школы/детского сада")
    the_class = models.CharField(max_length=20, verbose_name="класс/группа")
    foto_from_client = models.ImageField(upload_to=upload_path,
                                         verbose_name="Фото")
    status = models.CharField(max_length=15, choices=status_choices,
                              verbose_name="Статус", default='check')
    photo_available = models.BooleanField(default=False,
                                          verbose_name='Наличие фото')

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class Articles(models.Model):
    description = models.TextField(null=True, verbose_name="Инструкция")

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
