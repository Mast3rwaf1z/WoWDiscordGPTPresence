import time
from os import listdir
from sys import argv

wowpath = input("Specify path to wow install") if not "--wowpath" in argv else argv[argv.index("--wowpath")+1]

orange = lambda s: f'\033[38;2;{int("e0",16)};{int("53", 16)};{int("00", 16)}m{s}\033[0m'

accounts = listdir(f'{wowpath}/_retail_/WTF/Account/')
accounts.remove("SavedVariables")
if len(accounts) > 1:
    index = int(input("\n".join([f'{orange(i)}: {accounts[i][-1]}' for i in range(len(accounts))]) + f'\nChoose the {orange("index")} of the account to use: '))
else:
    index = 0

def getTable():
    with open(f'{wowpath}/_retail_/WTF/Account/{accounts[index]}/SavedVariables/RichPresence.lua', 'r') as f:
        return f.read()

# Parse the Lua table into a Python dictionary
getDict = lambda: {
    key.strip(): value.strip() for key, value in [
        (
            line.split("=")[0].strip()[1:-1], 
            line.split("=")[1][1:-1]
        ) for line in getTable().replace('"', '').splitlines() if "[" in line
    ]
}


# Set up the rich presence client
import pypresence
RPC = pypresence.Presence(client_id='1089858208954318858')
RPC.connect()

# Start the rich presence loop
try:
    t = time.time()
    while True:
        # Update the rich presence
        data_dict = getDict()
        RPC.update(
            large_text='World of Warcraft',
            details=f"{data_dict['name']}: {data_dict['level']} {data_dict['class']}",
            state=f"In {data_dict['zone']}",
            start=t,
            small_image="wow_logo",
            buttons=[
                {
                    "label":"Profile",
                    "url":f"https://worldofwarcraft.blizzard.com/en-gb/character/eu/{data_dict['realm']}/{data_dict['name']}", },
                {
                    "label":"Logs",
                    "url":f"https://www.warcraftlogs.com/character/eu/{data_dict['realm']}/{data_dict['name']}"}]
        )

        # Wait for 15 seconds before updating again
        time.sleep(15)
except KeyboardInterrupt:
    # Clean up the rich presence client
    RPC.close()
