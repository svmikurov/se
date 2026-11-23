"""Dependency injection container."""

from dependency_injector import containers, providers

from se.domain import PresentationDomain

from .use_cases import PresentationUseCase


class RepoStub: ...


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=['.routes'])

    domain = providers.Factory(PresentationDomain)

    # FIXME: Add repositories to DI factory
    terms_repository = providers.Factory(RepoStub)
    term_repository = providers.Factory(RepoStub)

    use_case = providers.Factory(
        PresentationUseCase,
        domain=domain,
        terms_repository=terms_repository,
        term_repository=term_repository,
    )
