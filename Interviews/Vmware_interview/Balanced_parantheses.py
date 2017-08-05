def isBalanced_Parantheses(string):
    if len(string) == 0:
        return False
    if len(string) % 2 != 0:
        return False
    opening_set = set('({[')
    match_set = set([('(',')'), ('{','}'),('[',']')])
    output = []
    for char in string:
        if char in opening_set:
            output.append(char)
        else:
            if len(output) == 0:
                return False
            last_opened = output.pop()
            if (last_opened, char) not in match_set:
                return False
    return len(output) == 0
    
#print isBalanced_Parantheses('((')
#print isBalanced_Parantheses(']]')
#print isBalanced_Parantheses('“]][[“')
print isBalanced_Parantheses('((()(()){([()])}))')
#print isBalanced_Parantheses('{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}[[[[[[[]]]]]]]]]]')
#print isBalanced_Parantheses('1263%#@&')
