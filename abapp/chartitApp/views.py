from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import SalesReport
from chartit import DataPool, Chart, PivotDataPool, PivotChart
"""
from .models import SalesReport, MonthlyWeatherByCity, SalesHistory
from chartit import DataPool, Chart, PivotDataPool, PivotChart
from django.db.models import Avg, Sum, Count, Min, Max
"""


def home(request):
    first_graph = "My First django_chartit graph"
    return HttpResponse(first_graph)


def sales(request):
    sales = DataPool(
        series=
            [{'options': {
            #    'source': SalesReport.objects.all()},
            'source': SalesReport},
            #'source': SalesReport.objects.filter(sales__lte=10.00)},
                'terms': [{'month': 'month',
                'sales': 'sales'}]
                },
        ]) 


    def monthname(month_num):
        names = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
             7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = sales,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{
                  'month': [
                    'sales']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Sales Amounts Over Months'},
               'xAxis': {
                   'title':{'text': 'Sales Total'}},
               'yAxis': {
                   'title': {'text': 'Month Number'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
            x_sortf_mapf_mts=(None, monthname, False))  
    
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = sales,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'sales']
                  }}],
    
            chart_options =
              {'title': {
                   'text': 'Sales Amounts Over Months - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'Sales Total'}},
               'yAxis': {
                   'title': {'text': 'Month Number'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
            x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})
    