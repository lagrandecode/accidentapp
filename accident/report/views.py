from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .serializer import ReportSerializer
from .models import Report

# Create your views here.

@api_view(['GET','POST'])
def report_list(request):
    if request.method == 'GET':
        report = Report.objects.all()
        serializer = ReportSerializer(report,many=True)
        return Response(serializer.data)
    

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ReportSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def report_detail(request,pk):
    try:
        report = Report.objects.get(id=pk)
    except Report.DoesNotExist:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
    if request.method =='GET':
        serializer = ReportSerializer(report)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ReportSerializer(report,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        report.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

