class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (70, 70, 70)

        self.laser_width = 5
        self.laser_height = 15
        self.laser_color = (255, 0, 0)

        self.alien_spacing = 1.2
        self.fleet_drop = 10

        self.ship_limit = 3

        self.speedup_scale = 1.5
        # self.score_scale = 1.5
        self.score_scale = 1.0

        self.aliens_fireevery = 30

        self.ufo_spawn_chance = 25 # by percentage
        self.ufo_spawn_delay = 2 # number of screen bounces
        self.ufo_spawn_limit = 1 # number of UFO's, int >= 0

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.laser_speed = 5
        self.alien_speed = 1
        self.ship_speed = 15

        self.alien_points = 50

        self.ship_slow_fire_rate = 8
        self.ship_fast_fire_rate = 2

    def increase_speed(self):
        # self.laser_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        # self.ship_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)


if __name__ == '__main__':
    print("\nERROR: settings.py is the wrong file! Run play from alien_invasions.py\n")
