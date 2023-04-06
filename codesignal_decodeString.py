def solution(s):  # Time: O(n) - multiple passes but still O(n) for n words/tokens in s. Space: used is the multiplication of the numbers in input string s
    stack = []; token = ""
    prev = None
    
    for char in s:
        if char.isdigit():
            if prev is None or prev.isdigit():
                token += char
            else:
                stack.append(token)
                token = char
        
        elif char == "[":
            stack.append(int(token))
            token = ""
        
        elif char == "]":
            if token:
                stack.append(token)
                token = ""
    
            word = ""
            while not type(stack[-1]) is int:
                word = stack.pop() + word  # concatenate words before number on left
            stack.append(stack.pop() * word)
        
        else:  # just an alphabet char
            token += char    
        prev = char
    
    if token:
        stack.append(token)
        token = ""
    # print stack, token
    
    return "".join(stack)
