#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import json
import urllib
import urllib2
import random
import re

from microsofttranslator import Translator
from slackclient import SlackClient

print "> Rioka has started"
translatorClientID = ""
translatorClientSecret = ""
token = ""
sc = SlackClient(token)
globalChannel = "C07RLKT6C" #dev - #gen: C07RLUEUV
randomFirst  = ["Ryoukaishimashita!", "Wakarimashita!"]
randomSecond = ["Please wait a sec...", "Gimmie a sec..."]
if sc.rtm_connect():
    print "> Connected to Slack"
    while True:
        new_evts = sc.rtm_read()
        for evt in new_evts:
            #print(evt)
            if "type" in evt:
                if evt["type"] == "message" and "user" in evt and "text" in evt:
                    if evt["user"] != "U08C6H4JV":
                        channel = evt["channel"]
                        message = evt["text"]

                        if evt["user"] == "U07RM885B": # Kaori
                            if message.startswith("say in "):
                                if message == "say in ":
                                    sc.api_call("chat.postMessage", as_user="true", channel=channel, text="I don't know what you want me to say. :disappointed:")
                                else:
                                    string = message.split(" ", 3)
                                    toChannel = re.sub("[<\#>]", "", string[2], 0, 0)
                                    messageReturn = ("%s: %s" % (toChannel, string[3]))
                                    sc.api_call("chat.postMessage", as_user="true", channel=toChannel, text=string[3].encode('utf-8'))

                        if ("nya" in message) or (u"にゃ" in message) or (u"ニャ" in message):
                            sc.api_call("chat.postMessage", as_user="true", channel=channel, text=u"(=^・^=)")

                        if message.startswith("rioka"):
                            # RIOKA COMMAND
                            if (message == "rioka") or (message == "rioka "):
                                command = "rioka"
                            else:
                                command = message.split("rioka ",1)[1]

                            # COMMANDS
                            if command.startswith("translate"):
                                # TRANSLATE
                                if (command == "translate") or (command == "translate "):
                                    sc.api_call("chat.postMessage", as_user="true", channel=channel, text="I don't know what you want me to translate. :disappointed:")
                                else:
                                    waitText = ("_%s_ %s" % (random.choice(randomFirst), random.choice(randomSecond)))
                                    sc.api_call("chat.postMessage", as_user="true", channel=channel, text=waitText)
                                    if command.startswith("translate to ja"):
                                        string = command.split("translate to ja ",1)[1]
                                        translateName = "Japanese"
                                        translateTo = "ja"
                                    else:
                                        string = command.split("translate ",1)[1]
                                        translateName = "English"
                                        translateTo = "en"
                                    translator = Translator(translatorClientID, translatorClientSecret)
                                    messageReturn = ("In %s, that's: %s" % (translateName, translator.translate(string, translateTo)))
                                    sc.api_call("chat.postMessage", as_user="true", channel=channel, text=messageReturn.encode('utf-8'))

                            elif command.startswith("search"):
                                # SEARCH
                                if (command == "search") or (command == "search "):
                                    sc.api_call("chat.postMessage", as_user="true", channel=channel, text="I don't know what you want me to search! :anguished:")
                                else:
                                    waitText = ("_%s_ %s" % (random.choice(randomFirst), random.choice(randomSecond)))
                                    sc.api_call("chat.postMessage", as_user="true", channel=channel, text=waitText)
                                    string = urllib.quote_plus(command.split("search ",1)[1])
                                    response = urllib2.urlopen("https://www.googleapis.com/customsearch/v1?key=AIzaSyAruE7wV7LaL1tZ1XJRHCtA7pmuz9EfXl8&cx=006735756282586657842:s7i_4ej9amu&q=" + string)
                                    data = json.loads(response.read())
                                    response.close()
                                    messageReturn = ("%s\n%s" % (data["items"][0]["link"], data["items"][0]["snippet"]))
                                    sc.api_call("chat.postMessage", as_user="true", channel=channel, text=messageReturn.encode('utf-8'), unfurl_links="false", unfurl_media="false")

else:
    print "> Connection Failed."
