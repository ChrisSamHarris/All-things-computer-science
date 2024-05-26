def calPoints(operations):
    """
    :type operations: List[str]
    :rtype: int
    """
    score_sheet = []
    ss_i = 0

    for i in operations:
        try:
            if int(i):
                score_sheet.append(int(i))
                ss_i += 1
        except: 
            if i == "+":
                score_sheet.append(score_sheet[ss_i-1] + score_sheet[ss_i -2])
                ss_i += 1 
            elif i == "C":
                score_sheet.pop()
                ss_i -= 1 
            elif i == "D":
                num = score_sheet[ss_i-1] 
                score_sheet.append(num*2)
                ss_i += 1
    
    return sum(score_sheet)

print(calPoints(["5","2","C","D","+"]))

def calPointsB(operations):
    """
    :type operations: List[str]
    :rtype: int
    """
    stack = []

    for op in operations:
        if op == "+":
            stack.append(stack[-1] + stack[-2])
        elif op == "C":
            stack.pop()
        elif op == "D":
            stack.append(stack[-1] * 2)
        else:
            stack.append(int(op))
            
    return sum(stack)

print(calPointsB(["5","2","C","D","+"]))