from utils import read_data

def spawn(fish, days):
    if days <= 0:
        return 1
    if fish == 0:
        return spawn(0, days-7) + spawn(0, days-9)
    return spawn(0, days-fish)

def day06_1(data, days):
    return sum([spawn(fish, days) for fish in data])

def main():
    data = read_data('./data/day06.txt', typ='bingo')[0]

    # PART ONE
    print(day06_1(data, 80))

    # PART TWO
    print(day06_1(data, 256))

if __name__ == '__main__':
    main()
