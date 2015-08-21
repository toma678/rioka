#!/usr/bin/env python
# -*- coding: utf-8 -*-

if (command == "search") or (command == "search "):
    sc.api_call("chat.postMessage", as_user="true", channel=channel, text="I don't know what you want me to search! :anguished:")
else:
    waitText = ("_%s_ %s" % (random.choice(randomOkay), random.choice(randomWait)))
    sc.api_call("chat.postMessage", as_user="true", channel=channel, text=waitText)
    string = urllib.quote_plus(command.split("search ",1)[1])
    response = urllib2.urlopen("https://www.googleapis.com/customsearch/v1?key=AIzaSyAruE7wV7LaL1tZ1XJRHCtA7pmuz9EfXl8&cx=006735756282586657842:s7i_4ej9amu&q=" + string)
    data = json.loads(response.read())
    response.close()
    messageReturn = ("%s\n%s" % (data["items"][0]["link"], data["items"][0]["snippet"]))
    sc.api_call("chat.postMessage", as_user="true", channel=channel, text=messageReturn.encode('utf-8'), unfurl_links="false", unfurl_media="false")
