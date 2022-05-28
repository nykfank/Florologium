#!/usr/bin/python3
# Returns seconds of exposure for bulb mode or 0 for automatic.
transition_seconds = 60 * 90
max_exposure_seconds = 60
import astral, astral.sun, datetime
# Location of Botanical Gardens Bern and its local timezone.
loc = astral.LocationInfo(timezone='Europe/Zurich', latitude=46.95263, longitude=7.44545)
s = astral.sun.sun(loc.observer, tzinfo=loc.timezone)
dusk = s["dusk"] + datetime.timedelta(minutes=5)
dawn = s["dawn"] - datetime.timedelta(minutes=5)
current_time = datetime.datetime.now().astimezone()
delta = 0
if current_time < dawn: delta = (dawn - current_time).seconds
if current_time > dusk: delta = (current_time - dusk).seconds
exposure = max_exposure_seconds * delta / transition_seconds
if exposure > 25: exposure = 25
if exposure > 0 and exposure < 5: exposure = 5
print(int(exposure))
