from django.http import HttpResponse

def pagina_en_desarrollo(request):
    return HttpResponse("Página en desarrollo")
