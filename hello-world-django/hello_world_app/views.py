from django.shortcuts import render
from django.http import JsonResponse

def hello_world(request):
    return JsonResponse({"Message": "Hello World!"})

def hello_world_template(request):
    return render(request, 'hello_world.html')

