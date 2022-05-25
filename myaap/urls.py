from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index),
    path('save_Book', views.saveBook, name="Save book"),
    path('Api',views.jsondata)
]
