#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import json
from slackclient import SlackClient

print "> Rioka has started"
token = "SLACK TOKEN"
sc = SlackClient(token)
globalChannel = "C07RLKT6C"
if sc.rtm_connect():
    print "> Connected to Slack"

    while True:
        new_evts = sc.rtm_read()
        for evt in new_evts:
            if "type" in evt:
                if evt["type"] == "message" and evt["user"] != "U08C6H4JV" and evt["channel"] == globalChannel and "text" in evt:
                    channel = evt["channel"]

                    user = evt["user"]
                    userInfo = json.loads(sc.api_call("users.info", user=user))
                    userName = userInfo["user"]["name"]

                    message = evt["text"]
                    messageReturn = ("%s: %s" % (userName, message))
                    #print("channel: %s \nuser: %s \nmessage %s" % (channel, user, message))
                    #print messageReturn
                    sc.api_call("chat.postMessage", as_user="true", channel=globalChannel, text=messageReturn)
            #time.sleep(1)

else:
    print "> Connection Failed."
