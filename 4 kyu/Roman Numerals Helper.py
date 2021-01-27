class RomanNumerals:
    def to_roman(a):
        while len(str(a))<4:
            a='0'+str(a)

        list=[]
        if int(str(a)[-4])==0: a
        elif int(str(a)[-4]) in[1,2,3]: list.append('M'*int(str(a)[-4]))

        if int(str(a)[-3])==0: a
        elif int(str(a)[-3]) in[1,2,3]: list.append('C'*int(str(a)[-3]))
        elif int(str(a)[-3]) in[4,5]: list.append('CD'[int(str(a)[-3])-4:2])
        elif int(str(a)[-3]) in[6,7,8]: list.append('DCCC'[0:int(str(a)[-3])-4])
        elif int(str(a)[-3]) in[9]: list.append('CM')

        if int(str(a)[-2])==0: a
        elif int(str(a)[-2]) in[1,2,3]: list.append('X'*int(str(a)[-2]))
        elif int(str(a)[-2]) in[4,5]: list.append('XL'[int(str(a)[-2])-4:2])
        elif int(str(a)[-2]) in[6,7,8]: list.append('LXXX'[0:int(str(a)[-2])-4])
        elif int(str(a)[-2]) in[9]: list.append('XC')

        if int(str(a)[-1])==0: a
        elif int(str(a)[-1]) in[1,2,3]: list.append('I'*int(str(a)[-1]))
        elif int(str(a)[-1]) in[4,5]: list.append('IV'[int(str(a)[-1])-4:2])
        elif int(str(a)[-1]) in[6,7,8]: list.append('VIII'[0:int(str(a)[-1])-4])
        elif int(str(a)[-1]) in[9]: list.append('IX')

        return ''.join(x for x in list)

    def from_roman(a):
        list = []
        for x in a[:-1]:
            if x == 'I': list.append(-1 if 'IV' in a[(a.index(x)):(a.index(x) + 2)] or 'IX' in a[(a.index(x)):(a.index(x) + 2)] else 1)
            elif x == 'V': list.append(5)
            elif x == 'X': list.append(-10 if 'XL' in a[(a.index(x)):(a.index(x) + 2)] or 'XC' in a[(a.index(x)):(a.index(x) + 2)] else 10)
            elif x == 'L': list.append(50)
            elif x == 'C': list.append(-100 if 'CM' in a[(a.index(x)):(a.index(x) + 2)] or 'CD' in a[(a.index(x)):(a.index(x) + 2)] else 100)
            elif x == 'D': list.append(500)
            elif x == 'M': list.append(1000)

        if a[-1] == 'I': list.append(1)
        if a[-1] == 'V': list.append(5)
        if a[-1] == 'X': list.append(10)
        if a[-1] == 'L': list.append(50)
        if a[-1] == 'C': list.append(100)
        if a[-1] == 'D': list.append(500)
        if a[-1] == 'M': list.append(1000)

        return sum(list)

print(RomanNumerals.to_roman('1234'))