# Import the dependencies.


import numpy as np
import pandas as pd
import datetime as dt


#################################################
# Database Setup
#################################################
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect,text
# create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite").connect()

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

Base.classes.keys()


# Save references to each table
station=Base.classes.station
measurement=Base.classes.measurement

# Create our session (link) from Python to the DB
session=Session(engine)

#################################################
# Flask Setup
#################################################

from flask import Flask, jsonify
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

#Precipitatioin route
@app.route("/")
def home():
    return ("Welcome to my 'weather website' page!:<br/>"
            f"Available Routes:<br/>"
            f"/api/v1.0/precipitation <br/>"
            f"/api/v1.0/stations <br/>"
            f"/api/v1.0/tobs <br/> "
            f"/api/v1.0/Start <br/> "
            f"/api/v1.0 start/end <br/>"     
            )


@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    print("Server received request for 'precipitation' page...")
    result= session.query(measurement.date,measurement.prcp).filter(measurement.date>= "2016-08-23").all()
    session.close()
    precipitaion=[]
    for date,prcp in result:
        dict={}
        dict['date']=date
        dict['prcp']=prcp
        precipitaion.append(dict)
    

    return jsonify(precipitaion)



#Station route route
@app.route("/api/v1.0/stations")
def Station():
    session = Session(engine)
    stations_result=session.query(station.station,station.id).all()
    session.close()
    stations=[]
    for st,id in stations_result:
        dict_s={}
        dict_s['station']=st
        dict_s['id']=id
        stations.append(dict_s)
        
   
    return jsonify (stations) 


@app.route("/api/v1.0/tobs")
def tobs():
    print("Server received request for 'USC00519281 station' page...")
    
    session = Session(engine)
    most_active=session.query(measurement.station,func.count(measurement.station)).\
            order_by(func.count(measurement.station).desc()).group_by(measurement.station).first()
    most_active_id=most_active[0]

    data=session.query(measurement.date,measurement.tobs).filter(measurement.station==most_active_id\
                                                and measuremet.date>=date_object).order_by(measurement.date.desc()).all()

    session.close()
    
    print("Server received request for 'precipitation' page...")
    
    most_active_p=[]
    for date,temp in data:
        dict_t={}
        dict_t['date']=date
        dict_t['tobs']=temp
       
        most_active_p.append(dict_t)
    

    return jsonify(most_active_p)


    return ("Welcome to my 'USC00519281 station' page!")


@app.route("/api/v1.0/Start")
def Start():
    session = Session(engine)
    print("Server received request for 'precipitation' page...")
    info=session.query(func.min(measurement.tobs),func.max(measurement.tobs),\
                       func.avg(measurement.tobs)).filter(measurement.date >="2016-01-01").all()

    session.close()
    info_tobs=[]
    for min, max, avg in info:
        tobs_dict = {}
        tobs_dict["min"] = min
        tobs_dict["max"] = max
        tobs_dict["average"] = avg
        info_tobs.append(tobs_dict)
    return jsonify( info_tobs)


@app.route("//api/v1.0 start/end")
def Start_end_date():
    session = Session(engine)


    start_end_date_tobs_results = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).\
        filter(measurement.date >= "2016-08-23").\
        filter(measurement.date <= "2017-08-23").all()

    session.close()
  
    # Create a list of min,max,and average temps that will be appended with dictionary values for min, max, and avg tobs queried above
    start_end_tobs_date_values = []
    for min, max, avg in start_end_date_tobs_results:
        start_end_tobs_date_dict = {}
        start_end_tobs_date_dict["min_temp"] = min      
        start_end_tobs_date_dict["max_temp"] = max
        start_end_tobs_date_dict["avg_temp"] = avg
        start_end_tobs_date_values.append(start_end_tobs_date_dict) 
    

    return jsonify(start_end_tobs_date_values)
    
           




if __name__ == "__main__":
    app.run(debug=True)
