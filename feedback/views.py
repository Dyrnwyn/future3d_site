from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .forms import FeedbackForm


def contact_us(request):
    template = loader.get_template('contact-us.html')
    context = {'form': FeedbackForm}
    if request.method == 'POST':
        fdbk = FeedbackForm(request.POST)
        if fdbk.is_valid:
            fdbk.save()
            return HttpResponse(template.render(context, request))
        else:
            pass
    else:
        return HttpResponse(template.render(context, request))
