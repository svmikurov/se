"""Dependency injection container."""

from dependency_injector import containers, providers

from se.domain.models import PresentationDomain

from .use_cases import PresentationUseCase


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=['.routes'])

    domain = providers.Factory(PresentationDomain)

    use_case = providers.Factory(
        PresentationUseCase,
        domain=domain,
    )
