import pytest
from Solution import Solution

def test_removeDuplicates():
    # Test case 1: Example from README
    nums = [1, 1, 2]
    expected_nums = [1, 2]
    k = Solution().removeDuplicates(nums)
    assert k == len(expected_nums)
    for i in range(k):
        assert nums[i] == expected_nums[i]

    # Test case 2: Example from README
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    expected_nums = [0, 1, 2, 3, 4]
    k = Solution().removeDuplicates(nums)
    assert k == len(expected_nums)
    for i in range(k):
        assert nums[i] == expected_nums[i]

    # Test case 3: No duplicates
    nums = [1, 2, 3]
    expected_nums = [1, 2, 3]
    k = Solution().removeDuplicates(nums)
    assert k == len(expected_nums)
    for i in range(k):
        assert nums[i] == expected_nums[i]

    # Test case 4: All duplicates
    nums = [1, 1, 1, 1, 1]
    expected_nums = [1]
    k = Solution().removeDuplicates(nums)
    assert k == len(expected_nums)
    for i in range(k):
        assert nums[i] == expected_nums[i]

    # Test case 5: Single element
    nums = [5]
    expected_nums = [5]
    k = Solution().removeDuplicates(nums)
    assert k == len(expected_nums)
    for i in range(k):
        assert nums[i] == expected_nums[i]
