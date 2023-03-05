from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializer import ReportSerializer
from .models import Report

# Create your views here.

@csrf_exempt
def report_list(request):
    if request.method == 'GET':
        report = Report.objects.all()
        serializer = ReportSerializer(report,many=True)
        return JsonResponse(serializer.data,safe=False)
    

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ReportSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def report_detail(request,pk):
    try:
        report = Report.objects.get(id=pk)
    except Report.DoesNotExist:
        return HttpResponse(status=404)
    if request.method =='GET':
        serializer = ReportSerializer(report)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ReportSerializer(report,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=400)
    elif request.method == 'DELETE':
        report.delete()
        return HttpResponse(status=204)

