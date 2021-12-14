import numpy as np

def read_data(filename, typ='none'):
    ''' Read in and clean provided data
        filename: file containing line-delimited data
        typ: [none - remove white space
              int  - extract integers
              tup  - extract strings and integers]'''

    if typ == 'bingo':
        with open(filename, 'r') as f:
            data = f.read().strip()

        data = data.split('\n\n')
        numbers = [int(d) for d in data[0].split(',')]
        boards = np.array([np.array([n.split() for n in d.split('\n')]) for d in data[1:]]).astype(int)
        return numbers, boards

    with open(filename, 'r') as f:
        data = [d.strip() for d in f.readlines()]

    if typ == 'coords':
        data = [d.split(' -> ') for d in data]
        data = [[coord.split(',') for coord in d] for d in data]
        data = np.array(data, dtype='int').reshape(len(data), 4)

    if typ == 'int':
        data = [int(d) for d in data]
    if typ == 'tup':
        data = [d.split(' ') for d in data]
        data = [(d[0], int(d[1])) for d in data]
    if typ == 'comma':
        data = data.split(',')
    return data

