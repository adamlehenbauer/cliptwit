cliptwit - post the clipboard to twitter
========

I use cliptwit to post the contents of my clipboard to twitter ever hour from 9-5. In addition to the short python script, this requires the tweepy python library and a cron task.

Note that this only works on linux, and that I have only tested on Ubuntu 10.04. Clipboard access would work differently on windows, and windows doesn't come with cron.

Installing *tweepy*
-------------------

Follow [these instructions](https://github.com/joshthecoder/tweepy/blob/master/INSTALL), also mentioned in the authentication howto link.

Authenticating with twitter
---------------------------

1. Follow the steps [here](http://jeffmiller.github.com/2010/05/31/twitter-from-the-command-line-in-python-using-oauth) to grant access to your account
1. Copy `local_keys.py.template` to `local_keys.py`
1. Enter the {consumer, access} {keys, secrets} in local_keys.py; be sure not to check this in

Setting the cron
----------------

Mine looks like:

    00 09-17 * * *		DISPLAY=:0 /workspace/cliptwit/clip.py

A good cron reference is [here](http://www.thegeekstuff.com/2009/06/15-practical-crontab-examples/), and most importantly, *[this link](http://www.codecoffee.com/tipsforlinux/articles/23.html)* explains why you need `DISPLAY=:0`, and why cron won't work with X without it.
