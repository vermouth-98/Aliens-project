class Settings():
    """ A class to store all settings for Alien Invasion """
    def __init__(self):
        """ Initialize the game's settings """
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (0,0,0)

        #ship settings
        self.ship_limit = 3
        self.ship_speed = 2

        #bullet setting
        self.bullet_width = 100
        self.bullet_height = 15 
        self.bullet_speed = 30
        self.bullet_color = 255,0,0
        self.bullet_allowed = 3
        self.file_name = 'save_high.json'
        #alien setting
        
    
        #how quickly the game speeds up
        self.speedup_scale =1.1
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        self.alien_speed = 0.5
        self.fleet_drop_speed = 10
        #fleet direction of 1 represents right, -1 represents left
        self.fleet_direction = 1
        self.alien_points = 100
    
    def increase_speed (self):
        ''' Increase speed settings. '''
        self.alien_speed *= self.speedup_scale
        self.fleet_drop_speed *= self.speedup_scale
