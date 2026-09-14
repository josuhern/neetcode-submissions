class Solution:
    def calPoints(self, operations: List[str]) -> int:
        my_score = []
        for op in operations:
            if op == "+":
                add = int(my_score[-1]) + int(my_score[-2])
                my_score.append(add)
            elif op == "C":
                my_score.pop()
            elif op == "D":
                double = int(my_score[-1]) * 2
                my_score.append(double)
            else:
                my_score.append(int(op))
        return sum(my_score)
