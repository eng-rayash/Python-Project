squares = []
for n in range(1,6):
    squares.append(n ** 2)


squares = [n ** 2 for n in range(1,6)]
evens = [n for n in range(1,11)if n%2==0]
names = [s["name"]for s in [{"name":"ALi"},{"name":"sara"}]]
print(names)

squares_dict = {n: n ** 2 for n in range (1,4)}