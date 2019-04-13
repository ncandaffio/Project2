from flask import Flask, jsonify
import pymongo

#################################################
# Database Setup
#################################################


app = Flask(__name__)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.vacation 
collection = db.accommodations

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
        f"For all data: /data"
        f"To query:/data/'field'/'value'"
        
    )
#################################################
# API PRECIPITATION
#################################################

@app.route("/data")
def data():
    """Display all data from the collection.""" 

    a = []
    for result in collection.find():
        a.append(result.items())
    return jsonify(a)


@app.route("/data/<field>/<query>")
def query():
    """Display data based on user query.""" 

    a = []
    for result in collection.find():
        a.append(result.items({"field":"query"}))
    return jsonify(a)



if __name__ == '__main__':
    app.run(debug=True)