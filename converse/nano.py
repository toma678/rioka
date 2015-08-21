#!/usr/bin/env python
# -*- coding: utf-8 -*-

if message == u"ただいま〜":
    sc.api_call("chat.postMessage", as_user="true", channel=channel, text="おかえり～")
