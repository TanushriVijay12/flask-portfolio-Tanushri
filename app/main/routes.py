# app/main/routes.py

from flask import render_template
from app.main import bp

# Homepage
@bp.route('/')
def home():
    return render_template('main/home.html')

# About Page
@bp.route('/about')
def about():
    return render_template('main/about.html')

# Projects Page
@bp.route('/projects')
def projects():
    # Placeholder for project data
    project_list = [
        {"title": "Flask Blog", "description": "A blog built with Flask"},
        {"title": "Data Dashboard", "description": "Dashboard using Plotly and Flask"},
    ]
    return render_template('main/projects.html', projects=project_list)
