# @lc app=leetcode id=2409 slug=count-days-spent-together lang=python3
#
# [2409] Count Days Spent Together
# Difficulty: Easy
# Tags: Math, String
# URL: https://leetcode.com/problems/count-days-spent-together/
#
# @lc code=start
DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        def date2days(date):
            #-1 since DAYS_IN_MONTH is 0 indexed and month is 1-indexed
            month = int(date[:2]) -1
            result = 0
            for i in range(len(DAYS_IN_MONTH)):
                if i == month:
                    break
                result += DAYS_IN_MONTH[i]
            
            result += int(date[-2:]) -1
            return result 
        
        print(date2days(arriveAlice))
        print(date2days(leaveAlice))

        start = max(arriveAlice, arriveBob)
        end = min(leaveAlice, leaveBob)

        if end < start:
            return 0
        
        return date2days(end) - date2days(start) + 1


        

# @lc code=end

if __name__ == "__main__":
    li = ["a", "b", "c", "d", "e", "f", "g"]

    print("Original list:", li)
    print("Indices:       ", list(range(len(li))))
    print()

    print(f"{li=}")
    print(f"{li[2:]=}")
    print(f"{li[2:5]=}")
    print(f"{li[::2]=}")
    print(f"{li[1::2]=}")
    print(f"{li[:3]=}")
    print(f"{li[-3:]=}")
    print(f"{li[:-1]=}")
    print(f"{li[::-1]=}")
    print(f"{li[:]=}")
    print(f"{li[1:6:2]=}")