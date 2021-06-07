from flask import render_template
from app import app
from .request import get_news

@app.route('/')
def index():
    general_news = get_news('general')
    title = 'Great Britain News Centre'

    return render_template('index.html', title = title, general = general_news)

@app.route('/business')
def business():
    business_news = get_news('business')
    title = 'Great Britain News Centre'

    return render_template('business.html', title = title, business_news = business_news)

@app.route('/ent')
def entertainment():
    ent_news = get_news('entertainment')
    title = 'Great Britain News Centre'

    return render_template('ent.html', title = title, ent_news = ent_news)

@app.route('/health')
def health():
    health_news = get_news('health')
    title = 'Great Britain News Centre'

    return render_template('health.html', title = title, health_news = health_news)

@app.route('/science')
def science():
    science_news = get_news('science')
    title = 'Great Britain News Centre'

    return render_template('science.html', title = title, science_news = science_news)

@app.route('/sports')
def sports():
    sports_news = get_news('sports')
    title = 'Great Britain News Centre'

    return render_template('sports.html', title = title, sports_news = sports_news)

@app.route('/tech')
def technology():
    tech_news = get_news('technology')
    title = 'Great Britain News Centre'

    return render_template('tech.html', title =title, tech_news = tech_news)