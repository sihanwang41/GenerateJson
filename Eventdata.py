import json
import datetime
from pprint import pprint

def create_simple_event(info, Name, Location, Time, Participant):
        info[Name] = dict()
        info[Name]["Location"] = Location
        info[Name]["Time"] = Time
	info[Name]["Participant"] = Participant
        return

if __name__ == '__main__':
        info = dict()
        create_simple_event(info, "Devest", "Columbia", str(datetime.date(2015, 2, 6)), ["Sihan", "Xiwei", "Zhou"])
       	create_simple_event(info, "World Cup", "North Africa", str(datetime.date(2014, 7, 21)), ["Sihan", "Zhou"])
       	create_simple_event(info, "TI5", "Seattle",  str(datetime.date(2015, 7, 20)), [])
       # create_simple_user(info, "Dota", "ShangHai", ["Zhou", "Gushan"], ["Devest", "Dota", "World Cup"])
       # create_simple_user(info, "Piano", "Paris", ["Zhou", "Gushan"], ["Devest", "Dota", "World Cup"])
        with open("event.json", 'a') as outfile :
                json.dump(info, outfile)

