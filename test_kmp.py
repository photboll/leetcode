import pytest

# ------------------------------------------------------------------
# Main KMP search test cases
# Interface:
#   kmp_search(text: str, pattern: str) -> List[int]
# ------------------------------------------------------------------

@pytest.mark.parametrize("text, pattern, expected", [
    # --------------------------------------------------------------
    # 1. Basic correctness
    # --------------------------------------------------------------
    ("hello world", "world", [6]),
    ("abcdef", "abc", [0]),
    ("abcdef", "def", [3]),
    ("abcdef", "gh", []),

    # --------------------------------------------------------------
    # 2. Multiple matches
    # --------------------------------------------------------------
    ("aaaaa", "aaa", [0, 1, 2]),          # overlapping
    ("abcabcabc", "abc", [0, 3, 6]),      # repeated
    ("pattern", "pattern", [0]),

    # --------------------------------------------------------------
    # 3. Prefix–suffix stress cases (KMP critical)
    # --------------------------------------------------------------
    ("abababab", "abab", [0, 2, 4]),
    ("ababcababcab", "ababcab", [0, 5]),
    ("aaabaaabaaabaaab", "aaabaaab", [0, 4, 8]),

    # --------------------------------------------------------------
    # 4. Pattern longer than text
    # --------------------------------------------------------------
    ("short", "longerpattern", []),

    # --------------------------------------------------------------
    # 5. Single-character patterns
    # --------------------------------------------------------------
    ("aaaaa", "a", [0, 1, 2, 3, 4]),
    ("abcde", "e", [4]),
    ("abcde", "f", []),

    # --------------------------------------------------------------
    # 6. Special characters & spacing
    # --------------------------------------------------------------
    ("a man, a plan, a canal", "a ", [0, 7, 15]),
    ("AbcABCabc", "abc", [6]),  # case-sensitive

    # --------------------------------------------------------------
    # 7. Stress / performance sanity checks
    # --------------------------------------------------------------
    ("a" * 10000 + "b", "a" * 9999 + "b", [1]),
    ("a" * 10000, "a" * 5000 + "b", []),
])
def test_kmp_search(text, pattern, expected):
    from KMP import kmp_search 
    assert kmp_search(text, pattern) == expected


# ------------------------------------------------------------------
# Empty pattern behavior
# ------------------------------------------------------------------

def test_empty_pattern_matches_everywhere():
    from KMP import kmp_search
    assert kmp_search("abc", "") == [0, 1, 2, 3]
    assert kmp_search("", "") == [0]


# If empty pattern should be invalid, use this instead:
#
# def test_empty_pattern_invalid():
#     from your_module import kmp_search
#     with pytest.raises(ValueError):
#         kmp_search("abc", "")


# ------------------------------------------------------------------
# Optional: LPS (prefix table) unit tests
# Only include if you expose LPS computation
# ------------------------------------------------------------------

@pytest.mark.parametrize("pattern, expected_lps", [
    ("ababaca", [0, 0, 1, 2, 3, 0, 1]),
    ("aaaa",    [0, 1, 2, 3]),
    ("abcab",   [0, 0, 0, 1, 2]),
    ("aabaac",  [0, 1, 0, 1, 2, 0]),
])
def test_lps(pattern, expected_lps):
    from KMP import compute_lps
    assert compute_lps(pattern) == expected_lps
