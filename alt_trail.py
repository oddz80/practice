import re

# base_position = "58°56'32.12\""

def deg2format(dms :str):
    parts = re.split(r"[°'\"]",dms)
    lat = deg2dd(parts[0], parts[1], parts[2],)
    return(lat)

def deg2dd(deg, min, sec):
    dd = float(deg) + float(min)/60 + float(sec)/3600
    return(dd)

def dd2dms(deg):
    d = int(deg)
    md = (deg - d)*60
    m = int(md)
    sd = (md - m)*60
    return(d, m, sd)

def main():
    base_position = "58°56'32.12\""
    dd = deg2format(base_position)
    print('Position in decimal degrees: ' + str(dd))
    dms = dd2dms(dd)
    print('Position in (degrees, minutes, decimal seconds): ' + str(dms))

if __name__ == '__main__':
    main()