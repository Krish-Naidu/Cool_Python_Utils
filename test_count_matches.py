import pytest
from count_matches import count_matches


def test_all_matches():
    """Test when all numbers above threshold have binary 1"""
    numbers = [10, 20, 30, 40]
    binary_string = "1111"
    threshold = 5
    assert count_matches(numbers, binary_string, threshold) == 4


def test_no_matches():
    """Test when no numbers meet both conditions"""
    numbers = [10, 20, 30, 40]
    binary_string = "0000"
    threshold = 5
    assert count_matches(numbers, binary_string, threshold) == 0


def test_mixed_conditions():
    """Test with mixed conditions"""
    numbers = [10, 25, 3, 45, 8, 12, 30, 5]
    binary_string = "11010101"
    threshold = 15
    assert count_matches(numbers, binary_string, threshold) == 2


def test_threshold_boundary():
    """Test numbers exactly at threshold"""
    numbers = [10, 15, 20, 25]
    binary_string = "1111"
    threshold = 15
    assert count_matches(numbers, binary_string, threshold) == 2  # Only 20 and 25


def test_all_below_threshold():
    """Test when all numbers are below threshold"""
    numbers = [1, 2, 3, 4]
    binary_string = "1111"
    threshold = 10
    assert count_matches(numbers, binary_string, threshold) == 0


def test_single_element():
    """Test with single element arrays"""
    numbers = [20]
    binary_string = "1"
    threshold = 10
    assert count_matches(numbers, binary_string, threshold) == 1


def test_alternating_pattern():
    """Test with alternating binary pattern"""
    numbers = [20, 30, 40, 50]
    binary_string = "1010"
    threshold = 10
    assert count_matches(numbers, binary_string, threshold) == 2
