from django.urls import path
from .views import IndexView, ContactView, AboutView, PostView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('/sobre', AboutView.as_view(), name='about'),
    path('/contato', ContactView.as_view(), name='contact'),
    path('/post', PostView.as_view(), name='post'),
]