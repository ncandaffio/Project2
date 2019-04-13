import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///resources/db4.sqlite") #
Base = automap_base()
Base.prepare(engine, reflect=True)

Airbnb = Base.classes.airbnb
session = Session(engine)

app = Flask(__name__)


#################################################
# Flask Routes
#################################################

#################################################
# API ROUTES
#################################################

@app.route("/")
def Home():
    """List all available api routes."""
    return (
        f"Welcome to the API!<br/><br/>"
        f"Available Routes:<br/>"
        f"Date range available: 2010-01-01 to 2017-08-23<br/><br/>"
        f"Precipitation information from last year<br/>"
        f"/api/v1.0/precipitation <br/><br/>"
        f"Available Stations<br/>"
        f"/api/v1.0/stations <br/><br/>" 
        f"Temperature information from last year<br/>" 
        f"/api/v1.0/tobs <br/><br/>"
        f"Enter a start date in yyyy-mm-dd format to obtain temperature min,max,avg:<br/>"
        f"/api/v1.0/<start> <br/><br/>"
        f"Enter a start/end date in yyyy-mm-dd format to obtain temperature min,max,avg:<br/>"
        f"/api/v1.0/<start>/<end> <br/>"
    )
#################################################
# API PRECIPITATION
#################################################

@app.route("/airbnbdata")
def data():
    """List all available api routes."""
    total = session.query(Airbnb.City,Airbnb.Ratings) #.order_by(Measurement.date)
    
    datab = []
    for result in total:
        data_dict = {}
        data_dict["City"] = result.City
        data_dict["Ratings"] = result.Ratings
        datab.append(data_dict)

    return jsonify(datab)


if __name__ == '_main_':
    app.run(debug=True)