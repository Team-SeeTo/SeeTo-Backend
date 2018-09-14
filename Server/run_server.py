from app import create_app
from config.production import ProdConfig

app = create_app(ProdConfig)

if __name__ == "__main__":

    app.run(**ProdConfig.RUN_SETTING)