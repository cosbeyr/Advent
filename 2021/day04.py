from utils import read_data
import numpy as np

def day04_1(numbers, boards, winners=[]):
    if len(winners) > 0:
        winner, n = winners[0], numbers[0]
        return np.sum(boards[winner]) * n
    
    check = lambda board: 0 in [np.sum(b) for b in board]
    boards[np.where(boards == numbers[1])] = 0
    winners = [i for i, board in enumerate(boards) if check(board)]
    winners += [i for i, board in enumerate(boards.transpose(0, 2, 1)) if check(board)]

    return day04_1(numbers[1:], boards, winners=winners)


def day04_2(numbers, boards, winners=[]):
    if len(winners) == 100:
        return np.sum(boards[winners[-1]]) * numbers[0]
    
    check = lambda board: 0 in [np.sum(b) for b in board]
    boards[np.where(boards == numbers[1])] = 0

    winners += [i for i, board in enumerate(boards) if check(board) and i not in winners]
    winners += [i for i, board in enumerate(boards.transpose(0, 2, 1)) if check(board) and i not in winners]

    return day04_2(numbers[1:], boards, winners=winners)


def main():

    # PART ONE
    numbers, boards = read_data('./data/day04.txt', typ='bingo')
    numbers = [0] + numbers
    print(day04_1(numbers, boards))

    # PART TWO
    numbers, boards = read_data('./data/day04.txt', typ='bingo')
    numbers = [0] + numbers
    print(day04_2(numbers, boards))


if __name__ == '__main__':
    main()
