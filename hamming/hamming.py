def distance(first, second):
    if len(first) != len(second):
        raise ValueError('the length is not equal')
    distance = 0
    for i in xrange(len(first)):
        if first[i] != second[i]:
            distance += 1
    return distance
