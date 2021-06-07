from logging import DEBUG


class Config:
     NEWS_API_TOP_BASE_URL = 'https://newsapi.org/v2/top-headlines/?country=gb&category={}&apiKey={}'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True