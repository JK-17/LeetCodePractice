class Solution:
    def romanToInt(self, s: str) -> int:
        map = { 'M' : 1000, 'D' : 500, 'C' : 100, 'L' : 50, 'X' : 10, 'V' : 5, 'I': 1 }
        answer = 0

        for a, b in zip(s, s[1:]):
            if map[a] < map[b]:
                answer -= map[a]
            else:
                answer += map[a]

        return answer + map[s[-1]]