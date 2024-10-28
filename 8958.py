answerl = []
for i in range(int(input())):
    answer = 0
    n = 1
    for j in input():
        if j =='O':
            answer += n
            n += 1
        else:
            n = 1
    answerl.append(answer)
print(*answerl,sep='\n')
