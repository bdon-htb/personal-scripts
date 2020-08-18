def lcs_length(s1: str, s2: str) -> int:
    """Calculate the length of the longest common subsequence between s1 and s2.
    """
    if len(s1) == 0 or len(s2) == 0:
        return 0
    elif s1[-1] == s2[-1]:
        return 1 + lcs(s1[:-1], s2[:-1])
    else:
        return max(lcs(s1, s2[:-1]), lcs(s1[:-1], s2))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
