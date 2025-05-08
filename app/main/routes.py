# app/main/routes.py

from flask import render_template, flash, redirect, url_for
from app.main import bp
from app.forms import ContactForm
from app.github_service import fetch_github_repos

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
    projects = fetch_github_repos()
    tags = sorted(set([p['language'] for p in projects]))
    
    return render_template('main/projects.html', projects=projects, tags= tags)

@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # You can add logic here to send an email or save message
        flash('Thank you for your message!', 'success')
        return redirect(url_for('main.contact'))
    return render_template('main/contact.html', form=form)