class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'


class TestConfig(Config):
    TESTING = True


class DevelopmentConfig(Config):
    DEBUG = True
