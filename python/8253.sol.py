def h(start, goal):
    # ensure that start and goal are valid positions
    assert "".join(sorted(start)) == " 12345678" and "".join(sorted(goal)) == " 12345678"
    
    # Work out how many tiles are out of place
    
    tiles = {}
    for tile in range(0, len(start)):
        if start[tile] != goal[tile]:
            if goal[tile] != " ":
                tiles[start[tile]] = 1
    
    return len(tiles)