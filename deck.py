
class deck():
  def __init__(self, size):
    self.size = size

  def __str__(self):
    return 'size %s' % self.size

if __name__ == "__main__":
  deck = deck(20)
  print(deck)

