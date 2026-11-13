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