class Solution:
    def rob(self, nums: list[int]) -> int:
        # In this case its always two possibilities to get start
        rob1, rob2 = 0, 0

        for n in nums:
            # Getting the max of one neighbor before max value + current value or
            # current max values
            temp = max(
                n + rob1,
                rob2
            )
            # Storing the previous max value to rob1
            rob1 = rob2
            # saving the cur max value to rob2
            rob2 = temp
        # since rob2 has the largest value stored
        return rob2
        