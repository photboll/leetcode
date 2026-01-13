

def compute_lps(pattern):
    """
    Longest Proper prefix which is also a suffix
    """
    m = len(pattern)
    lps = [0] * m
    j = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                lps[i] = 0
                i += 1
    return lps
    

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)

    if pattern == "":
        return [i for i in range(n+1)]
    lps = compute_lps(pattern)
    matches = []
    i = j = 0

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
            if j == m:
                matches.append(i - j)
                j = lps[j-1]
        else:
            if i < n and pattern[j] != text[i]:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
            else:
                i += 1

    return matches

if __name__ == "__main__":
    pass
