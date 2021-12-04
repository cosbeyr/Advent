from utils import read_data

def day03_1(data):
    majority, length = len(data) / 2, len(data[0])
    data = [len([d[i] for d in data if d[i] == '1']) for i in range(length)]
    
    gamma = ''.join(['1' if d > majority else '0' for d in data])
    epsilon = ''.join(['1' if g == '0' else '0' for g in gamma])

    return int(gamma, 2) * int(epsilon, 2)

def main():
    data = read_data('./data/day03.txt')

    # PART ONE
    print(day03_1(data))

    # PART TWO


if __name__ == '__main__':
    main()
