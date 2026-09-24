
from django.urls import path,include

from rest_framework.routers  import DefaultRouter
from .views import Employeviewset

router=DefaultRouter()
router.register('em',Employeviewset,basename='employee')
urlpatterns = [

    # path('students/',studentview),
    # path('students/<int:pk>',studientdetailview),
    # path('em/',Employees.as_view()),
    # path('em/<int:pk>/',Emdetail.as_view())
    path('',include(router.urls))
]
