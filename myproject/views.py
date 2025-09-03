from django.http import HttpResponse

def handler404(request,exception):
    return HttpResponse("<h1 style='color:red'>Dear User, the page you are looking for does not exist</h1>",status=404) 
