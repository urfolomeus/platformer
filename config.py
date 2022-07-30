OPTS = {
  "rows": 20,
  "cols": 20,
  "tile_size": 50,
  "title": "Platformer",
}

class Config:
  def __init__(self):
    self.width = OPTS["rows"] * OPTS["tile_size"]
    self.height = OPTS["cols"] * OPTS["tile_size"]
    self.tile_size = OPTS["tile_size"]
    self.title = OPTS["title"]

config = Config()
