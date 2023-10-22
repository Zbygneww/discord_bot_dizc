import random as r

def gen_pass(pass_lengh):
    elements = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm+-/*!&$#?=@<>"
    password=""
    for i in range(pass_lengh):
        password += r.choice(elements)
        
    return password
def random_funfact():
    funfacts = [
        "George Patton(USA general) was a big Fan of Erwin Rommels book (Nazi General)",
        "Josef Stalin didn't help his son in concretation camp",
        "Simo Hayha was best sniper in history, he killed over 500 russians!",
        "San Marino and Turkey didnt sign treaty after WW1 so technicly they are still at war",
        "You can choose the name Monitor for your confirmation after the holy monitor",
        "Baby bones are very flexible, to such an extent, you can bounce a baby, like basketball!",
        "Shaquile in 2022 had more dunks, than every WNBA player combined! (Shaq had 2950, while WNBA 37)"
]

    return r.choice(funfacts)
def random_sum(a,b):
    return a + b
s = "null"
def head_or_tailss():
    global s
    printing = r.randint(1,2)
    if printing == 1:
        s = "head"
    if printing == 2:
        s = "tails"
    return s