from flask import Flask

APP = Flask(__name__)


@APP.get("/")


def index():
    return "<h1>Lucas Antonio Pelanda</h1>"

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=80)

    
