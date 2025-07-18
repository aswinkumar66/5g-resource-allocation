def stoi(str):
            if str == "I":
                return 1
            elif str == "X":
                return 10
            elif str == "V":
                return 5
            elif str == "L":
                return 50
            elif str == "C":
                return 100
            elif str == "D":
                return 500
            elif str == "1000":
                return 1000
def romanToInt(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            result+=stoi(s[i])
        return result

str = "XL"
print(romanToInt(str))