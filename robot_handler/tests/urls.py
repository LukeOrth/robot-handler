from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('<int:test_suite_id>/', views.detail, name='detail'),
        path('<int:test_suite_id>/results/', views.results, name='results'),
        path('<int:test_suite_id>/run/', views.run, name='run'),
]
