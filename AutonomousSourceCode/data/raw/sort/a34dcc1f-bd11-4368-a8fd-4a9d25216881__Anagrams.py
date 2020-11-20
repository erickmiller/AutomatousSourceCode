from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class Anagrams(LeetcodeProblem):
    def solve(self, strs):
        res = []
        record = {}
        for i, s in enumerate(strs):
            sortedS = str(sorted(list(s)))
            if sortedS in record:
                res.append(s)
                if record[sortedS] != -1:
                    res.append(strs[record[sortedS]])
                    record[sortedS] = -1
            else:
                record[sortedS] = i

        return res

    def verify(self, original_input, input, s1, s2):
        s1.sort()
        s2.sort()
        return s1 == s2

    def input(self):
        from Parser import parseStringArray
        return parseStringArray(open(self.inputPath))

    def output(self):
        from Parser import parseStringArray
        for o in parseStringArray(open(self.outputPath)):
            yield o[0]

problem = Anagrams
