N=1260

last = N
coin_type = [500, 100, 50, 10]
count = 0
for i in coin_type:
    count += last//i
    last = last%i #(last//i)*i

print(count)
#책과 같은 풀이