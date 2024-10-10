class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map_a = {}

        word_list = s.split(' ')
        if len(word_list) != len(pattern):
            return False
        map_b = {}

        for i in range(len(pattern)):
            if pattern[i] not in map_a:
                map_a[pattern[i]] = word_list[i]
            else:
                if map_a[pattern[i]] != word_list[i]:
                    return False

            if word_list[i] not in map_b:
                map_b[word_list[i]] = pattern[i]
            else:
                if map_b[word_list[i]] != pattern[i]:
                    return False

            
        return True
        