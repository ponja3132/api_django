from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Cake

@csrf_exempt
def get_patients(request):
    qs_json = serializers.serialize('json', Cake.objects.all())
    return HttpResponse(qs_json, content_type='application/json')
