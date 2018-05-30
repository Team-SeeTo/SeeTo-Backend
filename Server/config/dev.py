class Config:
    GRAPHIQL = True
    DEBUG = True
    HOST = '0.0.0.0'

    SERVICE_NAME = 'SeeTo_API'

    RUN_SETTING = {
        'host': HOST,
        'port': 5000,
        'debug': DEBUG
    }

    MONGODB_SETTINGS = {
        'db': SERVICE_NAME,
        'host': 'mongomock://localhost'
    }
