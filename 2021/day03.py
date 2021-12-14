from utils import read_data

def day03_1(data):
    majority, length = len(data) / 2, len(data[0])
    data = [len([d[i] for d in data if d[i] == '1']) for i in range(length)]
    
    gamma = ''.join(['1' if d > majority else '0' for d in data])
    epsilon = ''.join(['1' if g == '0' else '0' for g in gamma])

    return int(gamma, 2) * int(epsilon, 2)


def day03_2(data, idx=0, high=True):
    if len(data) == 1:
        return int(data[0], 2)

    curr = [d[idx] for d in data]
    zeros = [i for i, n in enumerate(curr) if n == '0']
    ones = [i for i, n in enumerate(curr) if n == '1']

    p1, p2 = (zeros, ones) if len(zeros) > len(ones) else (ones, zeros)
    p = p1 if high else p2

    return day03_2([data[i] for i in p], idx=idx+1, high=high)


def main():
    data = read_data('./data/day03.txt')

    # PART ONE
    print(day03_1(data))

    # PART TWO
    print(day03_2(data) * day03_2(data, high=False))

if __name__ == '__main__':
    main()
