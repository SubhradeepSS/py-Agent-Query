from django.urls import path
from . import views

app_name = 'src'

urlpatterns = [
    path('', views.index, name='index'),
    path('agents', views.view_agents, name='agents'),
    path('agents/<int:id>/edit', views.edit_agent, name='edit_agent'),
    path('agents/<int:id>/edit/delete', views.del_agent, name='del_agent'),
]