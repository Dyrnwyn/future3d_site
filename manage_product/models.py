from django.db import models
import uuid


class ProductId(models.Model):
	template_choise = (('1527', '1527'),
                       ('2032', '2032'),
                       ('2104', '2104'),
                       ('4021', '4021'),
                       ('4030', '4030'))
	product_id = models.UUIDField(unique=True, primary_key=True, editable=False, 
		default=uuid.uuid4, verbose_name="Уникальный ID изделия")
	img = models.ImageField(upload_to='img/', verbose_name="Фото")
	template = models.CharField(max_length = 4, choices=template_choise, verbose_name="Номер шаблона")
	payment_id = models.CharField(max_length = 10, verbose_name="id оплаты")
	paid = models.BooleanField(default=False, verbose_name="Оплачено")

	class Meta:
		verbose_name_plural = "Изделия"
		verbose_name = "Изделие"
		ordering = ["-template"]