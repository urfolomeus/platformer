OPTS = {
  "rows": 20,
  "cols": 20,
  "player_height": 80,
  "player_start_x": 100,
  "player_step_size": 5,
  "tile_size": 50,
  "title": "Platformer",
  "gravity": 1,
  "jump_height": -15,
  "fps": 60,
  "draw_grid": False,
  "draw_rect": False,
  "cheat_mode": False,
  "character": "rockie",
}

class Config:
  def __init__(self):
    self.title = OPTS["title"]

    self.fps = OPTS["fps"]

    self.width = OPTS["rows"] * OPTS["tile_size"]
    self.height = OPTS["cols"] * OPTS["tile_size"]
    self.tile_size = OPTS["tile_size"]

    self.player_size = (OPTS["player_height"] / 2, OPTS["player_height"])
    self.player_start_x = OPTS["player_start_x"]
    self.player_start_y = self.height - self.tile_size - OPTS["player_height"]
    self.player_step_size = OPTS["player_step_size"]

    self.gravity = OPTS["gravity"]
    self.jump_height = OPTS["jump_height"]

    self.draw_grid = OPTS["draw_grid"]
    self.draw_rect = OPTS["draw_rect"]

    self.character = OPTS["character"]
    self.cheat_mode = OPTS["cheat_mode"]

config = Config()
