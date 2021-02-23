from goal import views
from django.urls import path
from django.conf.urls import url

urlpatterns=[
    path('',views.goals,name='goals'),
    url(r'^goals/$',views.goals,name='goals'),
    url(r'^addgoal/$',views.addgoal,name='addgoal'),
    url(r'^add_goal/$',views.add_goal,name='add_goal'),
]
