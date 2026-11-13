==========================================
WEB entrypoint Django project localization 
==========================================

settings.py
===========

.. code-block:: python

   from django.utils.translation import gettext_lazy as _

   # Языки, которые поддерживает проект
   LANGUAGES = [
       ('en', _('English')),
       ('ru', _('Russian')),
   ]

   # Язык по умолчанию (если не определён из запроса)
   LANGUAGE_CODE = 'en'

   # Где лежат переводы
   LOCALE_PATHS = [
       BASE_DIR / 'locale',
   ]

   # Включаем i18n/l10n
   USE_I18N = True          # переводы строк
   USE_L10N = True          # форматирование дат/чисел (в Django 4+ всегда True, можно не указывать)
   USE_TZ = True            # хранение в UTC
   TIME_ZONE = 'UTC'        # серверный TZ; для отображения — per-request

   # Middleware (порядок важен)
   MIDDLEWARE = [
       ...
       'django.middleware.locale.LocaleMiddleware',   # после SessionMiddleware, перед CommonMiddleware
       ...
   ]


urls.py
=======

.. code-block:: python

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


code.py
=======

.. code-block:: python


   from django.utils.translation import gettext as _
   from django.utils.translation import gettext_lazy as _lazy

   # In functions/views — gettext
   def my_view(request):
       message = _("Hello, world")
       return HttpResponse(message)

   # In models/forms/settings — gettext_lazy
   class Tag(models.Model):
       name = models.CharField(
           max_length=70,
           verbose_name=_lazy('Name'),
       )


templates
=========

.. code-block::

   {% load i18n %}

   <h1>{% translate "Glossary" %}</h1>


Install gettext
===============


Генерация .po-файлов
====================