import pygame as pg

class Launch_Screen:
    def __init__(self):
        pass

    def play(self): pass

    def render_screen(self): pass

    def display_high_score(self): pass

    def exit_game(self):
        # write high score to txt file, may copy from the scoreboard file
        quit()

    def check_events(self):
        for event in pg.event.get():
            type = event.type

            if type == pg.KEYUP: pass
            elif type == pg.KEYDOWN: pass
            # Accept P for Play and Q for Quit as well
            # Todo: Implement screen
            # The key up and key down actions should "loop" which isn't too difficult

