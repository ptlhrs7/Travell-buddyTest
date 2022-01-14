#dependencies
import requests
import numpy as np
import datetime as dt
import pandas as pd
import os


import sqlalchemy
from sqlalchemy.ext.automap import automap_base, name_for_collection_relationship
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, render_template, redirect, url_for, request
from flask import Flask, jsonify

import googlemaps
import pprint
import time

from sqlalchemy.sql import functions
from config import g_key


#################################################
# Database Setup
#################################################
#engine = create_engine("sqlite:///travel.sqlite")

# reflect an existing database into a new model
#Base = automap_base()
# reflect the tables
#Base.prepare(engine, reflect=True)

# Save reference to the table
#Passenger = Base.classes.passenger

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################



# WEB ROUTES
'''
@app.route("/",methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        location = request.form
        print(location)
    print("Server accessed to the Home route")
    return render_template("index.html")
'''
'''

@app.route("/results",methods=['GET', 'POST'])
def searchresults():
    if request.method == 'POST':
        form = request.form
        return form
    else:
        return "something"
'''

# accessing a different route
@app.route("/Hotels")
def popular():
    print("Server accessed to the Popular route")
    return("Popular Hotels")



@app.route("/Gyms")
def workout():
    print("Server accessed to the Popular route")
    return("Popular Hotels")


@app.route("/Entertainment")
def party():
    print("Server accessed to the Popular route")
    return("Popular Hotels")

#API ROUTES
#@app.route("api/<lan")
#def get_landmarks():
    #showme = col.find({"landmarks"})
    #showme = dict(showme)
    #return jsonify(showme)

# defining main function

#make requests for updated location, remarks, etc. Create new script


# update database on api calls manually by going to browser
# or schedule to update daily
#@app.route("api/update_db")
#def update_database():
    
    # establish db connection

    # call api
    #url = "provide"
    ###if len(data) > db_entries:
    # add new to database if true


    # pip install googlemaps
# pip install pree\ttyprint


@app.route("/",methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template("index.html")
    elif request.method == 'POST':
        #location = request.form

        loc = 33.7490, -84.3880
        API_KEY = g_key
        gmap = googlemaps.Client(key = API_KEY)
        gym_result = gmap.places_nearby(location = loc, radius = 4000, open_now = False, type = 'gym' )
       # hotel_result = gmap.places_nearby(location = loc, radius = 4000, open_now = False, type = 'hotel' )
       # restaurant_result = gmap.places_nearby(location = loc, radius = 4000, open_now = False, type = 'restaurant' )
       # entertainment_result = gmap.places_nearby(location = loc, radius = 4000, open_now = False, type = 'entertainment' )
       # attraction_result = gmap.places_nearby(location = loc, radius = 4000, open_now = False, type = 'attraction' )
        for gym in gym_result['results']:

            my_place_id = gym['place_id']

            my_fields = ['icon', 'type', 'rating', 'opening_hours']
            gym_details = gmap.place(place_id = my_place_id, fields = my_fields)
            
            print("Server accessed to the Home route for map", name = gym['name'])
            print(gym_details)
            print(loc)

            return render_template("index.html")

'''
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/get_data", methods=['GET', 'POST'])
def search():
    print("Search route accessed.")
    search_term = request.get_json(force=True)
    print(search_term)

    # Query database for search term.

    return "Server says you searched for: " + str(search_term['search'])

'''

if __name__ == "__main__":
    app.run(debug=True)
    
    
    