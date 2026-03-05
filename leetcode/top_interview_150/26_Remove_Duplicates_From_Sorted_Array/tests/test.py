import pytest

@pytest.mark.parametrize("nums, expected_nums, expected_k", [
        ([1, 1, 2], [1, 2], 2),
            ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4], 5),
                ([1, 2, 3], [1, 2, 3], 3),
                    ([1, 1, 1, 1, 1], [1], 1),
                        ([5], [5], 1),
                        ])
def test_removeDuplicates(solution, nums, expected_nums, expected_k):
        k = solution.removeDuplicates(nums)
            assert k == expected_k
                for i in range(k):
                            assert nums[i] == expected_nums[i]

