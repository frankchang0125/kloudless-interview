from valid_braces import solution


def test_solution():
    assert solution("(){}[]") == True
    assert solution("}}}") == False
    assert solution("") == True
    assert solution("()") == True
    assert solution("[(])") == False
    assert solution("") == True
    assert solution("[[[") == False
    assert solution("[[]]") == True
    assert solution("}}}") == False
    assert solution("}[") == False
    assert solution("[") == False
