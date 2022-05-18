#!/usr/bin/python3
# Returns 1 after dusk and before dawn, otherwise 0.
import astral, astral.sun, datetime
loc = astral.LocationInfo(timezone='Europe/Zurich', latitude=46.95263, longitude=7.44545)
s = astral.sun.sun(loc.observer, tzinfo=loc.timezone)
current_time = datetime.datetime.now().time()
shift = datetime.timedelta(minutes=20)
dawn_time = (s["dawn"] - shift).time()
dusk_time = (s["dusk"] + shift).time()
mode = 1 if current_time < dawn_time or current_time > dusk_time else 0
print(mode)
