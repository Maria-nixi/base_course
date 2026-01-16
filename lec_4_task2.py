
def sr_arif(*args):
    C = 0
    for i in args:
        C += i
    d = len(args)
    sr = C / d
    print(sr)

sr_arif(3, 4, 6, 7)
