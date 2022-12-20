from talon import actions, Module, Context

module = Module()  
module.tag('fire_chicken_force_dragon', desc = 'Forces use of the dragon speech engine')
dragon_forced_context = Context()

@module.action_class
class Actions:
    def fire_chicken_toggle_forced_dragon():
        '''Toggles whether or not to force dragon to be the speech engine'''
        if len(dragon_forced_context.tags) == 0:
            enable_dragon_forced_context()
        else:
            disable_dragon_forced_context()
    
def enable_dragon_forced_context():
    dragon_forced_context.tags = ['user.fire_chicken_force_dragon']
def disable_dragon_forced_context():
    dragon_forced_context.tags = []
