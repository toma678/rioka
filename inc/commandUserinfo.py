#!/usr/bin/env python
# -*- coding: utf-8 -*-

if (command == "who is") or (command == "who is "):
    sc.api_call("chat.postMessage", as_user="true", channel=channel, text="At least give me a name... :disappointed:")
else:
    waitText = ("_%s_ %s" % (random.choice(randomOkay), random.choice(randomWait)))
    sc.api_call("chat.postMessage", as_user="true", channel=channel, text=waitText)
    string = urllib.quote_plus(command.split("who is ",1)[1])
    userList = json.loads(sc.api_call("users.list"))
    for x in userList["members"]:
        if string == x["name"]:
            userInfo = json.loads(sc.api_call("users.info", user=x["id"]))
            if not "real_name" in userInfo["user"]["profile"]:
                userInfo["user"]["profile"]["real_name"] = "*unknown*"
            if not "email" in userInfo["user"]["profile"]:
                userInfo["user"]["profile"]["email"] = "Unknown email"
            if not "skype" in userInfo["user"]["profile"]:
                userInfo["user"]["profile"]["skype"] = "unknown"
            if not "phone" in userInfo["user"]["profile"]:
                userInfo["user"]["profile"]["phone"] = "unknown"
            if userInfo["user"]["id"] == "U09218631": # nano
                extraData = "my waifu, "
            elif userInfo["user"]["id"] == "U0896EZ1N": #overwatch
                extraData = "my senpai who doesn't notice me, "
            elif userInfo["user"]["id"] == "U07RM885B": #kaori
                extraData = "my goshujinsama, "
            else:
                extraData = ""
            messageReturn = ("%s is %salso known as '%s' <%s>\nUser ID: %s\nSkype: %s\nPhone: %s" % (userInfo["user"]["name"], extraData, userInfo["user"]["profile"]["real_name"], userInfo["user"]["profile"]["email"], userInfo["user"]["id"], userInfo["user"]["profile"]["skype"], userInfo["user"]["profile"]["phone"]))
            sc.api_call("chat.postMessage", as_user="true", channel=channel, text=messageReturn)
            break
    else:
        sc.api_call("chat.postMessage", as_user="true", channel=channel, text="I don't know who you're talking about! :anguished: Try checking the name?")
