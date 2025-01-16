a,b = ["cfc","bob","hello","bye","mc","ll","p","a","r","pl","oo","i","q","735ferc","defuicxuw","happy"],[]
for i in a :
    if (len(i) >= 2) and (i[0] == i[-1]) :
        b.append(i)
print(b,"\n",len(b))
