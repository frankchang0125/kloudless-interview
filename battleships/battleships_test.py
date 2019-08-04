from battleships import solution


def test_solution():
    assert solution(4, "1B 2C,2D 4D", "2B 2D 3D 4D 4A") == "1,1"
    assert solution(3, "1A 1B,2C 2C", "1B") == "0,1"
    assert solution(12, "1A 2A,12A 12A", "12A") == "1,0"
    assert solution(4, "1B 2C,2D 4D", "2B 2D 3D 4D 4A") == "1,1"
    assert solution(3, "1A 1B,2C 2C", "1B") == "0,1"
    assert solution(12, "1A 2A,12A 12A", "12A") == "1,0"
    assert solution(12, "1A 2A,12A 12A", "1A 12A") == "1,1"
    assert solution(12, "1A 2A,12A 12A", "1A 2A") == "1,0"
    assert solution(12, "1A 2A,12A 12A", "1A") == "0,1"
    assert solution(12, "1A 2A,12A 12A", "1A 2A 12A") == "2,0"
    assert solution(12, "", "1A 2A 12A") == "0,0"
    assert solution(12, "1A 2A,12A 12A", "") == "0,0"
