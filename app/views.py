from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class PostView(TemplateView):
    template_name = 'post.html'
