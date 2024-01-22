
def pre_active(a, w, b):
    result = []
    final = []
    for i,j in zip(a,w):
        n = i * j
        result.append(n)
    z = sum(result) + b 
    final.append(z)
    return final 