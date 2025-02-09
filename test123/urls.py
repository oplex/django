
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import TemplateView
from .views import my_view

urlpatterns = [
    path('admin/', admin.site.urls),
]

# Wrap the multilingual views using i18n_patterns
urlpatterns += i18n_patterns(
    path('', TemplateView.as_view(template_name='test.html'), name='test'),
    path('set_language/', include('django.conf.urls.i18n')),  # Handles language change

)

