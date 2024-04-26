import os 
from flask import Flask, render_template

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        #Load the instance config, if it exists, when not testing.
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    #Ensure the instace folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/")
    def index():
        return render_template("index.html")
    
    @app.route("/credible")
    def about():
        return render_template("credible.html")
    
    @app.route("/fake")
    def palindrome():
        return render_template("fake.html")
    
    return app

app = create_app()