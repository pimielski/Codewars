def format_duration(seconds):
    s = seconds%60
    m = seconds//60%60
    h = seconds//(60**2)%24
    d = seconds//(60**2*24)%365
    y = seconds//(60**2*24*365)

    x = f'{(str(y) + " year" if y == 1 else str(y) + " years") if y > 0 else "x"} ' \
        f'{(str(d) + " day" if d == 1 else str(d) + " days") if d > 0 else "x"} ' \
        f'{(str(h) + " hour" if h == 1 else str(h) + " hours") if h > 0 else "x"} ' \
        f'{(str(m) + " minute" if m == 1 else str(m) + " minutes") if m > 0 else "x"} ' \
        f'{(str(s) + " second" if s == 1 else str(s) + " seconds") if s > 0 else "x"}'\

    x = x.replace('x ', '').replace('s ', 's, ').replace('r ', 'r, ').replace('y ', 'y, ').replace('e ', 'e, ').replace('d ', 'd, ').replace(', x','')
    return f'{(x[:x.rindex(",")])+" and"+(x[x.rindex(",")+1:])}' if "," in x else ('now' if seconds==0 else x)


print(format_duration(1234))