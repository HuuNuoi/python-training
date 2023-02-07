def add(*args):
    print(type(args))
    return sorted(args)

print(add(2,3,4,5,6,8))

lst =[1,2,3,4553,53,24,6,3,2]
fisrt , mid , *last = lst
print(fisrt)
print(mid)
print(last)