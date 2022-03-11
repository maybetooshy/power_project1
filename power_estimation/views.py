from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.db.models import Sum

from .models import test_table, parameter, ctrl
from .calculation import *
import json
# Create your views here.


def index(request):    
    return render(request, 'power_estimation/test.html')

### 클릭 --> 데이터 열어서 출력하기 (done)
### sqlite에 있는 데이터 db(모델)로 연결 (같은건가?) --> sqlite에 id column 필요! (done)
### input으로 nand 이름 받아서(드롭다운메뉴?) (done: input type=submit 추가) // 
### 계산 후 (다른 파일로 가서 계산해서 sql로 넣어야 할듯. done(calcultion_test)) // 결과 출력해보기 (표 형태 --> 가능하면 차트도?)
### html 구성해보기
### CTRL별로 세부 파일 리스트 만들기
### ELAN 누르면 세부 elan 데이터들 불러오기
### 세부 데이터 누르면 밑에 테이블에 반영 ㄱㄱ

def test2(request):
#     month_text = request.GET.get('month')

#     if month_text == '01':

#         calculation_test()
        
#         candidates = parameter.objects.all()
#         # candidates = parameter.objects.filter(name='nvcc')[0]
#         context = {'candidates':candidates}

#         return render(request, 'power_estimation/test2.html', context)

    return render(request, 'power_estimation/test2.html')

def chartsview(request):
    return render(request, 'power_estimation/charts.html')

def tablesview(request):
    return render(request, 'power_estimation/tables.html')

def userview(request):
    return render(request, 'power_estimation/usermode.html')

def userview2(request):
    return render(request, 'power_estimation/usermode2.html')    

def expertview(request):
    return render(request, 'power_estimation/expertmode.html')

def selected(request):
    ctrl_sel = request.GET.get('CTRL를 골라보자 !') ### value를 가져오는 듯. value를 파일 이름으로 해서 불러오게 하기 가능?

#    update_ctrl(ctrl_sel)

    candidates = ctrl.objects.filter(name=ctrl_sel) ### 한개만 골라서 보내기! 지금 받은 선택지의 value
    # candidates = ctrl.objects.values('name').annotate(ud_sum=Sum('ud'))
    context = {'candidates':candidates} ### 여러개 딕셔너리로 전달하면 골라서 출력할 수 있을 듯

    return render(request, 'power_estimation/usermode.html', context)

    # return HttpResponseRedirect(reverse('power_estimation:userview'))

def filepath(request):
    name = []
    queryset = ctrl.objects.all()
    for item in queryset:
        name.append(item.name)

    return JsonResponse(data={
        'name': name, ###[ctrl_1, ctrl_2] 각각이 data.item
    })

def filepath2(request):

    ctrl_sel = request.GET.get('name')
    
    name = [ctrl_sel]
    # queryset = ctrl.objects.filter(name=ctrl_sel)
    # for item in queryset:
    #     name.append(item.name)

    return JsonResponse(data={
        'name': name, ###[ctrl_1, ctrl_2] 각각이 data.item
    })

        # candidates = ctrl.objects.values(ctrl_sel).annotate(ud_sum=Sum('ud'))
        # context = {'candidates':candidates}

        # return render(request, 'power_estimation/usermode2.html', context)


# def chartview(request): ######################################   ajax 연습용
#     # ctrl_sel = request.GET.get('CTRL를 골라보자 !')

#     labels = []
#     data = []

#     #queryset = ctrl.objects.filter(name='ctrl_1').values('name').annotate(ud=Sum('ud'))
#     queryset = ctrl.objects.all()
#     for entry in queryset:
#         labels.append(entry.name)
#         data.append(entry.nd)
    
#     return JsonResponse(data={
#         'labels': labels,
#         'data': data,
#     })

#     # candidates_chart = ctrl.objects.filter('ctrl_1') ### 한개만 골라서 보내기! 지금 받은 선택지의 value
#     # # candidates = ctrl.objects.values('name').annotate(ud_sum=Sum('ud'))
#     # context = {'candidates_chart':candidates_chart}

#     # return render(request, 'power_estimation/usermode.html', context)
