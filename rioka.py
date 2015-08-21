#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import json
import urllib2
import random
import re

from microsofttranslator import Translator
from slackclient import SlackClient

print "> Rioka has started"

execfile("inc/import.py")
execfile("inc/settings.py")
execfile("inc/randomStrings.py")

if sc.rtm_connect():
    print "> Connected to Slack"
    sc.api_call("chat.postMessage", as_user="true", channel="#general", text="Rioka is tadaima~☆")
    while True:
        new_evts = sc.rtm_read()
        for evt in new_evts:
            #print(evt)
            if "type" in evt:
                if evt["type"] == "message" and "user" in evt and "text" in evt:
                    if evt["user"] != "U08C6H4JV":
                        channel = evt["channel"]
                        message = evt["text"]
                        #user = evt["user"]
                        #userInfo = json.loads(sc.api_call("users.info", user=user))
                        #userName = userInfo["user"]["name"]
                        #messageReturn = ("%s: %s" % (userName, message))
                        #print("channel: %s \nuser: %s \nmessage %s" % (channel, user, message))
                        #print messageReturn

                        #if evt["user"] == "U0896EZ1N": # Overwatch
                        #    sc.api_call("chat.postMessage", as_user="true", channel=channel, text="shh")

                        if evt["user"] == "U07RM885B": # Kaori
                            if message.startswith("say in "):
                                if message == "say in ":
                                    sc.api_call("chat.postMessage", as_user="true", channel=channel, text="I don't know what you want me to say. :disappointed:")
                                else:
                                    string = message.split(" ", 3)
                                    toChannel = re.sub("[<\#>]", "", string[2], 0, 0)
                                    messageReturn = ("%s: %s" % (toChannel, string[3]))
                                    sc.api_call("chat.postMessage", as_user="true", channel=toChannel, text=string[3].encode('utf-8'))

                        if evt["user"] == "U09218631": # Nano
                            execfile("converse/nano.py")

                        if ("nya" in message) or (u"にゃ" in message) or (u"ニャ" in message):
                            sc.api_call("chat.postMessage", as_user="true", channel=channel, text="(=^・^=)")

                        if message.lower().startswith("rioka"):
                            # RIOKA COMMAND
                            if (message.lower()[:6] == "rioka "):
                                command = message.lower().split("rioka ",1)[1]
                            else:
                                command = "rioka"

                            # COMMANDS
                            if command.startswith("translate"):
                                execfile("commands/translate.py")
                            elif command.startswith("search"):
                                execfile("commands/search.py")
                            elif command.startswith("who is"):
                                execfile("commands/userinfo.py")
                            elif command == "rioka":
                                sc.api_call("chat.postMessage", as_user="true", channel=channel, text=random.choice(randomRioka))

        time.sleep(.1)

else:
    print "> Connection Failed."
