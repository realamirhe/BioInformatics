"""
Parsa Yahoie 610395157
AmirHossein Ebrahimi 610395070
--------------------------------------------------------------------------------
Problem
Say that we have two strings s and t of respective lengths m and n and an alignment score. Let's define a matrix M corresponding to s and t by setting Mj,k equal to the maximum score of any alignment that aligns s[j] with t[k]. So each entry in M can be equal to at most the maximum score of any alignment of s and t.

Given: Two DNA strings s and t in FASTA format, each having length at most 1000 bp.

Return: The maximum alignment score of a global alignment of s and t, followed by the sum of all elements of the matrix M corresponding to s and t that was defined above. Apply the mismatch score introduced in “Finding a Motif with Modifications”.
--------------------------------------------------------------------------------
Sample Dataset
>Rosalind_35
ATAGATA
>Rosalind_5
ACAGGTA

Sample Output
3
-139
"""

GAP, MATCH, MISMATCH = -1, 1, -1

def parse_fasta(path):
    sequences = []
    with open(path, 'r') as file:
        for line in file.readlines():
            if line.startswith('>'):
                sequences.append('')
            else:
                sequences[-1] += line.strip()
    if len(sequences) > 1:
        return sequences
    else:
        return sequences[0]

def global_alignment(s, t):
    alignment_matrix = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]

    for i in range(1, len(s)+1):
        alignment_matrix[i][0] = GAP * i
    for j in range(1, len(t)+1):
        alignment_matrix[0][j] = GAP * j

    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            alignment_matrix[i][j] = max([alignment_matrix[i - 1][j - 1] + (MISMATCH, MATCH)[s[i - 1] == t[j - 1]],
                           alignment_matrix[i - 1][j] + GAP,
                           alignment_matrix[i][j - 1] + GAP])

    return alignment_matrix



def alignment(s, t):
    best_score, total_score = -1 * len(s + t), 0

    preffix_matrix = global_alignment(s, t)
    suffix_matrix = global_alignment(s[::-1], t[::-1])

    for i in range(len(s)):
        for j in range(len(t)):
            score = sum((preffix_matrix[i][j],
                        (MISMATCH, MATCH)[s[i] == t[j]],
                        suffix_matrix[len(s) - 1 - i][len(t) - 1 - j]))

            total_score += score

            if best_score < score:
                best_score = score

    return best_score, total_score


def main():

    s, t = parse_fasta('osym_dataset.txt')
    print(" ".join(map(str, alignment(s, t)))) # the highest score, sum of all scores

if __name__ == '__main__':
    main()