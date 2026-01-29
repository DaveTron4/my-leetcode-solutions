class Solution:
    def intToRoman(self, num: int) -> str:
        symList = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10], ["XL", 40], ["L", 50], ["XC", 90], ["C", 100], ["CD", 400],["D", 500],["CM", 900],["M", 1000]]

        result = []

        for i in range(len(symList) - 1, -1, -1):
            div = num // symList[i][1]
            
            if div > 0:
                result.append(f"{symList[i][0] * div}")

            num = num % symList[i][1]

        return "".join(result)