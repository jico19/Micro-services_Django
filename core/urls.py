from django.urls import path
from . import views


urlpatterns = [
    path('chat-bot/', views.SampleView.as_view(), name="example")
]
