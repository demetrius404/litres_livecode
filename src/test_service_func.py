import pytest
from solution import build_str
from solution import processing

test_case_0 = [
    pytest.param([], 1, "", id="case_0"),
    pytest.param(["x"], 1, "x", id="case_1"),
    pytest.param(["b", "a"], 1, "ab", id="case_2"),
    pytest.param(["b", "a"], 2, "abab", id="case_3"),
    pytest.param(["b", "a"], 3, "ababab", id="case_4"),
]

test_case_1 = [
    pytest.param([1], "", 0,  id="case_0"),
    pytest.param([3, "a"], "aaa", 0,  id="case_1"),
    pytest.param([1, "", 2, "a", "b"], "abab", 2, id="case_2")
]


@pytest.mark.parametrize("char_list, multiplier, expect", test_case_0)
def test_build_str_0(char_list, multiplier, expect):
    assert build_str(char_list, multiplier) == expect


@pytest.mark.parametrize("stack, expect, expect_len", test_case_1)
def test_processing_0(stack, expect, expect_len):
    assert processing(stack) == expect
    assert len(stack) == expect_len
