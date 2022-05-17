#!/usr/bin/python3
# Returns 1 after dusk and before dawn, otherwise 1.
import astral, astral.sun, datetime
loc = astral.LocationInfo(timezone='Europe/Zurich', latitude=46.95263, longitude=7.44545)
s = astral.sun.sun(loc.observer, tzinfo=loc.timezone)
current_time = datetime.datetime.now().time()
dawn_time = s["dawn"].time()
dusk_time = s["dusk"].time()
mode = 1 if current_time < dawn_time or current_time > dusk_time else 0
print(mode)
