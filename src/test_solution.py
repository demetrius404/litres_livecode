import pytest
from solution import solution

test_case = [
    pytest.param("", "", id="case_0"),
    pytest.param("[]", "", id="case_1"),
    pytest.param("ab", "ab", id="case_2"),
    pytest.param("[ab]", "ab", id="case_3"),
    pytest.param("2[aaa]", "aaaaaa", id="case_4"),
    pytest.param("ab[cd]e", "abcde", id="case_5"),
    pytest.param("ab3[cd]e", "abcdcdcde", id="case_6"),
    pytest.param("a2[b3[cd]]", "abcdcdcdbcdcdcd", id="case_7"),
    pytest.param("a2[b2[xx]y]", "abxxxxybxxxxy", id="case_8"),
    pytest.param("2[b2[xx]y]", "bxxxxybxxxxy", id="case_9"),
    pytest.param("2[aa2[yy]2[x]]", "aayyyyxxaayyyyxx", id="case_10"),
    pytest.param("4[2[[ab]]]", "abababababababab", id="case_11"),
    pytest.param("ab3[c2c[q]d]", "abc2cqdc2cqdc2cqd", id="case_12")
]


@pytest.mark.parametrize("source, expect", test_case)
def test_solution_0(source, expect):
    assert solution(source) == expect
