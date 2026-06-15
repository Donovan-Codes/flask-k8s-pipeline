# ---------------------------------------------------------------
# Donovan-Codes : Defining Flask Application Factory
# ---------------------------------------------------------------

# Donovan-Codes : Importing Flask Core and Prometheus Metrics Exporter
from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics


# Donovan-Codes : Building a Fresh Flask App Instance for Prod and Test Use
def create_app():
    # Donovan-Codes : Instantiating the Flask Application Object
    app = Flask(__name__)

    # Donovan-Codes : Attaching Prometheus Metrics to Auto-Instrument Routes at /metrics
    PrometheusMetrics(app)

    # Donovan-Codes : Importing and Registering Routes After App Creation to Avoid Circular Imports
    from app.routes import register_routes
    register_routes(app)

    return app
