from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from api.models import *
from api.forms import *
from rest_framework import viewsets
from api.serializers import *
import bcrypt
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import django_excel as excel
from django import forms
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory
import json
from operator import itemgetter
from django.db.models import Sum
import csv


class UploadFileForm(forms.Form):
    file = forms.FileField()

def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filehandle = request.FILES['file']
            return excel.make_response(filehandle.get_sheet(),"csv",file_name = "download")
    else:
        form = UploadFileForm()
    return render(request,'upload_form.html',{'form': form, 'title': 'Excel file and download', 'header' : ('Please choose any excel file '  +  'from your pc')})

#add users
#Healtcheck
def process_request(request):
        try:
            u = Allocatedeicdetail.objects.all()
            success = True
        except:
            success = False

        if success == True:
            j = {"status":"OK"}
            return JsonResponse(j)
        else:
            j = {"status" : "NOT OK"}
            return JsonResponse(j)

#@crsf_exempt
def user_list(request):
    if request.method =='GET':
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)

#@csrf_exempt
def user_detail(request,pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user,data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)

def actualtotalload_list(request):
    if request.method == 'GET':
        actualtotalloads = Actualtotalload.objects.all()
        data_to_export = []
        for data in actualtotalloads:
            areatype = data.areatypecodeid.areatypecodetext
            map = data.mapcodeid.mapcodetext
            resolution = data.resolutioncodeid.resolutioncodetext
            data_to_export.append({
            'source': 'entsoe',
            'dataset': 'Actualtotalload',
            'areaname': data.areaname,
            'areatypecode': areatype,
            'mapcode': map,
            'resolutioncode': resolution,
            'year': data.year,
            'month': data.month,
            'day': data.day,
            'datetimeUTC': data.datetime,
            'ActualTotalLoadValue' : data.totalloadvalue,
            'updatetimeUTC' : data.updatetime
            })
        return JsonResponse(data_to_export,json_dumps_params={'indent': 2},safe = False)


def actual(request,areaname,resolutioncode,date,info):
    if date == 'date':
        tmp = info[0:4]
        year = int(tmp)
        tmp = info[5:7]
        month = int(tmp)
        tmp = info[8:10]
        day = int(tmp)
        if len(info) > 10 :
            format = info[18:]
        else:
            format = 'json'
        return actualtotalload_detail2(request,areaname,resolutioncode,year,month,day,format)
    elif date == 'month':
        tmp = info[0:4]
        year = int(tmp)
        tmp = info[5:7]
        month = int(tmp)
        if len(info) > 9:
            format = info[15:]
        else:
            format = 'json'
        return actualtotalload_detail1(request,areaname,resolutioncode,year,month,format)
    elif date == 'year':
        tmp = info[0:4]
        year = int(tmp)
        if len(info) > 6:
            format = info[12:]
        else:
            format = 'json'
        return actualtotalload_detail(request,areaname,resolutioncode,year,format)
    else:
        return HttpResponse("Bad request")

def aggre(request,areaname,productiontype,resolutioncode,date,info):
    if date == 'date':
        tmp = info[0:4]
        year = int(tmp)
        tmp = info[5:7]
        month = int(tmp)
        tmp = info[8:10]
        day = int(tmp)
        if len(info) > 10 :
            format = info[18:]
        else:
            format = 'json'
        return aggregatedgenerationpertype_detail2(request,areaname,productiontype,resolutioncode,year,month,day,format)
    elif date == 'month':
        tmp = info[0:4]
        year = int(tmp)
        tmp = info[5:7]
        month = int(tmp)
        if len(info) > 9:
            format = info[15:]
        else:
            format = 'json'
        return aggregatedgenerationpertype_detail1(request,areaname,productiontype,resolutioncode,year,month,format)
    elif date == 'year':
        tmp = info[0:4]
        year = int(tmp)
        if len(info) > 6:
            format = info[12:]
        else:
            format = 'json'
        return aggregatedgenerationpertype_detail(request,areaname,productiontype,resolutioncode,year,format)
    else:
        return HttpResponse("Bad request")

def dayahead(request,areaname,resolutioncode,date,info):
    if date == 'date':
        tmp = info[0:4]
        year = int(tmp)
        tmp = info[5:7]
        month = int(tmp)
        tmp = info[8:10]
        day = int(tmp)
        if len(info) > 10 :
            format = info[18:]
        else:
            format = 'json'
        return dayaheadtotalloadforecast_detail2(request,areaname,resolutioncode,year,month,day,format)
    elif date == 'month':
        tmp = info[0:4]
        year = int(tmp)
        tmp = info[5:7]
        month = int(tmp)
        if len(info) > 9:
            format = info[15:]
        else:
            format = 'json'
        return dayaheadtotalloadforecast_detail1(request,areaname,resolutioncode,year,month,format)
    elif date == 'year':
        tmp = info[0:4]
        year = int(tmp)
        if len(info) > 6:
            format = info[12:]
        else:
            format = 'json'
        return dayaheadtotalloadforecast_detail(request,areaname,resolutioncode,year,format)
    else:
        return HttpResponse("Bad request")

def actualvs(request,areaname,resolutioncode,date,info):
    if date == 'date':
        tmp = info[0:4]
        year = int(tmp)
        tmp = info[5:7]
        month = int(tmp)
        tmp = info[8:10]
        day = int(tmp)
        if len(info) > 10 :
            format = info[18:]
        else:
            format = 'json'
        return actualvsforecast_detail2(request,areaname,resolutioncode,year,month,day,format)
    elif date == 'month':
        tmp = info[0:4]
        year = int(tmp)
        tmp = info[5:7]
        month = int(tmp)
        if len(info) > 9:
            format = info[15:]
        else:
            format = 'json'
        return actualvsforecast_detail1(request,areaname,resolutioncode,year,month,format)
    elif date == 'year':
        tmp = info[0:4]
        year = int(tmp)
        if len(info) > 6:
            format = info[12:]
        else:
            format = 'json'
        return actualvsforecast_detail(request,areaname,resolutioncode,year,format)
    else:
        return HttpResponse("Bad request")

def actualtotalload_detail2(request,areaname,resolutioncode,year,month,day,format):
    tmp = Resolutioncode.objects.filter(resolutioncodetext = resolutioncode)
    resolutioncodeid = tmp[0].id
    data_to_export = Actualtotalload.objects.filter(areaname = areaname,resolutioncodeid = resolutioncodeid,year=year,month=month,day=day)
    data = []
    for dd in data_to_export:
        areatypecode = dd.areatypecodeid.areatypecodetext
        mapcode = dd.mapcodeid.mapcodetext
        data.append({
        'source': 'entso-e',
        'dataset': 'ActualTotalLoad',
        'areaname': dd.areaname,
        'areatypecode': areatypecode,
        'mapcode': mapcode,
        'resolutioncode': resolutioncode,
        'year': dd.year,
        'month': dd.month,
        'day': dd.day,
        'datetime': dd.datetime,
        'actualtotalloadvalue': dd.totalloadvalue,
        'updatetime':dd.updatetime
        })
    if data == []:
        return HttpResponse("NO DATA")
    if request.method == 'GET':
        newdata = sorted(data, key=lambda k: k['datetime'])
        if  format == 'json':
            return JsonResponse(newdata,json_dumps_params={'indent': 2},safe = False)
        elif format == 'csv':
            csv_file = "Names.csv"
            csv_columns = ['source','dataset','areaname','areatypecode','mapcode','resolutioncode','year','month','day','datetime','actualtotalloadvalue','updatetime']
            with open(csv_file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for d in newdata:
                    writer.writerow(d)
            with open(csv_file) as csvfile:
                response = HttpResponse(csvfile,content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename = "ActualTotalLoad.csv"'
                return response
        else:
            return HttpResponse("Bad request")

def actualtotalload_detail1(request,areaname,resolutioncode,year,month,format):
    tmp = Resolutioncode.objects.filter(resolutioncodetext = resolutioncode)
    resolutioncodeid = tmp[0].id
    data_to_export = Actualtotalload.objects.filter(areaname = areaname,resolutioncodeid = resolutioncodeid,year=year,month=month)
    data = []
    for dd in data_to_export:
        areatypecode = dd.areatypecodeid.areatypecodetext
        mapcode = dd.mapcodeid.mapcodetext
        sum = Actualtotalload.objects.filter(areaname = areaname,resolutioncodeid = resolutioncodeid,year=year,month=month,day =dd.day,areatypecodeid = dd.areatypecodeid,mapcodeid = dd.mapcodeid).aggregate(Sum('totalloadvalue'))
        temp = ({
        'source': 'entso-e',
        'dataset': 'ActualTotalLoad',
        'areaname': dd.areaname,
        'areatypecode': areatypecode,
        'mapcode': mapcode,
        'resolutioncode': resolutioncode,
        'year': dd.year,
        'month': dd.month,
        'day': dd.day,
        'actualtotalloadvalue': sum,
        })
        if temp  not in data:
            data.append(temp)
    if data == []:
        return HttpResponse("NO DATA")
    if request.method == 'GET':
        newdata = sorted(data, key=lambda k: k['day'])
        if format =='json':
            return JsonResponse(newdata,json_dumps_params={'indent': 2},safe = False)
        elif format == 'csv':
            csv_file = "Names.csv"
            csv_columns = ['source','dataset','areaname','areatypecode','mapcode','resolutioncode','year','month','day','datetime','actualtotalloadvalue','updatetime']
            with open(csv_file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for d in newdata:
                    writer.writerow(d)
            with open(csv_file) as csvfile:
                response = HttpResponse(csvfile,content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename = "ActualTotalLoad.csv"'
                return response
        else:
            return HttpResponse("Bad rerquest")

def actualtotalload_detail(request,areaname,resolutioncode,year,format):
    tmp = Resolutioncode.objects.filter(resolutioncodetext = resolutioncode)
    resolutioncodeid = tmp[0].id
    data_to_export = Actualtotalload.objects.filter(areaname = areaname,resolutioncodeid = resolutioncodeid,year=year)
    data = []
    for dd in data_to_export:
        areatypecode = dd.areatypecodeid.areatypecodetext
        mapcode = dd.mapcodeid.mapcodetext
        sum = Actualtotalload.objects.filter(areaname = areaname,resolutioncodeid = resolutioncodeid,year=year,month=dd.month,areatypecodeid = dd.areatypecodeid,mapcodeid = dd.mapcodeid).aggregate(Sum('totalloadvalue'))
        temp = ({
        'source': 'entso-e',
        'dataset': 'ActualTotalLoad',
        'areaname': dd.areaname,
        'areatypecode': areatypecode,
        'mapcode': mapcode,
        'resolutioncode': resolutioncode,
        'year': dd.year,
        'month': dd.month,
        'actualtotalloadvalue': sum,
        })
        if temp  not in data:
            data.append(temp)
    if data == []:
        return HttpResponse("NO DATA")
    if request.method == 'GET':
        newdata = sorted(data, key=lambda k: k['month'])
        if format=='json':
            return JsonResponse(newdata,json_dumps_params={'indent': 2},safe = False)
        elif format=='csv':
            csv_file = "Names.csv"
            csv_columns = ['source','dataset','areaname','areatypecode','mapcode','resolutioncode','year','month','day','datetime','actualtotalloadvalue','updatetime']
            with open(csv_file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for d in newdata:
                    writer.writerow(d)
            with open(csv_file) as csvfile:
                response = HttpResponse(csvfile,content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename = "ActualTotalLoad.csv"'
                return response
        else:
            return HttpResponse("Bad request")

#Aggregatedgenerationpertype
def aggregatedgenerationpertype_list(request):
    agge = Aggregatedgenerationpertype.objects.all()
    data_to_export = []
    for data in agge:
        areatype = data.areatypecodeid.areatypecodetext
        map = data.mapcodeid.mapcodetext
        resolution = data.resolutioncodeid.resolutioncodetext
        production = data.productiontypeid.productiontypetext
        data_to_export.append({
        'source': 'entso-e',
        'dataset': 'ActualTotalLoad',
        'areaname': data.areaname,
        'areatypecode': areatype,
        'mapcode': map,
        'resolutioncode': resolution,
        'year': data.year,
        'month': data.month,
        'day': data.day,
        'datetime': data.datetime,
        'productiontype': production,
        'ActualGenerationOutputValue': data.actualgenerationoutput,
        'updatetime':data.updatetime
        })
    if data == []:
        return HttpResponse("NO DATA")
    if request.method == 'GET':
        return JsonResponse(data_to_export,json_dumps_params={'indent': 2},safe = False)


#@csrf_exempt
def aggregatedgenerationpertype_detail2(request,areaname,productiontype,resolutioncode,year,month,day,format):
    tmp = Resolutioncode.objects.filter(resolutioncodetext = resolutioncode)
    tmp2 = Productiontype.objects.filter(productiontypetext = productiontype)
    data_to_export = Aggregatedgenerationpertype.objects.filter(areaname = areaname, resolutioncodeid = tmp[0], productiontypeid = tmp2[0],year = year, month = month, day = day)
    data = []
    for dd in data_to_export:
        areatypecode = dd.areatypecodeid.areatypecodetext
        mapcode =dd.mapcodeid.mapcodetext
        data.append({
        'source': 'entso-e',
        'dataset': 'ActualTotalLoad',
        'areaname': dd.areaname,
        'areatypecode': areatypecode,
        'mapcode': mapcode,
        'resolutioncode': resolutioncode,
        'year': dd.year,
        'month': dd.month,
        'day': dd.day,
        'datetime': dd.datetime,
        'productiontype': productiontype,
        'ActualGenerationOutputValue': dd.actualgenerationoutput,
        'updatetime':dd.updatetime
        })
    if data == []:
        return HttpResponse("NO DATA")
    if request.method == 'GET':
        newdata = sorted(data, key=lambda k: k['datetime'])
        if format == 'json':
            return JsonResponse(newdata,json_dumps_params={'indent': 2},safe = False)
        elif format =='csv':
            csv_file = "Names.csv"
            csv_columns = ['source','dataset','areaname','areatypecode','mapcode','resolutioncode','year','month','day','datetime','actualtotalloadvalue','updatetime']
            with open(csv_file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for d in newdata:
                    writer.writerow(d)
            with open(csv_file) as csvfile:
                response = HttpResponse(csvfile,content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename = "AggreatedGenerationPerType.csv"'
                return response
        else:
            return HttpResponse("Bad request")

def aggregatedgenerationpertype_detail1(request,areaname,productiontype,resolutioncode,year,month,format):
    tmp = Resolutioncode.objects.filter(resolutioncodetext = resolutioncode)
    tmp2 = Productiontype.objects.filter(productiontypetext = productiontype)
    data_to_export = Aggregatedgenerationpertype.objects.filter(areaname = areaname, resolutioncodeid = tmp[0], productiontypeid = tmp2[0],year = year, month = month)
    data = []
    for dd in data_to_export:
        areatypecode = dd.areatypecodeid.areatypecodetext
        mapcode =dd.mapcodeid.mapcodetext
        sum = Aggregatedgenerationpertype.objects.filter(areaname = areaname, resolutioncodeid = tmp[0], productiontypeid = tmp2[0],year = year, month = month,day = dd.day,areatypecodeid = dd.areatypecodeid,mapcodeid = dd.mapcodeid).aggregate(Sum('actualgenerationoutput'))
        temp = ({
        'source': 'entso-e',
        'dataset': 'ActualTotalLoad',
        'areaname': dd.areaname,
        'areatypecode': areatypecode,
        'mapcode': mapcode,
        'resolutioncode': resolutioncode,
        'year': dd.year,
        'month': dd.month,
        'day': dd.day,
        'productiontype': productiontype,
        'ActualGenerationOutputValue': sum ,
        })
        if temp not in data:
            data.append(temp)
    if data == []:
        return HttpResponse("NO DATA")
    if request.method == 'GET':
        newdata = sorted(data, key=lambda k: k['day'])
        if format=='json':
            return JsonResponse(newdata,json_dumps_params={'indent': 2},safe = False)
        elif format=='csv':
            csv_file = "Names.csv"
            csv_columns = ['source','dataset','areaname','areatypecode','mapcode','resolutioncode','year','month','day','datetime','actualtotalloadvalue','updatetime']
            with open(csv_file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for d in newdata:
                    writer.writerow(d)
            with open(csv_file) as csvfile:
                response = HttpResponse(csvfile,content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename = "AggreatedGenerationPerType.csv"'
                return response
        else:
            return HttpResponse("Bad request")

def aggregatedgenerationpertype_detail(request,areaname,productiontype,resolutioncode,year,format):
    tmp = Resolutioncode.objects.filter(resolutioncodetext = resolutioncode)
    tmp2 = Productiontype.objects.filter(productiontypetext = productiontype)
    data_to_export = Aggregatedgenerationpertype.objects.filter(areaname = areaname, resolutioncodeid = tmp[0], productiontypeid = tmp2[0],year = year)
    data = []
    for dd in data_to_export:
        areatypecode = dd.areatypecodeid.areatypecodetext
        mapcode =dd.mapcodeid.mapcodetext
        sum = Aggregatedgenerationpertype.objects.filter(areaname = areaname, resolutioncodeid = tmp[0], productiontypeid = tmp2[0],year = year, month = dd.month,areatypecodeid = dd.areatypecodeid,mapcodeid = dd.mapcodeid).aggregate(Sum('actualgenerationoutput'))
        temp = ({
        'source': 'entso-e',
        'dataset': 'ActualTotalLoad',
        'areaname': dd.areaname,
        'areatypecode': areatypecode,
        'mapcode': mapcode,
        'resolutioncode': resolutioncode,
        'year': dd.year,
        'month': dd.month,
        'productiontype': productiontype,
        'ActualGenerationOutputValue': sum ,
        })
        if temp not in data:
            data.append(temp)
    if data == []:
        return HttpResponse("NO DATA")
    if request.method == 'GET':
        newdata = sorted(data, key=lambda k: k['month'])
        if format == 'json':
            return JsonResponse(data,json_dumps_params={'indent': 2},safe = False)
        elif format == 'csv':
            csv_file = "Names.csv"
            csv_columns = ['source','dataset','areaname','areatypecode','mapcode','resolutioncode','year','month','day','datetime','actualtotalloadvalue','updatetime']
            with open(csv_file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for d in newdata:
                    writer.writerow(d)
            with open(csv_file) as csvfile:
                response = HttpResponse(csvfile,content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename = "AggreatedGenerationPerType.csv"'
                return response
        else:
            return HttpResponse("Bad request")

#dayaheadtotalloadforecast

#@crsf_exempt
def dayaheadtotalloadforecast_list(request):
    dayahead = Dayaheadtotalloadforecast.objects.all()
    data_to_export = []
    for data in dayahead:
        areatypecode = data.areatypecodeid.areatypecodetext
        mapcode = data.mapcodeid.mapcodetext
        resolutioncode = data.resolutioncodeid.resolutioncodetext

        data_to_export.append({
        'source': 'entso-e',
        'dataset': 'ActualTotalLoad',
        'areaname': data.areaname,
        'areatypecode': areatypecode,
        'mapcode': mapcode,
        'resolutioncode': resolutioncode,
        'year': data.year,
        'month': data.month,
        'day': data.day,
        'datetime': data.datetime,
        'productiontype': data.totalloadvalue,
        'DayAheadTotalLoadForecastValue': data.actualgenerationoutput,
        'updatetime':data.updatetime
        })
    if data == []:
        return HttpResponse("NO DATA")
    if request.method == 'GET':
        return JsonResponse(data_to_export,json_dumps_params={'indent': 2},safe = False)

#@csrf_exempt
def dayaheadtotalloadforecast_detail2(request,areaname,resolutioncode,year,month,day,format):
    tmp = Resolutioncode.objects.filter(resolutioncodetext = resolutioncode)
    data_to_export = Dayaheadtotalloadforecast.objects.filter(areaname = areaname, resolutioncodeid = tmp[0],year = year, month = month, day = day)
    data = []
    for dd in data_to_export:
        areatypecode = dd.areatypecodeid.areatypecodetext
        mapcode =dd.mapcodeid.mapcodetext
        data.append({
        'source': 'entso-e',
        'dataset': 'ActualTotalLoad',
        'areaname': dd.areaname,
        'areatypecode': areatypecode,
        'mapcode': mapcode,
        'resolutioncode': resolutioncode,
        'year': dd.year,
        'month': dd.month,
        'day': dd.day,
        'datetime': dd.datetime,
        'DayAheadTotalLoadForecastValue': dd.totalloadvalue,
        'updatetime':dd.updatetime
        })
    if data == []:
        return HttpResponse("NO DATA")
    if request.method == 'GET':
        newdata = sorted(data, key=lambda k: k['datetime'])
        if format == 'json':
            return JsonResponse(newdata,json_dumps_params={'indent': 2},safe = False)
        elif format == 'csv':
            csv_file = "Names.csv"
            csv_columns = ['source','dataset','areaname','areatypecode','mapcode','resolutioncode','year','month','day','datetime','actualtotalloadvalue','updatetime']
            with open(csv_file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for d in newdata:
                    writer.writerow(d)
            with open(csv_file) as csvfile:
                response = HttpResponse(csvfile,content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename = "DayAheadTotalLoadForecast.csv"'
                return response
        else:
            return HttpResponse("Bad request")

def dayaheadtotalloadforecast_detail1(request,areaname,resolutioncode,year,month,format):
    tmp = Resolutioncode.objects.filter(resolutioncodetext = resolutioncode)
    data_to_export = Dayaheadtotalloadforecast.objects.filter(areaname = areaname, resolutioncodeid = tmp[0],year = year, month = month)
    data = []
    for dd in data_to_export:
        areatypecode = dd.areatypecodeid.areatypecodetext
        mapcode =dd.mapcodeid.mapcodetext
        sum =  Dayaheadtotalloadforecast.objects.filter(areaname = areaname, resolutioncodeid = tmp[0],year = year, month = month, day = dd.day,mapcodeid = dd.mapcodeid,areatypecodeid = dd.areatypecodeid).aggregate(Sum('totalloadvalue'))
        temp = ({
        'source': 'entso-e',
        'dataset': 'ActualTotalLoad',
        'areaname': dd.areaname,
        'areatypecode': areatypecode,
        'mapcode': mapcode,
        'resolutioncode': resolutioncode,
        'year': dd.year,
        'month': dd.month,
        'day': dd.day,
        'DayAheadTotalLoadForecastValue': sum
        })
        if temp not in data:
            data.append(temp)
    if data == []:
        return HttpResponse("NO DATA")
    if request.method == 'GET':
        newdata = sorted(data, key=lambda k: k['day'])
        if format == 'json':
            return JsonResponse(newdata,json_dumps_params={'indent': 2},safe = False)
        elif format == 'csv':
            csv_file = "Names.csv"
            csv_columns = ['source','dataset','areaname','areatypecode','mapcode','resolutioncode','year','month','day','datetime','actualtotalloadvalue','updatetime']
            with open(csv_file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for d in newdata:
                    writer.writerow(d)
            with open(csv_file) as csvfile:
                response = HttpResponse(csvfile,content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename = "Dayaheadtotalloadforecast.csv"'
                return response
        else:
            return HttpResponse("Bad request")

def dayaheadtotalloadforecast_detail(request,areaname,resolutioncode,year,format):
    tmp = Resolutioncode.objects.filter(resolutioncodetext = resolutioncode)
    data_to_export = Dayaheadtotalloadforecast.objects.filter(areaname = areaname, resolutioncodeid = tmp[0],year = year, month = month, day = day)
    data = []
    for dd in data_to_export:
        areatypecode = dd.areatypecodeid.areatypecodetext
        mapcode =dd.mapcodeid.mapcodetext
        sum =  Dayaheadtotalloadforecast.objects.filter(areaname = areaname, resolutioncodeid = tmp[0],year = year, month = dd.month,areatypecodeid = dd.areatypecodeid,mapcodeid = dd.mapcodeid).aggregate(Sum('totalloadvalue'))
        temp = ({
        'source': 'entso-e',
        'dataset': 'ActualTotalLoad',
        'areaname': dd.areaname,
        'areatypecode': areatypecode,
        'mapcode': mapcode,
        'resolutioncode': resolutioncode,
        'year': dd.year,
        'month': dd.month,
        'DayAheadTotalLoadForecastValue': sum
        })
        if temp not in data:
            data.append(temp)
    if data == []:
        return HttpResponse("NO DATA")
    if request.method == 'GET':
        newdata = sorted(data, key=lambda k: k['month'])
        if format == 'json':
            return JsonResponse(newdata,json_dumps_params={'indent': 2},safe = False)
        elif format == 'csv':
            csv_file = "Names.csv"
            csv_columns = ['source','dataset','areaname','areatypecode','mapcode','resolutioncode','year','month','day','datetime','actualtotalloadvalue','updatetime']
            with open(csv_file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for d in newdata:
                    writer.writerow(d)
            with open(csv_file) as csvfile:
                response = HttpResponse(csvfile,content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename = "DayAheadTotalLoadForecast.csv"'
                return response
        else:
            return HttpResponse('Bad request')


#Actual Total Load vs Day-Ahead Total Load Forecast

def actualvsforecast_detail2(request,areaname,resolutioncode,year,month,day,format):
    tmp = Resolutioncode.objects.filter(resolutioncodetext = resolutioncode)
    resolutioncodeid = tmp[0].id
    data_to_export = Actualtotalload.objects.filter(areaname = areaname,resolutioncodeid = resolutioncodeid,year=year,month=month,day=day)
    data = []
    for dd in data_to_export:
        areatypecode = dd.areatypecodeid.areatypecodetext
        mapcode = dd.mapcodeid.mapcodetext
        nes = Dayaheadtotalloadforecast.objects.filter(areaname = areaname,resolutioncodeid = resolutioncodeid,mapcodeid = dd.mapcodeid,datetime = dd.datetime,year=year,month=month,day=day)
        data.append({
        'source': 'entso-e',
        'dataset': 'ActualTotalLoad',
        'areaname': dd.areaname,
        'areatypecode': areatypecode,
        'mapcode': mapcode,
        'resolutioncode': resolutioncode,
        'year': dd.year,
        'month': dd.month,
        'day': dd.day,
        'datetime': dd.datetime,
        'DayAheadTotalLoadForecastValue': nes[0].totalloadvalue,
        'actualtotalloadvalue': dd.totalloadvalue,
        'updatetime':dd.updatetime
        })
    if data == []:
        return HttpResponse("NO DATA")
    if request.method == 'GET':
        newdata = sorted(data, key=lambda k: k['datetime'])
        if format == 'json':
            return JsonResponse(newdata,json_dumps_params={'indent': 2},safe = False)
        elif format == 'csv':
            csv_file = "Names.csv"
            csv_columns = ['source','dataset','areaname','areatypecode','mapcode','resolutioncode','year','month','day','datetime','actualtotalloadvalue','updatetime']
            with open(csv_file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for d in newdata:
                    writer.writerow(d)
            with open(csv_file) as csvfile:
                response = HttpResponse(csvfile,content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename = "ActualVsForecast.csv"'
                return response
        else:
            return HttpResponse('Bad rerquest')

def actualvsforecast_detail1(request,areaname,resolutioncode,year,month,format):
    tmp = Resolutioncode.objects.filter(resolutioncodetext = resolutioncode)
    resolutioncodeid = tmp[0].id
    data_to_export = Actualtotalload.objects.filter(areaname = areaname,resolutioncodeid = resolutioncodeid,year=year,month=month)
    data = []
    for dd in data_to_export:
        areatypecode = dd.areatypecodeid.areatypecodetext
        mapcode = dd.mapcodeid.mapcodetext
        sum = Actualtotalload.objects.filter(areaname = areaname,resolutioncodeid = resolutioncodeid,year=year,month=month,day =dd.day,mapcodeid = dd.mapcodeid,areatypecodeid = dd.areatypecodeid).aggregate(Sum('totalloadvalue'))
        nes = Dayaheadtotalloadforecast.objects.filter(areaname = areaname,resolutioncodeid = resolutioncodeid,mapcodeid = dd.mapcodeid,year=year,month=month,day=dd.day,areatypecodeid = dd.areatypecodeid).aggregate(Sum('totalloadvalue'))
        temp = ({
        'source': 'entso-e',
        'dataset': 'ActualTotalLoad',
        'areaname': dd.areaname,
        'areatypecode': areatypecode,
        'mapcode': mapcode,
        'resolutioncode': resolutioncode,
        'year': dd.year,
        'month': dd.month,
        'day': dd.day,
        'DayAheadTotalLoadForecastValue': nes,
        'actualtotalloadvalue': sum
        })
        if temp  not in data:
            data.append(temp)
    if data == []:
        return HttpResponse("NO DATA")
    if request.method == 'GET':
        newdata = sorted(data, key=lambda k: k['day'])
        if format == 'json':
            return JsonResponse(newdata,json_dumps_params={'indent': 2},safe = False)
        elif format == 'csv':
            csv_file = "Names.csv"
            csv_columns = ['source','dataset','areaname','areatypecode','mapcode','resolutioncode','year','month','day','datetime','actualtotalloadvalue','updatetime']
            with open(csv_file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for d in newdata:
                    writer.writerow(d)
            with open(csv_file) as csvfile:
                response = HttpResponse(csvfile,content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename = "ActualVsForecast.csv"'
                return response
        else:
            return HttpResponse("Bad reqquest")

def actualvsforecast_detail(request,areaname,resolutioncode,year,format):
    tmp = Resolutioncode.objects.filter(resolutioncodetext = resolutioncode)
    resolutioncodeid = tmp[0].id
    data_to_export = Actualtotalload.objects.filter(areaname = areaname,resolutioncodeid = resolutioncodeid,year=year)
    data = []
    for dd in data_to_export:
        areatypecode = dd.areatypecodeid.areatypecodetext
        mapcode = dd.mapcodeid.mapcodetext
        sum = Actualtotalload.objects.filter(areaname = areaname,resolutioncodeid = resolutioncodeid,year=year,month=dd.month,mapcodeid = dd.mapcodeid,areatypecodeid = dd.areatypecodeid).aggregate(Sum('totalloadvalue'))
        nes = Dayaheadtotalloadforecast.objects.filter(areaname = areaname,resolutioncodeid = resolutioncodeid,mapcodeid = dd.mapcodeid,year=year,month=dd.month,areatypecodeid = dd.areatypecodeid).aggregate(Sum('totalloadvalue'))
        temp = ({
        'source': 'entso-e',
        'dataset': 'ActualTotalLoad',
        'areaname': dd.areaname,
        'areatypecode': areatypecode,
        'mapcode': mapcode,
        'resolutioncode': resolutioncode,
        'year': dd.year,
        'month': dd.month,
        'DayAheadTotalLoadForecastValue': nes,
        'actualtotalloadvalue': sum
        })
        if temp  not in data:
            data.append(temp)
    if data == []:
        return HttpResponse("NO DATA")
    if request.method == 'GET':
        newdata = sorted(data, key=lambda k: k['month'])
        if format == 'json':
            return JsonResponse(newdata,json_dumps_params={'indent': 2},safe = False)
        elif format == 'csv':
            csv_file = "Names.csv"
            csv_columns = ['source','dataset','areaname','areatypecode','mapcode','resolutioncode','year','month','day','datetime','actualtotalloadvalue','updatetime']
            with open(csv_file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for d in newdata:
                    writer.writerow(d)
            with open(csv_file) as csvfile:
                response = HttpResponse(csvfile,content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename = "ActualTotalLoad.csv"'
                return response
        else:
            return HttpResponse("Bad request")
