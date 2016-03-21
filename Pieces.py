Pieces = {"Pawn":
              {"Movement": {"North": 2, "NorthEast": None, "East": None, "SouthEast": None, "South": None,
                            "SouthWest": None, "West": None, "NorthWest": None},
               "Location": None},
          # Handle the Night differntly due to his unique movement style
          "Knight":
              {"Movement": {"North": 2, "NorthEast": 1, "East": 2, "SouthEast": 1, "South": 2, "SouthWest": 1,
                            "West": 2, "NorthWest": 1},
               "Location": None},
          "Bishop":
              {"Movement": {"North": None, "NorthEast": "All", "East": None, "SouthEast": "All", "South": None,
                            "SouthWest": "All", "West": None, "NorthWest": "All"},
               "Location": None},
          "Rook":
              {"Movement": {"North": "All", "NorthEast": None, "East": "All", "SouthEast": None, "South": "All",
                            "SouthWest": None, "West": "All", "NorthWest": None},
               "Location": None},
          "Queen":
              {"Movement": {"North": "All", "NorthEast": "All", "East": "All", "SouthEast": "All", "South": "All",
                            "SouthWest": "All", "West": "All", "NorthWest": "All"},
               "Location": None},
          "King":
              {"Movement": {"North": 1, "NorthEast": 1, "East": 1, "SouthEast": 1, "South": 1, "SouthWest": 1,
                            "West": 1, "NorthWest": 1},
               "Location": None}
          }
