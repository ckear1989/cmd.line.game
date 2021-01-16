
class card():
  def __init__(
    self,
    cost=0,
    coin=0,
    color=None,
    number=0,
    shape=None,
    fill=None
  ):
    self.cost = cost
    self.coin = coin
    self.color = color
    self.number = number
    self.shape = shape
    self.fill = fill

  def __repr__(self):
    outstr = 'cost: %s' % self.cost
    return outstr

if __name__ == "__main__":
  acard = card(cost=1)
  print(acard)

