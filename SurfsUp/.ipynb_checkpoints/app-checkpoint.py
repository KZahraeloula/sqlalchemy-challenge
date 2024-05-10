# Import the dependencies.



#################################################
# Database Setup
#################################################


# reflect an existing database into a new model

# reflect the tables


# Save references to each table


# Create our session (link) from Python to the DB


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
            f"api/v1.0/tobs "
                 
            )


@app.route("api/v1.0/precipitation")
def precipitation():
    print("Server received request for 'precipitation' page...")
    return ("Welcome to my 'precipitation' page!")



#Station route route
@app.route("api/v1.0/stations")
def Station():
    print("Server received request for 'Station' page...")
    return ("Welcome to my 'station' page!")


@app.route("api/v1.0/tobs")
def tobs():
    print("Server received request for 'USC00519281 station' page...")
    return ("Welcome to my 'USC00519281 station' page!")


if __name__ == "__main__":
    app.run(debug=True)
