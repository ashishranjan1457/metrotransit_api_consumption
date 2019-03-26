import requests
import os
import json
import sys

def findBusRoute ( bus_route_input ):
	url = "http://svc.metrotransit.org/NexTrip/Routes?format=json"

	busRouteJson = callApi( url )
	for i in busRouteJson:
		if (i['Description'].find(bus_route_input)) > 0:
			foundRoute = i['Route']

	return foundRoute

def findStopId ( route_id, bus_stop_input, direction ):
	url = "http://svc.metrotransit.org/NexTrip/Stops" + "/" + str(route_id) + "/" + str(direction) + "?format=json"

	stopIdJson = callApi( url )
	for i in stopIdJson:
		if (i['Text'].find(bus_stop_input)) > 0:
			return i['Value']

def callApi ( url ):
	print("Calling URL: " + url)
	try:
		r = requests.get( url )
	except requests.exceptions.RequestException as e:
		print(e)
		sys.exit( 1 )
	return json.loads(r.text)

def main():
	bus_route_input = sys.argv[1]
	bus_stop_input = sys.argv[2]
	direction_input = sys.argv[3]
	direction = 0
	print(bus_route_input + " " + bus_stop_input + " " + direction_input)

	if direction_input == 'south':
		direction = 1
	elif direction_input == 'east':
		direction = 2
	elif direction_input == 'west':
		direction = 3
	elif direction_input == 'north':
		direction = 4

	#print(bus_route_input + " " + bus_stop_input + " " + direction_input)

	route_id = findBusRoute ( bus_route_input )
	print(route_id)

	stop_id = findStopId ( route_id, bus_stop_input, direction )
	print(stop_id)

if __name__ == "__main__":
	main()
