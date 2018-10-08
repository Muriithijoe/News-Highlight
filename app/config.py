class Config:
    NEWS_API_BASE_URL = 'https://newapi.org/v2/sources?&api_api_key{}'

class ProdConfig(Config):
    pass

class DevConfig(Config):

    DEBUG = True
