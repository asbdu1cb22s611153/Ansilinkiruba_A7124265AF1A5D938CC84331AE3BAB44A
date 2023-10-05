class player:
  def play(self):
    print("The Player is playing Cricket")
class batsman(player):
  def play(self):
    print("The Batsman is Batting")
class bowler(player):
  def play(self):
    print("The Bowler is bowling")
Batsman=batsman()
Bowler=bowler()
