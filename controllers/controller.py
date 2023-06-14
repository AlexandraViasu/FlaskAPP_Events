from flask import render_template , request , redirect
from app import app
from models.event import *
from models.event_planer import *


@app.route("/events" , methods=["GET"])
def index():
    return render_template("base.html", title="Events", events=events )

@app.route('/events', methods=['POST'])
def add_event():
    event_name = request.form['title']
    event_description = request.form['description']
    event_number_guest = request.form['number_guest']
    event_room_location = request.form['room_location']
    event_recurring = request.form['event_recurring']
    new_event = Events(event_name, event_description, event_number_guest, 
                       event_room_location, event_recurring, False)
    add_new_event(new_event)
    return render_template("base.html", title="Events", events=events )

@app.route("/events/delete/<index>" , methods = ["POST"])
def remove(index):
     removing_event = events[int(index)]
     remove_event(removing_event)
     return redirect("/events")
     
     

     

