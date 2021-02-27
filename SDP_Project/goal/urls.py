from goal import views
from django.urls import path
from django.conf.urls import url

urlpatterns=[
    path('',views.goals,name='goals'),
    url(r'^goals/$',views.goals,name='goals'),
    url(r'^addgoal/$',views.addgoal,name='addgoal'),
    url(r'^add_goal/$',views.add_goal,name='add_goal'),
    url(r'^del_goal/$',views.del_goal,name='del_goal'),
    url(r'^contri/$',views.contri,name='contri'),
    url(r'^updateGoal/$',views.updateGoal,name='updateGoal'),
    url(r'^upd_goal/$',views.upd_goal,name='upd_goal'),  

]
