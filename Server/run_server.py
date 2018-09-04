from app import create_app
from config.dev import Config

app = create_app(Config)

if __name__ == "__main__":

    app.run(**Config.RUN_SETTING)