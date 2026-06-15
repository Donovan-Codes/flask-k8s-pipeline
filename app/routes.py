# ---------------------------------------------------------------
# Donovan-Codes : Defining API Route Registrations
# ---------------------------------------------------------------

# Donovan-Codes : Importing JSON Response Helper from Flask
from flask import jsonify


# Donovan-Codes : Attaching Routes to the Provided App Instance for Test/Prod Separation
def register_routes(app):

    # Donovan-Codes : Exposing Health Endpoint for Kubernetes Liveness and Readiness Probes
    @app.route("/health")
    def health():
        return jsonify(status="healthy"), 200

    # Donovan-Codes : Serving Basic Service Metadata on the Info Endpoint
    @app.route("/api/info")
    def info():
        return jsonify(
            service="flask-k8s-pipeline",
            version="1.0.0",
            message="Running in Kubernetes"
        ), 200
