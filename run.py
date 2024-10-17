import os

from productcatalogue import create_app
from productcatalogue.config import Config as config

app = create_app()

# for WSGI deployment
application = app

if __name__ == '__main__':

    app.run(
        host=config.HOST,
        port=config.PORT,
        debug=config.DEBUG
    )
