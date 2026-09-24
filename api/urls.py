
from django.urls import path


from .views import Employees,Emdetail


urlpatterns = [

    # path('students/',studentview),
    # path('students/<int:pk>',studientdetailview),
    path('em/',Employees.as_view()),
    path('em/<int:pk>/',Emdetail.as_view())
]
