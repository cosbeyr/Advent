import sys

def day1(data):
    ''' Count number of times depth increases from previous '''
    return sum([curr > prev for prev, curr in zip(data, data[1:])])

def day1_aux(data):
    ''' Compute three-measurment sliding window of the depths '''
    return [sum(three) for three in zip(data, data[1:], data[2:])]

def read_data(filename):
    ''' Read in and clean provided data
        filename: file containing line-delimited integers '''
    with open(filename, 'r') as f:
        data = [int(d.strip()) for d in f.readlines()]
    return data


def main():
    try:
        depths = read_data(sys.argv[1])
    except:
        print('Error: Please supply depth data file')
        return

    # Day One - Parts 1 & 2
    print(day1(depths))
    depths_three = day1_aux(depths)
    print(day1(depths_three))


if __name__ == '__main__':
    main() 
