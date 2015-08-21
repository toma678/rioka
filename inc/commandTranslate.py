#!/usr/bin/env python
# -*- coding: utf-8 -*-

if (command == "translate") or (command == "translate "):
    sc.api_call("chat.postMessage", as_user="true", channel=channel, text="I don't know what you want me to translate. :disappointed:")
else:
    waitText = ("_%s_ %s" % (random.choice(randomOkay), random.choice(randomWait)))
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
