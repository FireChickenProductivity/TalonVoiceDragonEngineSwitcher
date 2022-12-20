from talon import actions, settings, Module

module = Module()

dictation_box_keypress = module.setting(
    'fire_chicken_dragon_dictation_box_keypress',
    type = str,
    default = 'ctrl-shift-d', 
    desc = "The key combination used to try to open Dragon's dictation box",
)
correction_keypress = module.setting(
    'fire_chicken_dragon_correction_keypress',
    type = str,
    default = 'keypad_minus',
    desc = "The key combination used to try to open Dragon's correction menu", 
)

dragon_box_opening_delay = module.setting(
    'fire_chicken_dragon_box_opening_delay',
    type = int,
    default = 2000,
    desc = "How long to wait for Dragon's dictation box to open in milliseconds",
)
def wait_for_dragon_box_opening_delay():
    wait_for_delay_setting(dragon_box_opening_delay)
def wait_for_delay_setting(setting):
    actions.sleep(f'{setting.get()}ms')

correction_delay = module.setting(
    'fire_chicken_dragon_correction_delay',
    type = int,
    default = 500,
    desc = "How long to wait for a Dragon correction to finish",
)
def wait_for_correction_delay():
    wait_for_delay_setting(correction_delay)

@module.action_class
class Actions:
    def fire_chicken_open_dragon_dictation_box():
        '''Opens dragon's dictation box'''
        actions.key(dictation_box_keypress.get())
    def fire_chicken_open_dragon_correction():
        '''Opens dragon's correction menu'''
        actions.key(correction_keypress.get())
    def fire_chicken_correct_selection_using_dragon_dictation_box():
        '''Uses Dragon's dictation box and correction menu to try to correct the current selection'''
        actions.user.fire_chicken_open_dragon_dictation_box()
        wait_for_dragon_box_opening_delay()
        actions.edit.select_all()
        actions.user.fire_chicken_open_dragon_correction()
    def fire_chicken_pick_dragon_correction_option(option: int):
        '''Picks the specified option from Dragon's correction menu'''
        option_string = str(option)
        actions.key('alt-' + option_string)
    def fire_chicken_dragon_dictation_box_transfer():
        '''Transfers the text from Dragon's dictation box'''
        actions.key('alt-t')
    def fire_chicken_dragon_dictation_box_cancel():
        '''Cancels out of the Dragon dictation box'''
        actions.key('alt-c')
    def fire_chicken_transfer_dragon_correction_option(option: int):
        '''Chooses the specified Dragon correction option and transfers it'''
        actions.user.fire_chicken_pick_dragon_correction_option(option)
        wait_for_correction_delay()
        actions.user.fire_chicken_dragon_dictation_box_transfer()
