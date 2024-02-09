dd = '45.605'

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