
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
]

# Wrap the multilingual views using i18n_patterns
urlpatterns += i18n_patterns(
    path('', TemplateView.as_view(template_name='page1.html'), name='page1'),
    path('page2/', TemplateView.as_view(template_name='page2.html'), name='page2'),
    path('page3/', TemplateView.as_view(template_name='page3.html'), name='page3'),
    path('set_language/', include('django.conf.urls.i18n')),  # Handles language change
    path('test', TemplateView.as_view(template_name='test.html'), name='test'),

)