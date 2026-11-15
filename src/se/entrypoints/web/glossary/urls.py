from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path(
        'presentation/', views.PresentationView.as_view(), name='presentation'
    ),
]
