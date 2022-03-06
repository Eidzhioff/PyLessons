import statistics
lst=list(map(int,input().split()))
Min=min(lst)
Max=max(lst)
im=lst.index(Max)
imn=lst.index(Min)
if imn + 1 < im:
    sa=statistics.mean(lst[imn+1:im])
    print("Среднее арифметическое", sa)
elif imn + 1 > im:
    med=statistics.median(lst[im:imn])
    for x in range(im+1,imn):
        lst[x]=med
    print("Замена на медиану",lst)
