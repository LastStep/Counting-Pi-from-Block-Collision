import pygame as py
import Block
py.init()

screen = py.display.set_mode((500,500))

digits = int(input('Number of digits : '))
timestep = 10000

block1 = Block.block(100,100,20,0,1)
block2 = Block.block(300,100,100,-1/timestep,pow(100,digits-1))

w = 30
h = 30
count = 0
myfont = py.font.SysFont('monosoace', 24)

while True:
  py.time.delay(1)

  for event in py.event.get():
    if event.type == py.QUIT:
      py.quit()
      break

  screen.fill((0, 0, 0))

  text = myfont.render(str(count), 1, (0, 0, 255))
  screen.blit(text, (400, 400))

  for i in range(timestep):

    if block1.collision(block2):
      block1.v, block2.v = block1.elastic_collision(block2), block2.elastic_collision(block1)
      count += 1

    if block1.wall_collision():
      block1.v *= -1
      count += 1

    block1.move()
    block2.move()

  py.draw.rect(screen, (255,0,0), (block1.x, block1.y, block1.w, block1.w))
  py.draw.rect(screen, (0,255,0), (block2.x, block2.y, block2.w, block2.w))

  py.display.update()

