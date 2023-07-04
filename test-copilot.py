def countOfOddsInRange(start, end):
    count = 0
    for i in range(start, end + 1):
        if i % 2 == 1:
            count += 1
    return count
# call the function and print the result
print(countOfOddsInRange(1, 10))

def fizzBuzz(n):
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)

print(fizzBuzz(15))

def isPalindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True

print(isPalindrome("racear"))