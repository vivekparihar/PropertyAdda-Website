from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('forsale', views.forsale, name='forsale'),
    path('forrent', views.forrent, name='forrent'),
    path('toSell', views.toSell, name='toSell'),
    path('details/<int:myid>', views.details, name='details'),
    path('details2/<int:myid>', views.details2, name='details2'),
    path('sold', views.sold, name='sold'),

]
