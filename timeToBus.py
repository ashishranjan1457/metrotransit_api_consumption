#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import requests 
import os
import json
import sys

def findBusRoute ( bus_route ):
	url = "http://svc.metrotransit.org/NexTrip/Routes?format=json"

	busRouteJson = callApi( url )

	for a, b, c in busRouteJson.items():
		#if (i['Description'].find(bus_route)) > 0:
			print(a.value + "'" + b + "'" + c)

def callApi ( url ):
	try:
		r = requests.get( url )
	except requests.exceptions.RequestException as e:
		print(e)
		sys.exit( 1 )
	return json.loads(r.text)

def main():
	bus_route = sys.argv[1]
	bus_stop = sys.argv[2]
	direction = sys.argv[3]
	print(bus_route + " " + bus_stop + " " + direction)
	findBusRoute ( bus_route )


if __name__ == "__main__":
	main()
