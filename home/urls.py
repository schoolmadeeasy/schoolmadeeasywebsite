from django.urls import path
from . import views
from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('upload/', views.upload, name='upload'),
]