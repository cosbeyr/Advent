from utils import read_data

def day01(data):
    ''' Count number of times depth increases from previous '''
    return sum([curr > prev for prev, curr in zip(data, data[1:])])

def day01_aux(data):
    ''' Compute three-measurment sliding window of the depths '''
    return [sum(three) for three in zip(data, data[1:], data[2:])]

def main():
    data = read_data('./data/day01.txt', typ='int')

    # PART ONE
    print(day01(data))

    # PART TWO
    data2 = day01_aux(data)
    print(day01(data2))

if __name__ == '__main__':
    main()
