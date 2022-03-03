from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

from .models import test_table, parameter
from .calculation import *
# Create your views here.


def index(request):    
    return render(request, 'power_estimation/test.html')

### 클릭 --> 데이터 열어서 출력하기 (done)
### sqlite에 있는 데이터 db(모델)로 연결 (같은건가?) --> sqlite에 id column 필요! (done)
### input으로 nand 이름 받아서(드롭다운메뉴?) (done: input type=submit 추가) // 
### 계산 후 (다른 파일로 가서 계산해서 sql로 넣어야 할듯. done(calcultion_test)) // 결과 출력해보기 (표 형태 --> 가능하면 차트도?)
### html 구성해보기

def openfile(request):
    month_text = request.GET.get('month')

    if month_text == '01':

        calculation_test()
        
        candidates = parameter.objects.all()
#        candidates = parameter.objects.filter(name='nvcc')[0]
        context = {'candidates':candidates}

        return render(request, 'power_estimation/test2.html', context)

#    candidates = test_table.objects.all()
#    context = {'candidates':candidates}

#    return render(request, 'power_estimation/test2.html', context)


# def indexview(request):``
#     return render(request, 'power_estimation/index.html')

def chartsview(request):
    return render(request, 'power_estimation/charts.html')

def tablesview(request):
    return render(request, 'power_estimation/tables.html')