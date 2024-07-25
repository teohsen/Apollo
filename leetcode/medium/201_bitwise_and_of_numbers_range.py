class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """
        CHATGPT

        :param left:
        :param right:
        :return:
        """
        count = 0
        # Find the common prefix of left and right in binary representation
        while left != right:
            left >>= 1
            right >>= 1
            count += 1
        # Left shift the common prefix to restore the result
        return left << count