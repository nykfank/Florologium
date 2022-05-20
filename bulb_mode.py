#!/usr/bin/python3
# Returns seconds of exposure for bulb mode or 0 for automatic.
transition_seconds = 60 * 60
max_exposure_seconds = 30
import astral, astral.sun, datetime
# Set location of Botanical Gardens Bern and its local timezone.
loc = astral.LocationInfo(timezone='Europe/Zurich', latitude=46.95263, longitude=7.44545)
# Get sun data for this location/timezone.
s = astral.sun.sun(loc.observer, tzinfo=loc.timezone)
current_time = datetime.datetime.now().astimezone()
delta = 0
if current_time < s["dawn"]: delta = (s["dawn"] - current_time).seconds
if current_time > s["dusk"]: delta = (current_time - s["dusk"]).seconds
exposure = max_exposure_seconds * delta / transition_seconds
if exposure > 30: exposure = 30
if exposure < 0: exposure = 0
if exposure > 0 and exposure < 3: exposure = 3
print(int(exposure))
