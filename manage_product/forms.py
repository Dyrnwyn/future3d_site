from django import forms
from .models import FotoOrder
from django.core.validators import FileExtensionValidator
from PIL import Image

class FotoOrderForm(forms.ModelForm):

    def get_available_image_extensions():
        Image.init()
        return [ext.lower()[1:] for ext in Image.EXTENSION]

    client_email = forms.EmailField(label="Email")
    town = forms.CharField(label="Город")
    ed_institution = forms.CharField(label="Номер школы/детского сада")
    the_class = forms.CharField(label="Класс/группа")
    foto_from_client = forms.ImageField(label="Фотография изделия",
                                        validators=[FileExtensionValidator(allowed_extensions=get_available_image_extensions())])

    class Meta(object):
        model = FotoOrder
        fields = ('client_email', 'town', 'ed_institution',
                  'the_class', 'foto_from_client')
