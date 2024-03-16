import time
import pygame as pg
from pygame.sprite import Sprite
from lasers import Lasers
from timer import Timer
from vector import Vector 
from time import sleep
from random import randint

class Ship(Sprite):
  laser_image_files = [f'images/ship_laser_0{x}.png' for x in range(4, 10)]
  laser_images = [pg.image.load(x) for x in laser_image_files]

  ship_explosion_images = [pg.image.load(f'images/ship_explode{x}.png') for x in range(0,6)]

  def __init__(self, game, v=Vector()):
    super().__init__()
    self.game = game 
    self.v = v
    self.settings = game.settings
    self.stats = game.stats
    self.laser_timer = Timer(image_list=Ship.laser_images, delta=10)
    self.lasers = Lasers(game=game, v=Vector(0, -1) * self.settings.laser_speed, 
                         timer=self.laser_timer, owner=self)
    self.shiptimer = Timer(Ship.ship_explosion_images, delta=10, looponce=True)
    self.aliens = game.aliens
    self.continuous_fire = False
    self.screen = game.screen 
    self.screen_rect = game.screen.get_rect() 

    self.image = pg.image.load('images/ship.png')
    self.rect = self.image.get_rect()

    self.rect.midbottom = self.screen_rect.midbottom 
    self.fire_counter = 0

    self.isdying = False
    self.isreallydead = False

  def set_aliens(self, aliens): self.aliens = aliens

  # def set_lasers(self, lasers): self.lasers = lasers

  def set_sb(self, sb): self.sb = sb

  def clamp(self):
    r, srect = self.rect, self.screen_rect   # read-only alias 
    # cannot use alias for writing, Python will make a copy
    #     and will change the copy instead

    if r.left < 0: self.rect.left = 0
    if r.right > srect.right: self.rect.right = srect.right 
    if r.top < 0: self.rect.top = 0
    if r.bottom > srect.bottom: self.rect.bottom = srect.bottom
      
  def set_speed(self, speed): self.v = speed

  def add_speed(self, speed): self.v += speed

  def all_stop(self): self.v = Vector()
  
  def fire_everything(self): self.continuous_fire = True

  def cease_fire(self): self.continuous_fire = False

  def fire(self):
    timer = Timer(Ship.laser_images, start_index=randint(0, len(Ship.laser_images) - 1), delta=10)
    self.lasers.add(owner=self, timer=timer)
    # Todo: implement ship shooting sound sfx
    # self.sound.play_phaser()

  def hit(self): 
    print('Abandon ship! Ship has been hit!')
    self.isdying = True
    self.game.sound.play_ship_explosion()
    self.timer = self.shiptimer
    # time.sleep(2.5)

    self.stats.ships_left -= 1
    self.sb.prep_ships()
    if self.stats.ships_left <= 0:
      self.game.game_over()
    else:
      self.game.restart()

  def laser_offscreen(self, rect): return rect.bottom < 0

  def laser_start_rect(self):
    rect = self.rect
    rect.midtop = self.rect.midtop
    return rect.copy()
  
  def center_ship(self): 
    self.rect.midbottom = self.screen_rect.midbottom 
    self.x = float(self.rect.x)

  def reset(self):
    self.lasers.empty()
    self.center_ship()

  def update(self):
    if self.shiptimer.finished():
      self.isreallydead = True
      self.kill()

    self.rect.left += self.v.x * self.settings.ship_speed
    self.rect.top += self.v.y * self.settings.ship_speed
    self.clamp()
    self.draw()
    if self.continuous_fire and self.fire_counter % self.settings.ship_fast_fire_rate == 0:
      self.fire()
    self.fire_counter += 1
    self.lasers.update()

  def draw(self):
    self.screen.blit(self.image, self.rect)


if __name__ == '__main__':
  print("\nERROR: ship.py is the wrong file! Run play from alien_invasions.py\n")

  