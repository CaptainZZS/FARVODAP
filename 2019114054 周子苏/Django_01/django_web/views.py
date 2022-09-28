from django.shortcuts import render

import ETL4
from PYETL import ETL2,ETL3
from jinja2 import Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig
from django.http import HttpResponse

CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./django_web/templates"))

from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Pie, Page


def index_view(request):
    return render(request, 'index.html')

def first_view(request):
    return render(request, 'first.html')

def find(request):
    cs = str(request.POST["cs"])
    gzjy = str(request.POST["gzjy"])
    gs = str(request.POST["gs"])
    xl = str(request.POST["xl"])
    print(cs,gs,xl,gzjy)
    list_data = ETL3.find_data(cs,gs,xl,gzjy)
    return render(request,'find.html',{"list_data":list_data})

def beijing_view(request):
    list1 = ETL2.beijing()
    page_1 = ETL4.visualization(list1)
    return HttpResponse(page_1.render_embed())

def shanghai_view(request):
    list1 = ETL2.shanghai()
    page_1 = ETL4.visualization(list1)
    return HttpResponse(page_1.render_embed())

def guangzhou_view(request):
    list1 = ETL2.guangzhou()
    page_1 = ETL4.visualization(list1)
    return HttpResponse(page_1.render_embed())

def shenzhen_view(request):
    list1 = ETL2.shenzheng()
    page_1 = ETL4.visualization(list1)
    return HttpResponse(page_1.render_embed())

def wuhan_view(request):
    list1 = ETL2.wuhan()
    page_1 = ETL4.visualization(list1)
    return HttpResponse(page_1.render_embed())

def chongqing_view(request):
    list1 = ETL2.chongqing()
    page_1 = ETL4.visualization(list1)
    return HttpResponse(page_1.render_embed())

def hangzhou_view(request):
    list1 = ETL2.hangzhou()
    page_1 = ETL4.visualization(list1)
    return HttpResponse(page_1.render_embed())

def suzhou_view(request):
    list1 = ETL2.suzhou()
    page_1 = ETL4.visualization(list1)
    return HttpResponse(page_1.render_embed())

def tianjing_view(request):
    list1 = ETL2.tianjing()
    page_1 = ETL4.visualization(list1)
    return HttpResponse(page_1.render_embed())

def nanjing_view(request):
    list1 = ETL2.nanjing()
    page_1 = ETL4.visualization(list1)
    return HttpResponse(page_1.render_embed())

def changsha_view(request):
    list1 = ETL2.changshang()
    page_1 = ETL4.visualization(list1)
    return HttpResponse(page_1.render_embed())

def xiameng_view(request):
    list1 = ETL2.xiameng()
    page_1 = ETL4.visualization(list1)
    return HttpResponse(page_1.render_embed())
