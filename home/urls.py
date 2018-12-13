from django.urls import path
from . import views
from .views import IndexView, AboutView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('about/', AboutView.as_view(), name='about'),

    path('upload/', views.upload, name='upload'),
]