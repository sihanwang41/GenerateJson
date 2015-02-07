import json
import datetime
from pprint import pprint

def create_simple_user(info, Name, Friends, Events):
        info[Name] = dict()
        info[Name]["Friends"] = Friends
        info[Name]["Events"] = Events
        return

if __name__ == '__main__':
        info = dict()
        create_simple_user(info, "Sihan", ["Zhou", "Gushan"], ["Devest", "World Cup"])
       	create_simple_user(info, "Gushan", ["Zhou", "Xiwei"], [])
       	create_simple_user(info, "Xiwei", ["Zhou", "Gushan"], ["Devest"])
	create_simple_user(info, "Zhou", ["Sihan", "Gushan"], ["Devest", "World Cup"])
	
        with open("user.json", 'a') as outfile :
                json.dump(info, outfile)


