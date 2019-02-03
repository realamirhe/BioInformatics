"""
Parsa Yahoie 610395157
AmirHossein Ebrahimi 610395070
--------------------------------------------------------------------------------
Problem [# http://rosalind.info/problems/rear/]
A reversal of a permutation creates a new permutation by inverting some interval of the permutation; (5,2,3,1,4), (5,3,4,1,2), and (4,1,2,3,5) are all reversals of (5,3,2,1,4). The reversal distance between two permutations π and σ, written drev(π,σ), is the minimum number of reversals required to transform π into σ (this assumes that π and σ have the same length).

Given: A collection of at most 5 pairs of permutations, all of which have length 10.

Return: The reversal distance between each permutation pair.
--------------------------------------------------------------------------------
Sample Dataset
1 2 3 4 5 6 7 8 9 10
3 1 5 2 7 4 9 6 10 8

3 10 8 2 5 4 7 1 6 9
5 2 3 1 7 4 10 8 6 9

8 6 7 9 4 1 3 10 2 5
8 2 7 6 9 1 5 3 10 4

3 9 10 4 1 8 6 7 5 2
2 9 8 5 1 7 3 4 6 10

1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10

Sample Output
9 4 5 7 0
"""
from collections import deque


def permutation_generator(sequence):
    """
    Generate all permutation of an input sequence
    using generator for memory issue
    """
    for i in range(len(sequence)):
        for j in range(i + 2, len(sequence) + 1):
            yield sequence[:i] + sequence[i:j][::-1] + sequence[j:]


def reversal_distance(per_1, per_2):
    """
    let per_1, per_2 be two permutation
    """
    # Zero Reversal distance for same permutation
    if (per_1 == per_2):
        return 0

    target = tuple(per_2)
    from_first = {tuple(per_1): 0}
    queue = deque((per_1, ))

    while len(queue):
        sequence = queue.popleft()
        cost = from_first[sequence]

        for permutation in permutation_generator(sequence):
            if permutation == target:
                return cost + 1
            if not permutation in from_first:
                from_first[permutation] = cost + 1
                if cost != 4:
                    queue.append(permutation)

    target = {tuple(per_1): 0}
    from_second = {tuple(per_2): 0}
    queue = deque((per_2, ))
    answer = 10 ** 5

    while len(queue):
        sequence = queue.popleft()
        cost = from_second[sequence]

        if cost == 4:
            break

        for permutation in permutation_generator(sequence):
            if permutation == target:
                return cost + 1
            if not permutation in from_second:
                from_second[permutation] = cost + 1
                if cost != 3:
                    queue.append(permutation)
            if permutation in from_first:
                answer = min(
                    answer, from_first[permutation] + from_second[permutation])
    return answer


def main():
    distances = []
    dataset = open("rear_dataset.txt", "r")

    lines = dataset.readlines()
    for i in range(0, len(lines), 3):
        per_1 = tuple(map(str, lines[i].split()))
        per_2 = tuple(map(str, lines[i+1].split()))

        distances.append(reversal_distance(per_1, per_2))

    print(" ".join(map(str, distances)))

if __name__ == '__main__':
    main()
