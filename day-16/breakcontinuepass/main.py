# Day - 16 Break , continue , pass

# break ka mtlb ye hai ki jaise hi wo condition hit kiya uske baad loop ni chalega in short wo break ho jaegaz
for i in range(1,11):
    if i == 5:
        break
    print(i)

# continue ka mtlb ye hai ki wo loop skip ho jaega
for i in range(1,11):
    if i == 5:
        continue
    print(i)

# pass mtlb ki abhi tm define kr diye but tmko idea ni hai ki ye kaise implement hoga toh uske liye pass mtlb ki hmhi aise hi chor rhe hai baad me aake likh dege


for i in range(1,11):
    pass