"""
Parsa Yahoie 610395157
AmirHossein Ebrahimi 610395070
--------------------------------------------------------------------------------
Problem [# http://rosalind.info/problems/ksim/]
Given: A positive integer k (k≤50), a DNA string s of length at most 5 kbp representing a motif, and a DNA string t of length at most 50 kbp representing a genome.

Return: All substrings t′ of t such that the edit distance dE(s,t′) is less than or equal to k. Each substring should be encoded by a pair containing its location in t followed by its length.
--------------------------------------------------------------------------------
Sample Dataset
2
ACGTAG
ACGGATCGGCATCGT

Sample Output
1 4
1 5
1 6
"""

# h_ed = hjelmqvist_levenshtein_edit_distance
def h_ed(s_1, s_2):
    """
    A fast and memory efficient implementation by Hjelmqvist, Sten
    """
    # let s_1, s_2 be two not empty string
    if (not s_1 or not s_2):
        raise ValueError

    # Basis
    if s_1 == s_2:
        return 0
    if len(s_1) == 0:
        return len(s_2)
    if len(s_2) == 0:
        return len(s_1)

    # it only needs 2 row of hole matrix in each step
    # initialize pre_row with identity row
    # this row is A[0][i]: edit distance for an empty s_1
    # the distance is just the number of characters to delete from s_2
    # current and previous row
    pre_row = [i for i in range(len(s_2) + 1)]
    cur_row = [0 for _ in range(len(s_2) + 1)]

    for i in range(len(s_1)):
        # calculate cur_row from the pre_row
        # first element of cur_row is A[i+1][0]
        # edit distance is delete s_1[i+1] to match empty s_2
        cur_row[0] = i + 1

        # use formula to fill in the rest of the row
        for j in range(len(s_2)):
            cost = 0 if s_1[i] == s_2[j] else 1
            cur_row[j + 1] = min(cur_row[j]+1, pre_row[j+1]+1, pre_row[j]+cost)

        # copy cur_row to pre_row for next iteration
        for j in range(len(s_2)+1):
            pre_row[j] = cur_row[j]

    return cur_row[len(s_2)]


def main():
    file = open("ksim_dataset.txt", "r")
    lines = file.readlines()
    k = int(lines[0])
    p = lines[1][:-1]
    t = lines[2][:-1]
    print(k, p, t)

    for i in range(len(t)):
        for j in range(i + len(p) - k, min(i + len(p) + k, len(t)+1)):
            d = h_ed(p, t[i:j])
            if d <= k:
                print(i+1, j - i)


if __name__ == '__main__':
    main()
