#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import sys
import tweepy
from local_keys import *

def tweet(message):

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    result = api.update_status(message)
    return result
    
if __name__ == '__main__':

    f = open('/tmp/clip.log', 'a')
    f.write("running clip\n")

    message = gtk.clipboard_get().wait_for_text()
    if len(message) > 140:
        message = message[0:140]

    f.write("message to post is: %s\n" % message)

    result = tweet(message)
    f.write('result: ' + str(result) + "\n")
    f.close()
