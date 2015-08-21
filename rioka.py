#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "> Rioka has started"

execfile("inc/import.py")
execfile("inc/settings.py")
execfile("inc/randomStrings.py")

if sc.rtm_connect():
    print "> Connected to Slack"
    sc.api_call("chat.postMessage", as_user="true", channel="#general", text=random.choice(randomReturn))
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

                        if evt["user"] == "U09218631": # Nano
                            execfile("inc/converseNano.py")

                        if ("nya" in message) or (u"にゃ" in message) or (u"ニャ" in message):
                            sc.api_call("chat.postMessage", as_user="true", channel=channel, text="(=^・^=)")

                        if message.startswith("rioka"):
                            # RIOKA COMMAND
                            if (message[:6] == "rioka "):
                                command = message.split("rioka ",1)[1]
                            elif (message[:6] == "rioka:"):
                                command = message.split("rioka:",1)[1]
                            else:
                                command = "rioka"

                            # COMMANDS
                            if command.startswith("translate"):
                                execfile("inc/commandTranslate.py")

                            elif command.startswith("search"):
                                execfile("inc/commandSearch.py")

                            elif command.startswith("who is"):
                                execfile("inc/commandUserinfo.py")

        time.sleep(.1)

else:
    print "> Connection Failed."
