Pixelstate
==========

Send a Push notification in case Pixelbar gets opened or closed.

Install
-------

Install the requirements with pip `pip install --user -r requirements.txt`
and set the environment variables
```
PUSHOVER_TOKEN
PUSHOVER_USER
PIXELSTATE
```

You'll need an account with https://pushover.net. The `PIXELSTATE` variable is the link to a file on your file system to persist the last state.
