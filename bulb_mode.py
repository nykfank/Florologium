#!/usr/bin/python3
# Returns auto when the sun is up and bulb when it is down.
import astral, astral.sun, datetime
loc = astral.LocationInfo(timezone='Europe/Zurich', latitude=46.94809, longitude=7.44744)
s = astral.sun.sun(loc.observer, tzinfo=loc.timezone)
current_time = datetime.datetime.now().time()
dawn_time = s["dawn"].time()
dusk_time = s["dusk"].time()
mode = 0
if current_time < dawn_time or current_time > dusk_time: mode = 1
print(mode)
