from flask import Flask
from ceevee_backend import app_create



app = app_create()
# app.app_context().push()

""" @app.route("/hello/", strict_slashes=False)
def hello():
    """Just a hello"""

    return "Hello"
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
