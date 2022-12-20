from talon import settings, actions, Module

module = Module()
microphone_toggle_keypress = module.setting(
    'fire_chicken_dragon_microphone_toggle_keypress',
    type = str,
    default = 'keypad_plus',
    desc = "The keypress used to try to toggle dragon's microphone",
)

last_speech_engine = ''
def toggle_dragon_microphone_if_needed(new_speech_engine):
    print('speech engine change:', new_speech_engine)
    global last_speech_engine
    if new_speech_engine == last_speech_engine:
        return 
    if new_speech_engine == 'dragon' or last_speech_engine == 'dragon':
        toggle_dragon_microphone()
    last_speech_engine = new_speech_engine

def toggle_dragon_microphone():
    actions.key(microphone_toggle_keypress.get())

settings.register('speech.engine', toggle_dragon_microphone_if_needed)

@module.action_class
class Actions:
    def fire_chicken_toggle_dragon_microphone():
        '''Tries to toggle dragon's microphone'''
        toggle_dragon_microphone()