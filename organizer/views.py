from django import views
from django.views import generic

class Homepage(generic.TemplateView):
    template_name = 'index.html'
