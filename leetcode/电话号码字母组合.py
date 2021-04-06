def phoneLetter(digits):
    if not digits:
        return []

    keyboard = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    res  = []
    le_com = []

    def backtrack(index):
        if  index == len(digits):
            res.append("".join(le_com))
        else:
            digits_s = digits[index]
            for s in keyboard[digits_s]:
                le_com.append(s)
                backtrack(index+1)
                le_com.pop()

    backtrack(0)
    return res


print(phoneLetter("293"))


def letterCombinations(digits):
    if len(digits) == 0:
        return []

    keyboard = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    res = []
    def find_com_str(index, s):
        if index == len(digits):
            res.append(s)
            return
        for c in keyboard[digits[index]]:
            find_com_str(index+1, s+c)
    find_com_str(0, "")
    return res

print(letterCombinations("23"))