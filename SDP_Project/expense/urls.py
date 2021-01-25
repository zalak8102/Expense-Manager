from expense import views
from django.urls import path
from django.conf.urls import include, url

urlpatterns=[
    path('',views.expense,name='expense'),
    url(r'^expense/$',views.expense,name='expense'),
    url(r'^report/$',views.report,name='report'),

]
