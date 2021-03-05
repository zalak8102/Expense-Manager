from django.conf.urls import url
from income import views
from django.urls import path

urlpatterns=[
    path('',views.income,name='income'),
    url(r'^income/$',views.income,name='income'),
    url(r'^addinc/$',views.addinc,name='addinc'),
    url(r'^add_income/$',views.add_income,name='add_income'),
    url(r'^del_income/$',views.del_income,name='del_income'),
    url(r'^updateinc/$',views.updateinc,name='updateinc'),
    url(r'^upd_income/$',views.upd_income,name='upd_income'), 
  ]