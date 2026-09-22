
from django.urls import path


from .views import studentview

urlpatterns = [

    path('students/',studentview)
]
