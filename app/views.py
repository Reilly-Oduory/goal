from flask import render_template
from app import app
from .request import get_news

@app.route('/')
def index():
    general_news = get_news('general')
    title = 'Great Britain News Centre'

    return render_template('index.html', title = title, general = general_news)
