from expense import views
from django.urls import path
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('',views.exp,name='exp'),
    url(r'^exp/$',views.exp,name='exp'),
    url(r'^addexp/$',views.addexp,name='addexp'),
    url(r'^add_expense/$',views.add_expense,name='add_expense'),
    url(r'^viewExp/$',views.viewExp,name='viewExp'),
    url(r'^updateExp/$',views.updateExp,name='updateExp'),
    url(r'^upd_exp/$',views.upd_exp,name='upd_exp'),
    url(r'^del_exp/$',views.del_exp,name='del_exp'),
    url(r'^report/$',views.report,name='report'),
    url(r'^sortByDate/$',views.sortByDate,name='sortByDate'),
    url(r'^sortByAmt/$',views.sortByAmt,name='sortByAmt'),
    url(r'^sortByCate/$',views.sortByCate,name='sortByCate'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#urlpatterns = [
    # ... the rest of your URLconf goes here ...
#] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

