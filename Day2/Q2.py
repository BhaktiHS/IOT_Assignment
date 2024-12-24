#2) write a function to return compound interest


def comp_inter(p,t,r):
    print(f"Principle = {p}")
    print(f"Time = {t}")
    print(f"Rate = {r}")
    A = p*(pow((1+r/100),t))
    CI = A-p
    return CI

CI = comp_inter(3000,3,5)

print(f"Compound interest is : {CI}")