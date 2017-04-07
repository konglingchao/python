from django.http import HttpResponse
def welcome(request):
    return HttpResponse("<h2>Welcome Study Python</h2>")

