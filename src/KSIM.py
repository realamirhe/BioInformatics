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


def edit_distance():
    pass


def main():
    file = open("test.txt", "r")
    lines = file.readlines()
    k = int(lines[0])
    motif = lines[1]
    dna = lines[2]

    for i in range(len(dna)):
        for j in range(i, len(dna)):
            d = edit_distance(motif, dna[i:j+1])
            if d <= k:
                print(i, j)


if __name__ == '__main__':
    main()
