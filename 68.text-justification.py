#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#

# @lc code=start
def required_spaces(words):
    """ 
    How many space is required to make a sentence out of the words.
    Every two words needs atelast one space between them.
    """
    return max(len(words) -1, 0)

def left_justify_line(words, width):
    line = " ".join(words)
    return f"{line:{' '}<{width}}"
    
def full_justify_line(words, width, num_chars=None):
    """
    Pads the words with spaces so that they reach the given width 
    the padding is apllied as evenly as possible between the words.
    i.e. no two gaps between words ever differ by more than 1
    """
    if not None:
        #optionallly you can supply the total number of chars in the words
        #if not supplied wi simply compute them
        num_chars = sum(map(len, words))
    
    spaces = width - num_chars
    if spaces < required_spaces(words):
        raise ValueError(f"The number of chars exceeds the width can't add negative padding")
    
    spaces_per_gap, gaps_with_extra = divmod(spaces, len(words) -1)
    small_gap = " "*spaces_per_gap
    if gaps_with_extra == 0:
        return small_gap.join(words)
    big_gap = small_gap + " "
    return big_gap.join(words[:gaps_with_extra]) +big_gap+small_gap.join(words[gaps_with_extra:])

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        #The extra spaces need to be evenly divided among the wrods on a line
        result = []
        words.reverse()
        cur_line = []
        num_chars = 0
        while words:
            cur_word = words.pop()
            word_len = len(cur_word)
            #The current word can't fit into this line
            if num_chars + required_spaces(cur_line) + word_len >= maxWidth :
                #We have to start a new line 
                #First add the curent line to the result, don't add empty lines
                if len(cur_line) == 1:
                    result.append(left_justify_line(cur_line, maxWidth))
                elif len(cur_line) > 1:
                    result.append(full_justify_line(cur_line, maxWidth))
                    
                #Second start the new line with the current word
                cur_line.clear()
                num_chars = 0
            
            if word_len == maxWidth:
                result.append(cur_word)
                num_chars = 0
                continue

            cur_line.append(cur_word)
            num_chars += word_len
    
    
        if len(cur_line) > 0:
            result.append(left_justify_line(cur_line, maxWidth))
        return result
        
# @lc code=end

