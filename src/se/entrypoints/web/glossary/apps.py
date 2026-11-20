from django.apps import AppConfig

from se.entrypoints.web.glossary import views as glossary_views

from .. import container


class GlossaryConfig(AppConfig):
    name = 'se.entrypoints.web.glossary'

    def ready(self) -> None:
        container.wire(
            modules=[
                glossary_views,
            ]
        )
