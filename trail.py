import math

def main():
    print('python prcatice')
    print(to_decimal_degrees(45,36,18))
    decimal_deg_to_deg_min_sec('45.605')

def to_decimal_degrees(deg, min, sec):
    result = deg + min/(60) + sec/(60*60)
    return(result)

def decimal_deg_to_deg_min_sec(dd:str):
#    (deg,drest) = dec_deg.split('.')
#    minute = (float(dec_deg) - float(drest))*60
#    min = str(minute)
#    second = min.split('.')
#    sec = (float(min) - )
#    sec = str(second)
#    sd = float(sec)*60
#    return(deg, min, sd)
     dm = dd.split('.')
     d = dm[0]
     nil = '0.'
     md = nil + dm[1]
     mf = float(md)*60
     m = str(mf)
     sd = m.split('.')
     sf = nil + sd[1]
     sg = float(sf) *60
     s = str(sg)
     print(d + ' deg ' + m + ' min ' + s + ' sec ')

if __name__ == "__main__":
    main()