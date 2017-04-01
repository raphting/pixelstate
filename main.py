import os
import requests
import sys
import pushover

PIXELSTATE = "https://spacestate.pixelbar.nl/spacestate.php"
PERSIST_STATE = os.environ['PIXELSTATE']

#Bootstrap file if not existing
if not os.path.isfile(PERSIST_STATE):
	print("Bootstraping persistence...")
	with open(PERSIST_STATE, "w") as f:
		f.write("open")
		f.close()

print("Requesting pixel state...")
r = requests.get(PIXELSTATE).json()
if 'state' not in r:
	print("Given JSON seems to be broken. Missing state key. Exit.")
	sys.exit(1)


f = open(PERSIST_STATE, "r+")
if f.read() == r['state']:
	#No state change
	print("No state change. Nothing to do here. Exit.")
	sys.exit(0)

print("Sending Push notification for pixel state change")
pushover.init(os.environ['PUSHOVER_TOKEN'])
pushover.Client(os.environ['PUSHOVER_USER']).send_message("Pixelbar is now " + r['state'], title="Pixelbar")

f.seek(0)
f.write("open")
f.truncate()
f.close()
print("Done.")
