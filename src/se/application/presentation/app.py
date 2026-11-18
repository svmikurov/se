from typing import Any

from fastapi import FastAPI

DEBUG = True

PRESENTATION_CARD = {
    'definition': 'Definition text',
    'explanation': 'Explanation text',
}

app = FastAPI(debug=DEBUG)


@app.get('/presentation')
def presentation() -> dict[str, Any]:
    return {'presentation': PRESENTATION_CARD}
