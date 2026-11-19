from dataclasses import asdict
from typing import Any

from fastapi import FastAPI

from se.domain.models import PresentationDomain
from se.domain.values import PresentationCard

from .use_cases import PresentationUseCase

DEBUG = True

app = FastAPI(debug=DEBUG)


@app.get('/presentation', response_model=PresentationCard)
def presentation() -> dict[str, Any]:
    domain = PresentationDomain()
    use_case = PresentationUseCase(domain=domain)
    card = use_case.handle()
    return {'presentation': asdict(card)}  # type: ignore[call-overload]
