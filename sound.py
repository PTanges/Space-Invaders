import pygame as pg
from pygame import mixer
import time

# Todo: After game restart (game over), music does not correctly replay despite either unpause nor play

class Sound:
    bgm = "sounds/Moog_City.mp3"
    def __init__(self):
        mixer.init()
        self.phaser_sound = mixer.Sound("sounds/alienlaser.wav")
        self.ship_hit = mixer.Sound("sounds/Ship_Hit.wav")
        self.transition = mixer.Sound("sounds/Transition.wav")
        self.outer_wild = mixer.Sound("sounds/approaching.wav")
        self.volume = 0.1
        self.set_volume(self.volume)
        '''
        # Better format
        self.sound_library = {'KEY' : mixer.Sound(string)} ...
        '''

    def set_volume(self, volume=0.3):
        mixer.music.set_volume(volume)
        self.phaser_sound.set_volume(3 * volume)

    def play_music(self, filename):
        self.stop_music()
        mixer.music.load(filename)
        mixer.music.play(loops=-1)

    def pause_music(self):
        mixer.music.pause()

    def unpause_music(self):
        mixer.music.unpause()

    def stop_music(self):
        mixer.music.stop()

    def play_phaser(self):
        mixer.Sound.play(self.phaser_sound)

    def play_ship_explosion(self):
        mixer.Sound.play(self.ship_hit)

    def play_level_transition(self):
        mixer.Sound.play(self.transition)

    def play_approaching_sfx(self):
        mixer.Sound.play(self.outer_wild)

    def play_game_over(self):
        self.stop_music()
        self.play_music("sounds/gameover.wav")
        time.sleep(2.9)
        self.stop_music()