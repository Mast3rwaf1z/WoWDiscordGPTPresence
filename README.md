# RichPresence Addon

The RichPresence addon is a World of Warcraft addon that gathers the current zone, character name, character class, and character level, and saves it in the SavedVariables file.

The saved data is then read by a Python program using the pypresence library, which sets up a rich presence on Discord. The rich presence displays the player's name, level, class, and current zone.
## File structure
```
RichPresence/
├── RichPresence.toc
├── RichPresence.lua
└── RichPresence.py
```

* `RichPresence.toc`: The addon's Table of Contents file, which defines its metadata, such as the addon name, version, and saved variables.
* `RichPresence.lua`: The addon's main Lua script, which gathers the player's data and saves it in the SavedVariables file.
* `RichPresence.py`: The Python script that reads the data from the SavedVariables file and displays the rich presence on Discord.

## Dependencies

* World of Warcraft
* Python 3
* pypresence library

## Usage

1. Copy the `RichPresence` folder to the `World of Warcraft/_retail_/Interface/AddOns` directory.
2. Launch World of Warcraft and enable the RichPresence addon.
3. Run the `RichPresence.py` Python script to display the rich presence on Discord. Make sure to install the pypresence library using `pip install pypresence` before running the script.

## Credits

* Mast3r_waf1z: 
  * Cleaned the code and a little debugging and added interactiveness
* ChatGPT: 
  * Primary author