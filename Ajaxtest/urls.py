from django.contrib import admin
from django.urls import path , include
import myaap.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(myaap.urls)),
]
