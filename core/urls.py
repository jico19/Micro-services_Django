from django.urls import path
from . import views


urlpatterns = [
    path('test/', views.SampleView.as_view(), name="example")
]
