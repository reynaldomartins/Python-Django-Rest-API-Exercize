from django.urls import path
from .views import (TODOsBasicAPIView, TODOsIDAPIView, TODOsFilterStateAPIView,
                    TODOsFilterDuedateAPIView, TODOsFilterStateDuedateAPIView)

App_name = 'pepperRestApp'

urlpatterns = [
    path('TODOs/', TODOsBasicAPIView.as_view(), name="todos_basic_api_method"),
    path('TODOs/<int:pk>/', TODOsIDAPIView.as_view(), name="todos_id_api_method"),
    path('TODOs/duedate/<str:td_duedate>/', TODOsFilterDuedateAPIView.as_view(), name="todos_filterduedate_api_method"),
    path('TODOs/state/<str:td_state>/', TODOsFilterStateAPIView.as_view(), name="todos_filterstate_api_method"),
    path('TODOs/search/<str:td_state>/<str:oper>/<str:td_duedate>/', TODOsFilterStateDuedateAPIView.as_view(), name="todos_filterstateduedate_api_method"),
]
