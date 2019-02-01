In computational linguistics and computer science, `edit distance` is a way of quantifying how dissimilar two strings (e.g., words) are to one another by counting the minimum number of operations required to transform one string into the other.
#USECASES
Edit distances find applications in `natural language processing` `automatic spelling correction`
The `Levenshtein distance` operations are the removal, insertion, or substitution of a character in the string. Being the most common metric, the Levenshtein distance is usually what is meant by "edit distance"
In Levenshtein's original definition, each of these operations has unit cost (except that substitution of a character by itself has zero cost), so the Levenshtein distance is equal to the `minimum number of operations required to transform a to b`.

In information theory, the `Hamming distance` between two strings of equal length is the `number of positions at which the corresponding symbols are different`. In other words, it measures the `minimum number of substitutions required` to change one string into the other, or the minimum number of errors that could have transformed one string into the other

```python
def hamming_distance(s1, s2):
    """Return the Hamming distance between equal-length sequences"""
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(el1 != el2 for el1, el2 in zip(s1, s2))
```
```java
    /*Levenshtein_distance a,b(|a|, |b|)*/
    Levenshtein_distance = min(i, j) == 0 ? max(i, j) : min(
            Levenshtein_distance(i - 1, j) + 1,
            Levenshtein_distance(i, j - 1) + 1,
            Levenshtein_distance(i - 1, j - 1) + 1, //(ai != bj)
        )
```