# ===============================================================
# Donovan-Codes : Defining Multi-Stage Docker Build for Flask Service
# ===============================================================

# ---------------------------------------------------------------
# Donovan-Codes : Stage 1 — Builder (Installs Dependencies, Discarded After Build)
# ---------------------------------------------------------------
# Donovan-Codes : Basing the Builder Stage on Slim Python 3.12
FROM python:3.12-slim AS builder

# Donovan-Codes : Setting the Working Directory for the Build Stage
WORKDIR /app

# Donovan-Codes : Copying Requirements First to Leverage Docker Layer Caching
COPY requirements.txt .

# Donovan-Codes : Installing Dependencies Into an Isolated /install Prefix for Clean Hand-Off
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# ---------------------------------------------------------------
# Donovan-Codes : Stage 2 — Runtime (Final Slim Image That Ships)
# ---------------------------------------------------------------
# Donovan-Codes : Starting Fresh From Slim Python 3.12 With No Build Tooling
FROM python:3.12-slim

# Donovan-Codes : Setting the Working Directory for the Runtime Stage
WORKDIR /app

# Donovan-Codes : Creating a Non-Root User to Shrink the Container Blast Radius
RUN useradd --create-home appuser

# Donovan-Codes : Copying Installed Packages Forward From the Builder Stage
COPY --from=builder /install /usr/local

# Donovan-Codes : Copying Application Code and the WSGI Entrypoint Into the Image
COPY app/ ./app/
COPY wsgi.py .

# Donovan-Codes : Dropping to the Non-Root User for All Subsequent Operations
USER appuser

# Donovan-Codes : Documenting the Port Gunicorn Listens On (Informational Only)
EXPOSE 8000

# Donovan-Codes : Launching Gunicorn With Two Workers Bound to All Interfaces on Port 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "wsgi:app"]
