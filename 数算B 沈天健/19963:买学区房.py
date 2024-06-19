#2300011417 沈天健
n=int(input())
pairs = [i[1:-1] for i in input().split()]
distances = [ sum(map(float,i.split(','))) for i in pairs]
prices=list(map(float,input().split()))
values=[i/j for i,j in zip(distances,prices)]
from dataclasses import dataclass
@dataclass
class house:
    ii:int
    price:float
    value:float
houses=[]
for i in range(n):
    houses.append(house(i,prices[i],distances[i]/prices[i]))
prices.sort()
values.sort()
price_m=(prices[n//2]+prices[(n-1)//2])/2
value_m=(values[n//2]+values[(n-1)//2])/2
ans=0
for i in range(n):
    if houses[i].price<price_m and houses[i].value>value_m:
        ans+=1
print(ans)
