def tester():
    for n in range(100,1000000000):
        for input in Test:
            N = str(n)
            Check = True
            for i in range(3):
                if str(input)[i] in N:
                    N = N[N.index(str(input)[i]):]
                else:
                    Check = False
                    break
            if not Check:
                break
        if Check:
            return n
    return "Fail"   

# 73162890
   




Test = [319,
680,
180,
690,
129,
620,
762,
689,
762,
318,
368,
710,
720,
710,
629,
168,
160,
689,
716,
731,
736,
729,
316,
729,
729,
710,
769,
290,
719,
680,
318,
389,
162,
289,
162,
718,
729,
319,
790,
680,
890,
362,
319,
760,
316,
729,
380,
319,
728,
716]

