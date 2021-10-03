from flask import Blueprint

bp = Blueprint("scraper", __name__)

def init_lyrics_app(bp):
    @bp.route("/lyrics")
    def index():
        return "lyrics"
