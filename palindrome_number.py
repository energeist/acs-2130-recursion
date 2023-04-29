def palindrome_integer(number):
    strnum = str(number)
    print(strnum)
    if len(strnum) == 1 or (len(strnum) == 2 and strnum[0] == strnum[1]):
        return f"The number is a palindrome"
    if strnum[0] == strnum[-1]:
        return palindrome_integer(strnum[1:-1])
    return "The number is not a palindrome"

print(palindrome_integer(1234321))
print(palindrome_integer(12341234))