import time
import requests

while True:
    r = requests.request('GET', 'http://ww2.lufthansa-flynet.com/fapi/flightData')
    j = r.json()

    distDest = float(j['distDest'])
    heading = float(j['heading'])
    gs = int(j['groundSpeed'])
    alt = int(j['altitude'])
    
    print("DIST: %3.1f ; HEAD: %3.1f ; GS: %3d ; ALT: %5d" % (distDest, heading, gs, alt))
    
    time.sleep(5)
