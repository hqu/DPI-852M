import re,json,itertools,collections
S=[];
for l in open('rows.txt'):
    p=l.strip().split('|')
    cs=[]
    for c in p[2:]:
        m=re.match(r'^\s*([A-Za-z]+)[\s-]*(\d{2,3})',c)
        if m:
            k=m.group(1).upper()+'-'+m.group(2)
            if k not in cs: cs.append(k)
    S.append({'id':p[0],'prog':p[1],'courses':cs})
cc=collections.Counter(c for s in S for c in s['courses'])
se=collections.Counter(); ce=collections.Counter()
for a,b in itertools.combinations(S,2):
    sh=sorted(set(a['courses'])&set(b['courses']))
    if sh: se[(a['id'],b['id'])]=sh
for s in S:
    for a,b in itertools.combinations(sorted(s['courses']),2): ce[(a,b)]+=1
D={'students':[{'id':s['id'],'prog':s['prog'],'courses':s['courses']} for s in S],
 'sedges':[{'s':a,'t':b,'shared':v} for (a,b),v in se.items()],
 'courses':[{'id':c,'n':n} for c,n in cc.items()],
 'cedges':[{'s':a,'t':b,'w':w} for (a,b),w in ce.items()]}
json.dump(D,open('data.json','w'))
print(len(S),len(D['sedges']),len(D['courses']),len(D['cedges']),cc.most_common(6))
