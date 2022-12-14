from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path, include, re_path
from django.views.generic.base import RedirectView

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

        path('api/', views.ApiOverview.as_view(), name="api-overview"),
        path('api/v1/test-suites/', views.TestSuites.as_view(), name='test-suites'),
        path('api/v1/test-suites/<str:id>', views.TestSuites.as_view(), name='test-suite'),
        path('api/v1/test-cases/', views.TestCases.as_view(), name='test-cases'),
        path('api/v1/test-cases/<str:id>', views.TestCases.as_view(), name='test-case'),
        path('api/v1/tags/', views.Tags.as_view(), name='tags'),
        path('api/v1/tags/<str:name>', views.Tags.as_view(), name='tag'),
        path('api/v1/settings/', views.Settings.as_view(), name='settings'),
        path('api/v1/update-tests/', views.UpdateTests.as_view(), name='update-tests'),
        re_path(r'^api.*$', views.ServiceUnavailable, name='error'),

        path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url("tests/images/robotframework.svg"))),

        re_path(r'^.*$', views.index, name='home'),
]
