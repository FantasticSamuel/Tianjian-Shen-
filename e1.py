s = input().lower()
source, target = input().lower().split()
ns = s.replace(source, target).lower()
#print(ns)
*a, = ns.split('.')
a = [i.strip() for i in a if i.strip()]
result = '. '.join([i[0].upper() + i[1:] for i in a])
print(result)
