import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'eine_geheime_zufällige_zeichenkette'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # Beispiel für SQLite-Datenbank
    SQLALCHEMY_TRACK_MODIFICATIONS = False
