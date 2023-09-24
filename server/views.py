from django.http import HttpResponse

def getData(request):
    return HttpResponse("hello")