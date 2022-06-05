from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """ View definition for home page. """
    template_name = 'home.html'
