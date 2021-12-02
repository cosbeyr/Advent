def read_data(filename, typ='none'):
    ''' Read in and clean provided data
        filename: file containing line-delimited data
        typ: [none - remove white space
              int  - extract integers
              tup  - extract strings and integers]'''
    with open(filename, 'r') as f:
        data = [d.strip() for d in f.readlines()]

    if typ == 'int':
        data = [int(d) for d in data]
    if typ == 'tup':
        data = [d.split(' ') for d in data]
        data = [(d[0], int(d[1])) for d in data]

    return data

