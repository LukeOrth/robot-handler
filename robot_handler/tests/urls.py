from django.urls import path, include

from . import views

app_name = 'tests'
urlpatterns = [
        path('', views.index, name='index'),
        path('vue_test/', views.vue_test, name='vue_test'),
        path('refresh/', views.refresh_tests, name='refresh_tests'),
        path('<int:test_suite_id>/', views.test_suite, name='test_suite'),
        path('<int:test_suite_id>/results/', views.test_suite_results, name='test_suite_results'),
        path('<int:test_suite_id>/run/', views.test_suite_run, name='test_suite_run'),
        path('<int:test_suite_id>/<int:test_case_id>/', views.test_case, name='test_case'),
        path('<int:test_suite_id>/<int:test_case_id>/results/', views.test_case_results, name='test_case_results'),
        path('<int:test_suite_id>/<int:test_case_id>/run/', views.test_case_run, name='test_case_run'),

        path('api/', views.apiOverview, name="api-overview"),
        path('api/v1/test-suites/', views.testSuitesList, name='test-suites'),
        path('api/v1/test-suites/<str:pk>/', views.testSuite, name='test-suite'),
        path('api/v1/test-cases/', views.testCasesList, name='test-cases'),
        path('api/v1/test-cases/<str:pk>', views.testCase, name='test-case'),
]
