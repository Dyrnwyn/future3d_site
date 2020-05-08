from django.contrib import admin
from .models import ProductId, Email, Town, Worker
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from datetime import date
from django.template.loader import render_to_string
from future3d_site.settings import BASE_DIR

class ProductIdAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'template', 'email',
                    'date_opening', 'payment_id', 'paid', 'date_payment',
                    'stage', 'product_link')
    list_display_links = ('product_id', 'template', 'email')
    actions = ('send_product_link', 'send_emailmessage_for_pay', 'create_product_link')
    host_name_for_email = 'http://localhost:8000/product/'

    def create_product_link(self, request, queryset):
        for rec in queryset:
            obj = ProductId.objects.get(product_id=rec.product_id)
            obj.product_link = 'http://localhost:8000/product/' + str(rec.product_id)
            obj.save()

    create_product_link.short_description = 'Создать ссылку на изделие'

    def send_product_link(self, request, queryset):
        for rec in queryset:
            context = {'product_link': self.host_name_for_email +
                       str(rec.product_id)}
            s = render_to_string('email/send_product_link.html',
                                 context=context)
            send_mail('Ссылка на изделие', '',
                      'stereo-ph@yandex.ru',
                      [rec.email, ],
                      html_message=s, )
            obj = ProductId.objects.get(product_id=rec.product_id)
            obj.stage = 'perfomed'
            obj.date_close = date.today()
            obj.save()

    send_product_link.short_description = 'Отправить письмо с ссылкой на изделие'

    def send_emailmessage_for_pay(self, request, queryset):
        for rec in queryset:
            context = {'payment_id' : rec.payment_id}
            s = render_to_string('email/send_pay_id.html', context=context)
            em = EmailMultiAlternatives(subject='Оплата заказа',
                                        body='',
                                        to=[rec.email])
            em.attach_alternative(s, 'text/html')
            # em.attach_file(r'E:/work/parallax_site/future3d_site/static/email/Инструкция по оплате заказа для родителей.pdf',
            #                'application/pdf')
            em.attach_file(BASE_DIR + '/static/email/Инструкция по оплате заказа для родителей.pdf',
                            'application/pdf')
            em.send()
            obj = ProductId.objects.get(product_id=rec.product_id)
            obj.stage = 'pay'
            obj.save()

    send_emailmessage_for_pay.short_description = 'Отправить письмо для оплаты'


    def set_paid_stage(self, request, queryset):
        for rec in queryset:
            obj = ProductId.objects.get(product_id=rec.product_id)
            obj.date_payment = date.today()
            obj.stage = 'in_work'
            obj.save()
    set_paid_stage.short_description = 'Изделие оплачено'


class EmailAdmin(admin.ModelAdmin):
    list_display = ('email',)


admin.site.register(ProductId, ProductIdAdmin)
admin.site.register(Email, EmailAdmin)
admin.site.register(Town)
admin.site.register(Worker)
# Register your models here.
