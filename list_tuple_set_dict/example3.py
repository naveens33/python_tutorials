if __name__ == '__main__':
    # list of fruit names -> we need to find the vowels count in each fruit
    fruits = ['banana', 'apple', 'papaya', 'Orange']
    ans = {}
    for fruit in fruits:
        count = 0
        for c in fruit:
            if c in 'aeiou':
                count += 1
        ans[fruit] = count
    print(ans)
    li = list(ans.values())
    li.sort(reverse=True)
    d = {}
    for key in ans.keys():
        if ans[key] == li[0]:
            d[key] = ans[key]
    if len(d)!=1:
        li = list(d.keys())
        li.sort()
        print(li[0],d[li[0]])
    else:
        print(d)

