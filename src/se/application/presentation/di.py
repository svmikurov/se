"""Dependency injection container."""

from dependency_injector import containers, providers

from se.domain.models import PresentationDomain
from se.infrastructure.repositories import InMemoryTermRepository

from .use_cases import PresentationUseCase


# HACK: Replace in-memory repository
class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=['.routes'])

    domain = providers.Factory(PresentationDomain)

    in_memory_repository = providers.Factory(InMemoryTermRepository)

    use_case = providers.Factory(
        PresentationUseCase,
        domain=domain,
        repo=in_memory_repository,
    )
