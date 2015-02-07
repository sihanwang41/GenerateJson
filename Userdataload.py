import json
from pprint import pprint

def load_simple_user():
        with open('user.json') as data_file:
                data = json.load(data_file)
	pprint(data)
	print(data["Sihan"])
        return

if __name__ == '__main__':
	load_simple_user()


