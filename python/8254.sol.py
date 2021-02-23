from math import sqrt

def h(start, goal):
    assert "".join(sorted(start)) == " 12345678" and "".join(sorted(goal)) == " 12345678"
    # |1 3|  |123|
    # |824|  |8 4|
    # |756|  |756|
    
    # |876|   | 12|
    # |543|   |345|
    # |21 |   |678|
    
    #h("87654321 "," 12345678")
    
    # Work out the manhattah distance of each tile from its eventual goal
    
    manhattan_distance = 0
    
    startTiles = {}
    endTiles = {}
    x = 0
    y = 0
    for tile in range(0, len(start)):
        if tile % 3 == 0 and tile != 0:
            y += 1
            x = 0
        if start[tile] != goal[tile]:
            startTiles[start[tile]] = (y, x)
            endTiles[goal[tile]] = (y, x)
        x += 1
        
    for tile, coOrd in sorted(startTiles.items()):
        if tile != " ":
            y1, x1 = coOrd[0], coOrd[1]
            y2, x2 = endTiles[tile][0], endTiles[tile][1]
            
            y = int(sqrt((y2 - y1) ** 2))
            x = int(sqrt((x2 - x1) ** 2))
            
            manhattan_distance += x + y
    
    return manhattan_distance