# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

# Example 1:

# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
# Example 2:

# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.
# Example 3:

# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.
# 1 <= k <= s.length

class Solution:
    def genera_lista_sottostringhe(self, s:str):
        n = len(s)
        sottostringhe = [s[i:j] for i in range(n) for j in range(i + 1, n + 1)]
        return sottostringhe
    
    def maxVowels(self, s: str, k: int) -> int:
        lista = self.genera_lista_sottostringhe(s)
        count = 0
        massimo = -1
        for i in range(len(lista)):
            if len(lista[i]) == k:
                count = lista[i].count('a') + lista[i].count('e') + lista[i].count('i') + lista[i].count('o') + lista[i].count('u')
                if count > massimo:
                    massimo = count
        return massimo