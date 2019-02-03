from django.urls import path, include
from django.contrib.flatpages import views


urlpatterns = [
    path('<path:url>', views.flatpage),
]
