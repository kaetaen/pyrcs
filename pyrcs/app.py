from flask import Flask
from pyrcs.ext.scraper.main import init_lyrics_app

def create_app():
    app = Flask(__name__)
    init_lyrics_app(app)
    return app
