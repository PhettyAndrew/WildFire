from django.urls import path
from . import views

app_name='eapp'

urlpatterns=[
    path('',views.index,name='index'),
    path('(?P<event_id>[0-9]+)/',views.details,name='details'),
    path('add_event',views.add_Event,name='add_event'),
    path('(?P<event_id>[0-9]+)/comment/',views.comment,name='comment'),
    path('(?P<event_id>[0-9]+/login/edit/',views.login_edit,name='login_edit'),
    path('(?P<event_id>[0-9]+/delete',views.delete,name='delete'),
]