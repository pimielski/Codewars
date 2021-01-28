def parse_int(string):
    
    matrix = [['one',1], ['two',2], ['three',3], ['four',4], ['five',5],
             ['six',6], ['seven',7], ['eight',8], ['nine',9], ['ten',10],
             ['eleven', 11], ['twelve', 12], ['thirteen', 13], ['fourteen', 14], ['fifteen',15],
             ['sixteen', 16], ['seventeen',17], ['eighteen',18], ['nineteen',19], ['twenty',20],
             ['thirty',30], ['forty',40], ['fifty',50], ['sixty',60], ['seventy',70], ['eighty',80],
             ['ninety', 90], ['hundred',100], ['thousand', 1000], ['million', 1000000]]
    
    while '-' in string: string = string.replace('-', ' ')
    while ' and' in string: string = string.replace(' and', '')
    
    result_c = 0
    result_m = 0
    string = string.split()
        
    for x in string:
        for y in matrix:
            if x == y[0]:
                if y[1] == 1000000: result_c *= y[1]
                elif y[1] == 1000:
                    result_m = result_c * 1000
                    result_c = 0
                elif y[1] == 100: result_c *= y[1]
                else: result_c += y[1] 
    
    return result_c + result_m


print(parse_int('twenty-six thousand three hundred and fifty-nine'))