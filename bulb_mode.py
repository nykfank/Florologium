#!/usr/bin/python3
# Returns seconds of exposure for bulb mode or 0 for automatic.
import astral, astral.sun, datetime
loc = astral.LocationInfo(timezone='Europe/Zurich', latitude=46.95263, longitude=7.44545)
s = astral.sun.sun(loc.observer, tzinfo=loc.timezone)
current_time = datetime.datetime.now().time()
shift1 = datetime.timedelta(minutes=15)
shift2 = datetime.timedelta(minutes=30)
shift3 = datetime.timedelta(minutes=45)
dawn_time1 = s["dawn"].time()
dusk_time1 = s["dusk"].time()
dawn_time2 = (s["dawn"] - shift1).time()
dusk_time2 = (s["dusk"] + shift1).time()
dawn_time3 = (s["dawn"] - shift2).time()
dusk_time3 = (s["dusk"] + shift2).time()
dawn_time4 = (s["dawn"] - shift3).time()
dusk_time4 = (s["dusk"] + shift3).time()
exposure = 0
if current_time < dawn_time1 or current_time > dusk_time1: exposure = 5
if current_time < dawn_time2 or current_time > dusk_time2: exposure = 10
if current_time < dawn_time3 or current_time > dusk_time3: exposure = 20
if current_time < dawn_time4 or current_time > dusk_time4: exposure = 30
print(exposure)


