import os

class Config:
    """Main configurations class"""
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://yvette:yvette@localhost/blog'
    SECRET_KEY='ac7d66d2'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://yvette:yvette@localhost/blog'# os.environ.get("DATABASE_URL")

    SECRET_KEY = "try harder" #os.environ.get("SECRET_KEY")
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    QUOTES_URL = 'http://quotes.stormconsultancy.co.uk/random.json'



class ProdConfig(Config):
    """Production configuration class that inherits from the main configurations class"""
    # os.environ.get("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    """Configuration class for development stage of the app"""

    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://yvette:yvette@localhost/blog'# os.environ.get("DATABASE_URL")

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
    #'test':TestConfig
}