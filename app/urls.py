from django.urls import path
from app.views import add_view, substract_view, multiply_view, divide_view, IndexView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('add/', add_view, name='add'),
    path('substract/', substract_view, name='substract'),
    path('multiply/', multiply_view, name='multiply'),
    path('divide/', divide_view, name="divide"),
    path('', IndexView.as_view(), name='index')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)