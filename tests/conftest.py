import os

# Required at import time by presentation api until URL
# is moved to Settings (see FIXME in api_client/presentation.py)
os.environ.setdefault('PRESENTATION_SERVICE_URL', 'http://presentation:8000')
