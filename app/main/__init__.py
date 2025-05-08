# app/main/__init__.py

from flask import Blueprint

# Create a Blueprint instance named 'main'
bp = Blueprint('main', __name__)

# Import routes so they're registered with the blueprint
from app.main import routes
