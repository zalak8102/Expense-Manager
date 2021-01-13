from django.conf.urls import url
from signup import views
from django.urls import path

urlpatterns=[
    path('',views.home,name='home'),
    url(r'^register/$',views.register,name='register'),
    url(r'^user_register/$',views.user_register,name='user_register'),
    url(r'^login/$',views.login,name='login'),
    url(r'^signin/$',views.signin,name='signin'),
     url(r'^logout/$',views.logout,name='logout'),
    #path('',views.signup,name='register'),
]