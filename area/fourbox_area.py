def area(boxes):
    s = []
    for box in boxes:
        x1, y1, x2, y2 = box
        for x in xrange(x1, x2):
            for y in xrange(y1, y2):
                if contains(s, x, y): continue
                s.append((x,y))

    return len(s)

def contains(l, xpos, ypos):
    for t in l:
        x, y = t
        if x == xpos and y == ypos:
            return True
    
    return False


if __name__ == "__main__":

    boxes = [[1, 2, 4, 4], [2, 3, 5, 7], [3, 1, 6, 5], [7, 3, 8, 6]]
    print(area(boxes))

    #boxes = [[1, 1, 2, 6], [3, 3, 5, 6], [1, 4, 2, 7], [3, 4, 8, 8]]
    #print(area(boxes))
