class Solution:
    def totalMoney(self, n: int) -> int:

        total_value = 0
        current_val = 0
        week_no = 0
        for i in range(1, n+1):
            current_val += 1
            total_value = total_value + (current_val + week_no)
            if i % 7 == 0:
                current_val = 0
                week_no += 1

        return total_value

    def totalMoney2(self, n: int) -> int:
        total_money = 0
        curr_val = 0

        for i in range(1, n+1):
            curr_val = n//7 + 1 if i%7 == 1 else curr_val+1
            total_money += curr_val

        return total_money