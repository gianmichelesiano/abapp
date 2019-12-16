from django.urls import path
from .import views


#http://localhost:8000/chart/sales
urlpatterns = [
    path('', views.home, name='home'),
    path('sales', views.sales, name='sales'),
    path('prove', views.prove, name='prove'),
    #url(r'^app/(?P<id>\d+)/new-page/$', views.myfunc, name="my_func"),

]

"""
    path('sales', views.sales, name='sales'),
    path('weather', views.weather_chart_view, name='weather_chart_view'),
    path('citySales', views.citySales, name='citySales'),
    path('weatherByCity', views.weatherByCity, name='weatherByCity'),
    path('pivot', views.pivot, name='pivot'),
"""