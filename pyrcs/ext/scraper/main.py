from flask import Blueprint, request
from bs4 import BeautifulSoup
import requests


bp = Blueprint("scraper", __name__)

def init_lyrics_app(bp):
    @bp.route("/search", methods=['POST'])
    def search():
        response = request.get_json()
        return response["artist"]

