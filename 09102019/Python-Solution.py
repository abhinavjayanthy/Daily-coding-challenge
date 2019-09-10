# Question :
# Given a string, return the first recurring character in it, or null if there is no recurring character.
# For example, given the string "acbbac", return "b". Given the string "abcdef", return null.


class Soultion:
    def MyRecurringChar(self, str: str) -> str:
        dic = {}
        for i in str:
            if i in dic:
                # doing this for extra! incase we want to know how may times it repeated
                dic[i] = dic[i] + 1
                return i
            else:
                dic[i] = 1
        return None


sol = Soultion()
# Test cases
print(sol.MyRecurringChar('acbbac'))
print(sol.MyRecurringChar('abcdef'))
print(sol.MyRecurringChar('aaaaaaa'))
print(sol.MyRecurringChar(''))
