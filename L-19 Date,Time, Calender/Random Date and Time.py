import random
import time
def rd(sD,eD) :
    rn = random.random()
    df = "%M/%D/%Y"
    st = time.mktime(time.strptime(sD,df))
    et = time.mktime(time.strptime(eD,df))
    rt = st + rn*(et - st)
    rd1 = time.strftime(df,time.localtime(rt))
    return rd1
print(rd('1/1/25','8/4/25'))