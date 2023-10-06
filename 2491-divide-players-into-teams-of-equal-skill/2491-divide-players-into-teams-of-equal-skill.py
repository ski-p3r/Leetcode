class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        right = len(skill)-1

        target_sum = skill[0] + skill[-1]
        l = len(skill)
        chemistry = 0
        for i in range(l//2):
            if skill[i] + skill[l-1-i] != target_sum:
                return -1
            chemistry += skill[i] * skill[l-1-i]
        return chemistry