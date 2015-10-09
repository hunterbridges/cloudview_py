import requests
import json
import sys
import urllib

username = sys.argv[1]

try:
    # Grab JSON from twitch api for user
    url = "https://api.twitch.tv/kraken/users/%s" % username
    print "Grabbing user json from: %s" % url
    r = requests.get(url)
    if r.status_code != 200:
        raise "Couldn't get user JSON!"

    d = r.json()
    uid = d['_id']

    # Pack the ping data
    print "Packing ping data..."
    pingdata = {
        "type": "channel",
        "id": uid
    }
    pingjson = json.dumps(pingdata, separators=(',', ':'))
    querystr = urllib.urlencode({"u": pingjson})

    # Do the ping
    pingurl = "http://countess.twitch.tv/ping.gif?%s" % querystr
    print "Requesting ping pixel: %s" % pingurl
    r = requests.get(pingurl)
    if r.status_code != 200:
        raise "Couldn't get ping pixel!"

    print "Ping complete!"

except Exception as e:
    print "Ping failed! ERROR: %s" % e.value
