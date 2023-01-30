# You need to get your token to use this macro.
# Check this out if you don't know how to get token.
# https://www.youtube.com/watch?v=0wvIOPHiF0A (by Initial Solution)

# Checks if require package is installed.
# Do not remove following lines unless you already installed package.
import pkgutil
if not pkgutil.find_loader('httpx'):
    import pip # NOTE: Deprecated, change after.
    if not hasattr(pip, 'main'): import pip._internal as pip
    pip.main(['install', 'httpx'])
    del pip
del pkgutil

import time, httpx, threading

# Change following variables to change settings.

CHANNELS = []
# "id" is the channel's id that you can get with developer mode on Discord.
# "delay" is the channel's slow mode delay in second.
# Example: 
# CHANNELS = [
#     {"id": 925654304256307200, "delay": 900},
#     {"id": 953830751571427368, "delay": 300},
#     {"id": 891368716758052874, "delay": 120},
#     {"id": 1026658601399488542, "delay": 300},
#     {"id": 1026662598332121119, "delay": 120},
#     {"id": 1026662729634828289, "delay": 300},
# ]

# Put your Discord token in quotes.
# Example: TOKEN = 'mYDisCorDTOKen'
TOKEN = ''

# Put your message's content inside quotes.
# Example: CONTENT = 'Trading hoh'
# "\n" means indents. You can use it like 'This is line 1\nThis is line 2'.
# If you wanna use "\" in message, then use "\\".
CONTENT = ''

# ⚠ Do not edit anything from under this line.
client = httpx.Client(headers={'authorization': TOKEN, 'content-type': 'application/json'}) 

# Creates threads for looping many macros at once.
def create_new_macro(channel):
    def macro():
        while 1: # You can use while True instead.
            id = channel['id']
            delay = channel['delay']
            
            response = client.post(f'https://discord.com/api/v9/channels/{id}/messages', json={'content': CONTENT})
            try: 
                response.raise_for_status()
            except Exception as exception: 
                print('[!]', exception)
            time.sleep(delay) 

    thread = threading.Thread(target=macro, daemon=True)
    return thread.start()

# Makes the process run forever until user closes the program.
def run_until_keyboard_interrupt():
    try:
        while 1: pass
    except KeyboardInterrupt:
        return print('[!]', 'The macro cancelled by the user.')

for channel in CHANNELS: create_new_macro(channel)
run_until_keyboard_interrupt()
