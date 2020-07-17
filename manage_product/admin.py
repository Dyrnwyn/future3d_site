from django.contrib import admin
from .models import ProductId, Email, Town, Worker, FotoOrder, Articles
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from datetime import date
from django.template.loader import render_to_string
from future3d_site.settings import BASE_DIR, HOSTNAME_SITE
from django.http import HttpResponseRedirect
import json


host_name_for_email = HOSTNAME_SITE + 'product/'


class ProductIdAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'template', 'email',
                    'date_opening', 'payment_id', 'paid', 'date_payment',
                    'stage', 'product_link')
    list_display_links = ('product_id', 'template', 'email')
    actions = ('send_product_link', 'send_emailmessage_for_pay',
               'create_product_link', 'generate_json_for_pay')

    def generate_json_for_pay(self, request, queryset):
        json_file = open(BASE_DIR + '/upload/' + 'product_for_pay.json', 'w',
                         encoding='utf-8')
        json_data = {}
        for rec in queryset:
            obj = ProductId.objects.get(product_id=rec.product_id)
            if obj.stage == 'pay':
                json_data[str(obj.product_id)] = {'template': obj.template,
                                                  'payment_id': obj.payment_id,
                                                  'email': str(obj.email),
                                                  'paid': str(obj.paid)}
        json.dump(json_data, json_file, indent=4)
        json_file.close()
        return HttpResponseRedirect('/admin/manage_product/download_json')

    generate_json_for_pay.short_description = 'Сформировать файл оплаты для 1С'

    def create_product_link(self, request, queryset):
        for rec in queryset:
            obj = ProductId.objects.get(product_id=rec.product_id)
            obj.product_link = host_name_for_email + str(rec.product_id)
            obj.save()

    create_product_link.short_description = 'Создать ссылку на изделие'

    def send_product_link(self, request, queryset):
        for rec in queryset:
            context = {'product_link': host_name_for_email + str(rec.product_id)}
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


class FotoOrderAdmin(admin.ModelAdmin):
    list_display = ('client_email', 'town', 'ed_institution',
                    'the_class')

admin.site.register(ProductId, ProductIdAdmin)
admin.site.register(Email, EmailAdmin)
admin.site.register(Town)
admin.site.register(Worker)
admin.site.register(FotoOrder, FotoOrderAdmin)
admin.site.register(Articles)
# Register your models here.
