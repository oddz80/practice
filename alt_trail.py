import re
from typing import Tuple
# base_position = "58°56'32.12\""

def deg2format(dms :str)-> float:
    parts = re.split(r"[°'\"]",dms)
    lat = deg2dd(parts[0], parts[1], parts[2],)
    return(lat)

def deg2dd(deg:str, min:str, sec:str)-> float:
    dd = float(deg) + float(min)/60 + float(sec)/3600
    return(dd)

def dd2dms(deg:str)-> Tuple:
    d = int(deg)
    md = (deg - d)*60
    m = int(md)
    sd = (md - m)*60
    return(d, m, sd)

def my_fuc(list_deg:list)->list:
    
    return ([(73,69),(18.34,898)])
def main():
    
    base_position = "58°56'32.12\""
    dd = deg2format(base_position)
    print('Position in decimal degrees: ' + str(dd))
    dms = dd2dms(dd)
    print('Position in (degrees, minutes, decimal seconds): ' + str(dms))

if __name__ == '__main__':
    main()