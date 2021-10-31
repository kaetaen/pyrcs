from flask import Blueprint, request
from bs4 import BeautifulSoup
import requests


bp = Blueprint("scraper", __name__)


def scrap_lyric(artist: str, song: str):
    artist   = artist.lower().strip()
    song     = song.lower().strip()
    base_url = f"https://www.letras.mus.br/{artist}/{song}/traducao.html"

    html_content = requests.get(base_url).content
    soup = BeautifulSoup(html_content)
    original_lyric = len(soup.find_all("div", {"class": "cnt-trad_l"}))


    return {"foo": original_lyric}

def init_lyrics_app(bp):
    @bp.route("/search", methods=['POST'])
    def search():
        req = request.get_json()

        artist = req["artist"]
        song   = req["song"]  

        return scrap_lyric(artist, song)
