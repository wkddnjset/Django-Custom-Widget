from django.shortcuts import render
from django.http import JsonResponse
from .models import Country

# Create your views here.

def country_list(request):
    qs= Country.objects.all()
    q = request.GET.get('q', '')
    print(q)
    qs = qs.filter(name__icontains=q)
    results = [{ 'id':country.id, 'text':country.name } for country in qs]
    print(qs)
    return JsonResponse({
        'results':results,
    })