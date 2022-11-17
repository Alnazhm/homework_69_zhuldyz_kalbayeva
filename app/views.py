from django.http import JsonResponse
import json
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


def add_view(request, *args, **kwargs):
    answer = {}
    if request.body:
        numbers = json.loads(request.body)
        try:
            a = float(numbers['A'])
            b = float(numbers['B'])
            response = a + b
            answer['response'] = response
        except ValueError:
            answer['error'] = ''
            return JsonResponse(answer, status=400)
    return JsonResponse(answer)

def substract_view(request, *args, **kwargs):
    answer = {}
    if request.body:
        numbers = json.loads(request.body)
        try:
            a = float(numbers['A'])
            b = float(numbers['B'])
            response = a - b
        except ValueError:
            answer['error'] = 'Try only numbers please'
            return JsonResponse(answer, status=400)
    answer['response'] = response
    return JsonResponse(answer)


def multiply_view(request, *args, **kwargs):
    answer = {}
    if request.body:
        numbers = json.loads(request.body)
        try:
            a = float(numbers['A'])
            b = float(numbers['B'])
            response = a * b
        except ValueError:
            answer['error'] = 'Try only numbers please'
            return JsonResponse(answer, status=400)
    answer['response'] = response
    return JsonResponse(answer)


def divide_view(request, *args, **kwargs):
    answer = {}
    if request.body:
        numbers = json.loads(request.body)
        try:
            a = float(numbers['A'])
            b = float(numbers['B'])
            response = a / b
            answer['response'] = response
            return JsonResponse(answer)
        except ZeroDivisionError:
            answer['error'] = "Division by zero!"
            return JsonResponse(answer, status=400)
        except ValueError:
            answer['error'] = 'Try only numbers please'



