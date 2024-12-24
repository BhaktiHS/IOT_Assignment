# 1) Write a function to return simple interest

def simp_inter(p,t,r):
    print(f"Principle = {p}")
    print(f"Time = {t}")
    print(f"Rate = {r}")
    SI = (p*t*r)/100

    return SI

SI = simp_inter(18,16,18)

print(f"Simple interest is : {SI}")




