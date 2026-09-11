class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_count = 0
        curr_word = ""
        for c in s:
            if c.isdigit():
                curr_count = curr_count * 10 + int(c)
            elif c == "[":
                stack.append((curr_word,curr_count))
                curr_count = 0
                curr_word = ""
            elif c == "]":
                prev_word,prev_count = stack.pop()
                curr_word = prev_word + curr_word * prev_count
            else:
                curr_word = curr_word + c
        return curr_word   