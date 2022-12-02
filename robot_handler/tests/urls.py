from django.urls import path

from . import views

app_name = 'tests'
urlpatterns = [
        path('', views.index, name='index'),
        path('<int:test_suite_id>/', views.test_suite, name='test_suite'),
        path('<int:test_suite_id>/results/', views.results, name='results'),
        path('<int:test_suite_id>/run/', views.run, name='run'),
        path('<int:test_suite_id>/<int:test_case_id>/', views.test_case, name='test_case'),
        path('<int:test_suite_id>/<int:test_suite_id>/results/', views.results, name='results'),
        path('<int:test_suite_id>/<int:test_suite_id>/run/', views.run, name='run'),
]
