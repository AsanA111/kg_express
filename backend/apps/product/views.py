from django.shortcuts import render
from .models import SubCategory
from django.shortcuts import render
from django.http import  HttpResponse
from django.views.generic import TemplateView
import json

# Create your views here.
def get_subcategory(request):
    id = request.GET.get('id', '')
    result = list(SubCategory.objects.filter(
    category_id=int(id)).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type="application/json")

class IndexPage(TemplateView):
    template_name = "index.html"