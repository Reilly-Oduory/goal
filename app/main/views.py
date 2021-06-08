from flask import render_template
from . import main
from ..request import get_news

@main.route('/')
def index():
    general_news = get_news('general')
    title = 'Great Britain News Centre'

    return render_template('index.html', title = title, general = general_news)

@main.route('/business')
def business():
    business_news = get_news('business')
    title = 'Great Britain News Centre'

    return render_template('business.html', title = title, business_news = business_news)

@main.route('/ent')
def entertainment():
    ent_news = get_news('entertainment')
    title = 'Great Britain News Centre'

    return render_template('ent.html', title = title, ent_news = ent_news)

@main.route('/health')
def health():
    health_news = get_news('health')
    title = 'Great Britain News Centre'

    return render_template('health.html', title = title, health_news = health_news)

@main.route('/science')
def science():
    science_news = get_news('science')
    title = 'Great Britain News Centre'

    return render_template('science.html', title = title, science_news = science_news)

@main.route('/sports')
def sports():
    sports_news = get_news('sports')
    title = 'Great Britain News Centre'

    return render_template('sports.html', title = title, sports_news = sports_news)

@main.route('/tech')
def technology():
    tech_news = get_news('technology')
    title = 'Great Britain News Centre'

    return render_template('tech.html', title =title, tech_news = tech_news)