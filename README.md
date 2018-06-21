# lufthansa-fapi

## what?
this script is a proof-of-concept of what can be done with information provided onboard a **FlyNet-equipped** Lufthansa flight.

## how?
Lufthansa provides a _paid_ onboard internet service through an open Wi-Fi access point aboard some of their flights.
This Wi-Fi access point is always available; however, true internet access is only available above a certain altitude (a 3 hour flight will only have under 2 hours' worth of internet availability due to taxi, takeoff, approach, and landing).
Lufthansa provides some information on their access gateway such as the flight destination, estimated remaining flight time, and some more touristy information.
Interestingly enough, when inspecting network requests on said gateway, a certain resource was being refreshed quite often, although it was not exposed to the user via the page.
This resource turns out to be a `.json` file with a bunch of useful properties, including:
- Flight number
- Longitude
- Latitude
- Heading
- Ground speed
- Altitude
- Distance to destination
- _a few other bits_

## what's next?
First thoughts would be to place the flight on a world map, giving more interactivity than overhead screens.
