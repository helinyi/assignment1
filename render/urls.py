from django.urls import path

from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path('cv/', views.cv_view, name='cv'),
]