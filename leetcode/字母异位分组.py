class Soultion():

    def groupAnagrams(self, array):

        dict_tmp = {}
        for i in array:
            t = "".join(sorted(i))
            if t in dict_tmp:
                dict_tmp[t].append(i)
            else:
                dict_tmp[t] = [i]
        return list(dict_tmp.values())


group_anagrams_ins = Soultion()
print(group_anagrams_ins.groupAnagrams(["tea", "eta", "ring"]))
