#!/bin/sh

python /src/ping.py ${USERNAME}
livestreamer -O "http://twitch.tv/${USERNAME}" worst > /dev/null
