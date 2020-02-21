'''
def actualtotalload_detail(request,year,month,day):
    #tmp = Resolutioncode.objects.filter(resolutioncodetext = resolutioncode)
    resolutioncodeid = tmp.ResolutionCode.resolutioncodetext
    data_to_export = Actualtotalload.objects.filter(year=year,month=month,day=day)
    data = []
    for dd in data_to_export:
        data.append( {
        'year': dd.Actualtotalload.year,
        'month': dd.Actualtotalload.month,
        'day': dd.Actualtotalload.day
        })
        if request.method == 'GET':
            serializer = ActualtotalloadSerializer(data, many=True)
            return JsonResponse(serializer.data,safe=False)
'''

'''
def actualtotalload_detail(request,areaname,resolutioncode,year,month,day):
    try:
        actualtotalload = Actualtotalload.objects.filter(areanmae=areaname,resolutioncode=resolutioncode,year=year,month=month,day=day)
    except  Actualtotalload.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ActualtotalloadSerializer(actualtotalload)
        return JsonResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ActualtotalloadSerializer(actualtotalload,data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=400)

    elif request.method == 'DELETE':
        actualtotalload.delete()
        return HttpResponse(status=204)

'''
'''
'''
def actualtotalload_detail(request,areaname,resolutioncode,year,month):
    try:
        actualtotalload = User.objects.filter(areanmae=areaname,resolutioncodeid=resolutioncodeid,year=year,month=month)
    except  Actualtotalload.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ActualtotalloadSerializer(actualtotalload)
        return JsonResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ActualtotalloadSerializer(actualtotalload,data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=400)

    elif request.method == 'DELETE':
        actualtotalload.delete()
        return HttpResponse(status=204)


def actualtotalload_detail(request,areaname,resolutioncode,year):
    try:
        actualtotalload = User.objects.filter(areanmae=areaname,resolutioncodeid=resolutioncodeid,year=year)
    except  Actualtotalload.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ActualtotalloadSerializer(actualtotalload)
        return JsonResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ActualtotalloadSerializer(actualtotalload,data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=400)

    elif request.method == 'DELETE':
        actualtotalload.delete()
        return HttpResponse(status=204)
'''

'''
