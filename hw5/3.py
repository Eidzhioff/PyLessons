import statistics
lst=[1, 5, 6.3, 6, None, 2.0, -4, None]
for i in range(len(lst)):
    if lst[i]==None:
        lst[i] = 0
sa=round(statistics.mean(lst))
for i in range(len(lst)):
    if lst[i]==0:
        lst[i] = sa
print(lst)
