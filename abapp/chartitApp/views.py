from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import SalesReport
from programmazione.models import Esercizi, Programma, Prova
from chartit import DataPool, Chart, PivotDataPool, PivotChart
from django.utils import timezone
import pytz


def one_nonths_hence():
    return timezone.now() - timezone.timedelta(days=365)



def home(request):
    first_graph = "My First django_chartit graph"
    return render(request, 'home.html', {})
    #return HttpResponse(first_graph)


def prove(request):

    inizio = request.GET['inizio'] # => [39]
    fine = request.GET['fine'] # => [137]
    prova_sel =  request.GET['prova']

    if inizio == '':
        print('X')
        inizio =  str(one_nonths_hence()).split(' ')[0]
        #inizio = str(inizio).split(' ')[0]
        print(inizio)
    
    if fine == '':
        print('Y')
        fine =  str(timezone.now()).split(' ')[0]
        #fine = str(fine).split(' ')[0]
        print(type(fine))
    #p = Esercizi.objects.select_related('programma','prova').filter( programma__data_creazione__range =[inizio, fine]).filter(prova__id = prova_sel)

    provaTitolo = Prova.objects.filter(id=prova_sel).values('titolo').last()
    print(provaTitolo['titolo'])
    source = Esercizi.objects.select_related('programma').filter( programma__data_creazione__range =[inizio, fine]).filter(prova__id = prova_sel).order_by('-programma__data_creazione')
    sales = DataPool(
            series=[{
                'options': {
                    'source': source
                },
                'terms': [
                    'programma__data_creazione',
                    'corretto',
                    'promt_indicativo',
                    'promt_fisico',
                    'non_corretto',
                ]
            }]
    )
   
    #Step 2: Create the Chart object
    def formatXDate(input):
        formatedDate = input.strftime("%d-%m-%Y")
        return formatedDate  

    cht = Chart(
            datasource = sales,
            series_options=[{
                'options': {
                    'type': 'column',
                    'stacking': True,
                    'stack': 0
                },
                'terms': {
                    'programma__data_creazione': [
                        'corretto',

                        {
                            'promt_indicativo': {
                                'stack': 1
                            }
                        },

                        {
                            'promt_fisico': {
                                'stack': 2
                            }
                        },

                        {
                            'non_corretto': {
                                'stack': 3
                            }
                        },
                    
                    ]
                }
            }],
            chart_options =
              {'title': {
                   'text': provaTitolo['titolo']},
               'xAxis': {
                   'title':{'text': 'Data'}},
               'yAxis': {
                   'title': {'text': 'Numero'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
            x_sortf_mapf_mts=(None, formatXDate, False)
            )  
    
    return render(request,'prove.html', 
        {'chart_list': [cht]})


def sales(request):

    inizio = request.GET['inizio'] # => [39]
    fine = request.GET['fine'] # => [137] 


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
    