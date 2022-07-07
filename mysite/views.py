#in the name of God
from django.http import HttpResponse
from django.http import JsonResponse
def http_test(request):
    return HttpResponse('<h1>http_request<h1>')  #this is html code

def json_test(request):
    return JsonResponse({'name':"ali"})
