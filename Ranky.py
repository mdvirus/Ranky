# Importing necessary modules
from flask import Flask

#import all the blueprints
from routes.api import api
from routes.frontend import frontend

# Starting of main framework
app = Flask(__name__)

#Register all the blueprints
app.register_blueprint(api);
app.register_blueprint(frontend)

#This route returns the data in json format like what an api would do

if __name__ == '__main__':
	app.run(debug = True)