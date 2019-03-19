import pygame as py
import Block
py.init()
py.mixer.init()

digits = int(input('Number of digits : '))
timestep = 10000
clack = py.mixer.Sound('clack.ogg')

screen = py.display.set_mode((800,400))

w = 30
h = 200
count = 0
myfont = py.font.SysFont('monosoace', 24)

block1 = Block.block(100,200,20,0,1,h)
block2 = Block.block(350,200,100,-1/timestep,pow(100,digits-1),h)



while True:
  py.time.delay(1)

  for event in py.event.get():
    if event.type == py.QUIT:
      print('Value of Pi is {}'.format(count))
      py.quit()
      break

  screen.fill((0, 0, 0))

  text = myfont.render('Number of Collisions : ' + str(count), 10, (0, 0, 255))
  screen.blit(text, (300, 300))

  for i in range(timestep):

    if block1.collision(block2):
      clack.play()
      block1.v, block2.v = block1.elastic_collision(block2), block2.elastic_collision(block1)
      count += 1

    if block1.wall_collision():
      clack.play()
      block1.v *= -1
      count += 1

    block1.move()
    block2.move()

  py.draw.rect(screen, (255,0,0), (block1.x, h, block1.w, block1.y - block1.w))
  py.draw.rect(screen, (0,255,0), (block2.x, h, block2.w, block2.y - block2.w))

  py.display.update()

