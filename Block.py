

class block:

  def __init__(self, x, y, w, v, m):
    self.x = x
    self.y = y
    self.v = v
    self.w = w
    self.m = m

  def move(self):
    self.x += self.v

  def collision(self, other):
    return not (self.x + self.w < other.x or self.x > other.x + other.w)

  def wall_collision(self):
    return self.x < 0

  def elastic_collision(self, other):
    sumM = self.m + other.m
    v = (self.m - other.m)*self.v/sumM
    v += (2*other.m*other.v)/sumM
    return v