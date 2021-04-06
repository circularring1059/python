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
        "9": "wzyz"
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