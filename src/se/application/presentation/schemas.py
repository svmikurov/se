from pydantic import BaseModel

from se.domain.values import PresentationCard


class PresentationSchema(BaseModel):
    presentation: PresentationCard
