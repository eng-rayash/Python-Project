x=10

def change():
    x=5
    print(x)

change()
print(x)


double = lambda n: n*2
print(double(4))

students = [{"name":"Ali","grade":85},{"name":"sara","grade":90}]

best = max(students, key=lambda s: s["grade"])
print(best["name"])

ranked= sorted(students, key=lambda s: s["grade"], reverse=True )