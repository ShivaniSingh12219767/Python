def largest(lst):
    r=0
    for a in range(1,len(lst)):
        if lst[a]>lst[r]:
            lst[r]=lst[a]
            r=a
    print("Largest element is",lst[r])
    print("Index of element is",r)
largest([40,8,50,100])