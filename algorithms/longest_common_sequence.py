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

if __name__ == '__main__':
    import doctest
    doctest.testmod()
