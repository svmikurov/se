from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class PresentationView(TemplateView):
    template_name = 'presentation.html'
