from pypeds.shape2d import Point2D

def shortest_path(map, dest, default_ident = 0, block_ident = 1):
    """ Find shortest-path field

    :param map: the proposed map (2-d)
    :param dest: the goal, a point
    :param default_ident: the identifier for default cell
    :param block_ident: the identifier for block cell
    :return: floor field and a distance matrix
    """
    w = len(map)
    l = len(map[0])
    dist_map = [[0 for i in range(w)] for j in range(l)]
    field = [[0 for i in range(w)] for j in range(l)]

    for line in map:
        assert(len(line) == l)

    queue = [dest]
    field[dest.x][dest.y] = dest
    while len(queue) != 0:
        cell = queue.pop(0)
        for p in gen_adjs(cell):
            if not (0 <= p.x < w and 0 <= p.y < l and map[p.x][p.y] != block_ident and not p.__eq__(dest)):
                continue
            dist = dist_map[p.x][p.y]
            if dist == 0 or dist > dist_map[cell.x][cell.y] + p.dist(cell):
                dist_map[p.x][p.y] = dist_map[cell.x][cell.y] + p.dist(cell)
                field[p.x][p.y] = cell
                queue.append(p)

    return field, dist_map

def gen_adjs(cell):
    """ Generate a list of adjuct cells for cell

    """
    x = cell.x
    y = cell.y
    return [Point2D(x-1,y-1),Point2D(x-1,y),Point2D(x-1,y+1),Point2D(x,y-1),Point2D(x,y+1),Point2D(x+1,y-1),Point2D(x+1,y),Point2D(x+1,y+1)]



