from django.urls import path
from . import views

urlpatterns = [
    path('first_view', views.first_view, name='first_view'),
    path('find',views.find, name='find'),
    path('beijing_view', views.beijing_view, name='beijing_view'),
    path('shanghai_view', views.shanghai_view, name='shanghai_view'),
    path('guangzhou_view', views.guangzhou_view, name='guangzhou_view'),
    path('shenzhen_view', views.shenzhen_view, name='shenzhen_view'),
    path('wuhan_view', views.wuhan_view, name='wuhan_view'),
    path('chongqing_view', views.chongqing_view, name='chongqing_view'),
    path('hangzhou_view', views.hangzhou_view, name='hangzhou_view'),
    path('suzhou_view', views.suzhou_view, name='suzhou_view'),
    path('tianjing_view', views.tianjing_view, name='tianjing_view'),
    path('nanjing_view', views.nanjing_view, name='nanjing_view'),
    path('changsha_view', views.changsha_view, name='changsha_view'),
    path('xiameng_view', views.xiameng_view, name='xiameng_view'),

]
