OPTS = {
  "rows": 20,
  "cols": 20,
  "player_height": 80,
  "player_start_x": 100,
  "tile_size": 50,
  "title": "Platformer",
}

class Config:
  def __init__(self):
    self.title = OPTS["title"]

    self.width = OPTS["rows"] * OPTS["tile_size"]
    self.height = OPTS["cols"] * OPTS["tile_size"]
    self.tile_size = OPTS["tile_size"]

    self.player_size = (OPTS["player_height"] / 2, OPTS["player_height"])
    self.player_start_x = OPTS["player_start_x"]
    self.player_start_y = self.height - self.tile_size - OPTS["player_height"]

config = Config()
