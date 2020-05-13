import ast

n=int(raw_input().strip())
L=[]
for i in range(n):
    L.append(raw_input().strip())

pub_title={}
pub_number={}
article_counts={}
pub_counts=[]


dict_=ast.literal_eval(L.pop(0))

for a,b in dict_.items():
    count=0
    for c in b:
        count=0
        pub_title.update({c["publicationNumber"]:c["publicationTitle"]})
        pub_number.update({c["publicationNumber"]:0})
        article_counts.update({c["publicationNumber"]:0})
        for f in c["articleCounts"]:
            count+= int(f["articleCount"])
        article_counts[c["publicationNumber"]]+=count
        
for d in L:
    dict_=dict_=ast.literal_eval(d)
    data = dict_["paperCitations"]["ieee"]
    for e in data:
        for g in pub_number:
            if (e["publicationNumber"]==g and (e["year"]=="2018" or e["year"]=='2017')):
                pub_number[g]+=1
                
answer={}
keys_=[]

for h in pub_number.keys():
    IF=float(pub_number[h])/float(article_counts[h])
    display=pub_title[h]+ ": " + "%.2f" %(IF)
    print display
    answer.update({IF:display})
    keys_.append(IF)

keys_.sorted()
keys_.reverse()

for i in keys_:
    print i

