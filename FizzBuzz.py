class Solution(object):
    def fizzBuzz(self, N):
        result = ["" for _ in range(N + 1)]

        for x in range(1, N + 1):
            if x % 3 == 0 and x % 5 == 0:
                result[x] = "FizzBuzz"
            elif x % 3 == 0:
                result[x] = "Fizz"
            elif x % 5 == 0:
                result[x] = "Buzz"
            else:
                result[x] = str(x)

        return result[1:]
