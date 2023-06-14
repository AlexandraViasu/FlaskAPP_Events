from models.event import *
import datetime


event1 = Events("New Years Eve" , datetime.date(2023, 12, 31) , 1000 , "B14" , "Celebrating The New Year" ,True)
event2 = Events("Easter Eve" , None , 200 , "Church" , "Celebrating Easter Eve" , False)
events = [event1 , event2]


def remove_event(event):
    events.remove(event)

def add_new_event(task):
    events.append(task)