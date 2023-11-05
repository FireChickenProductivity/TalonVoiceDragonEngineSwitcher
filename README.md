# Talon Voice Dragon Engine Switcher
Provides functionality for switching to and from using Dragon as one's talon voice speech engine. This is no longer being maintained.

## Commands
toggle force dragon: toggles whether talon should be forced to use dragon as its speech engine.

## Settings
fire_chicken_dragon_microphone_toggle_keypress: The key sequence to press to toggle dragon's microphone. You might need to change this for the code to be able to successfully turn dragon's microphone on and off.

## Tags
user.fire_chicken_force_dragon: When this tag is active, talon is forced to use dragon as its speech engine.

## Known Issues
If talon is forced to use dragon's engine, it will not be able to switch back to conformer through voice commands if dragon freezes or crashes. 

The code tries to toggle dragon's microphone every time you start and stop using dragon as your speech engine. This means that if the microphone's status gets out of sync with which speech engine is active, this could cause dragon to still be active while it is not your talon speech engine making it run commands independently of talon or cause dragon to be your active speech engine with the microphone off.

## Stuff not documented yet
The stuff in the correction folder was for working with dragon's correction system. I have not used it in a while but plan on looking at it again and documenting it later.
