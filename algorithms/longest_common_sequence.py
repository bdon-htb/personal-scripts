def lcs_length(s1: str, s2: str) -> int:
    """Calculate the length of the longest common subsequence between s1 and s2.
    >>> lcs_length("", "")
    0
    >>> lcs_length("", "a")
    0
    >>> lcs_length("aaa", "a")
    1
    >>> lcs_length("abcabba", "cbabac")
    4
    """
    if len(s1) == 0 or len(s2) == 0: # Base case; if any of the strings are empty return 0.
        return 0
    elif s1[-1] == s2[-1]: # If the last characters of the strings are equal.
        return 1 + lcs_length(s1[:-1], s2[:-1])
    else: # If the last characters are not equal, compare the lcs between the other characters in string.
        return max(lcs_length(s1, s2[:-1]), lcs_length(s1[:-1], s2))

def lcs(s1: str, s2: str, O='') -> str:
    """Find the longest common subsequence between s1 and s2.
    >>> lcs("BATD", "ABDACD")
    'BAD'
    >>> lcs("BANANA", "BANANA")
    'BANANA'
    >>> lcs("", "afmgsg")
    ''
    """
    if len(s1) == 0 or len(s2) == 0:
        return O
    elif s1[-1] == s2[-1]:
        return lcs(s1[:-1], s2[:-1], s1[-1] + O)
    elif lcs_length(s1[:-1], s2) > lcs_length(s1, s2[:-1]):
        return lcs(s1[:-1], s2, O)
    else:
        return lcs(s1, s2[:-1], O)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
