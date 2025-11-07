from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []
        for i in range(1, n + 1):
            if i % 3 == 0:
                if i % 5 ==0:
                    output.append("FizzBuzz")
                else:
                    output.append("Fizz")
            elif i % 5 == 0:
                output.append("Buzz")
            else:
                output.append(str(i))
        return output

if __name__ == "__main__":
    n_1 = 3
    n_2 = 5
    n_3 = 15

    s = Solution()
    o = s.fizzBuzz(n_3)
    print(o)
