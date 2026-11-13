"""URL configuration for config project."""

from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # set_language view
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('glossary/', include('glossary.urls'), name='glossary'),
    prefix_default_language=True,   # /en/ and /ru/ (else False — / and /ru/))
)
