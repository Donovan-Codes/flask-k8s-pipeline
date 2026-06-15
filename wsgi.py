# ---------------------------------------------------------------
# Donovan-Codes : Defining Production WSGI Entrypoint for Gunicorn
# ---------------------------------------------------------------

# Donovan-Codes : Importing the Application Factory
from app import create_app

# Donovan-Codes : Exposing the Top-Level `app` Callable That Gunicorn Targets (wsgi:app)
app = create_app()
