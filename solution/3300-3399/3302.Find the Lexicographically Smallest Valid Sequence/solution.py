from typing import List

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n = len(word1)
        m = len(word2)

        # last[j] = latest possible index in word1
        # where word2[j] can be matched while still
        # matching word2[j+1:] after it.
        last = [-1] * m

        i = n - 1
        j = m - 1

        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1
            i -= 1

        ans = []
        j = 0
        can_change = True

        for i in range(n):
            if j == m:
                break

            # Exact match: always take the earliest possible index.
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            # Use our one allowed modification.
            elif can_change:
                # After choosing i as the mismatching character,
                # word2[j+1:] must be matchable after i.
                if j == m - 1 or i < last[j + 1]:
                    ans.append(i)
                    j += 1
                    can_change = False

        return ans if j == m else []
