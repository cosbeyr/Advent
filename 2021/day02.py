from utils import read_data

def day02_1(data):
    ''' Compute depth and horizontal position
        down and up: add to or subtract from depth, respectively
        forward:     add to horizontal position'''
    depth = sum([amt if com == 'down' else -amt for com, amt in data if com != 'forward'])
    horizontal = sum([amt for com, amt in data if com == 'forward'])
    return depth * horizontal

def day02_2(data):
    ''' Compute aim, depth and horizontal position
        down and up: add or subtract from aim, respectively
        forward:     add to horizontal position
                     multiply by current aim and add to depth'''
    aim, depth, horizontal = 0, 0, 0
    for direction, amount in data:
        if direction == 'down':
            aim += amount
        if direction == 'up':
            aim -= amount
        if direction == 'forward':
            depth += amount * aim
            horizontal += amount
    return depth * horizontal

def main():
    data = read_data('./data/day02.txt', typ='tup')
   
    # PART ONE 
    print(day02_1(data))

    # PART TWO
    print(day02_2(data))

if __name__ == '__main__':
    main()
