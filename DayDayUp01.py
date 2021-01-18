dayFactor1=0.01
dayUp1=pow(1+dayFactor1,365)
dayDown1=pow(1-dayFactor1,365)
print("dayUp={:.2f},dayDown={:.2f}".format(dayUp1,dayDown1))

dayFactor5=0.005
dayUp5=pow(1+dayFactor5,365)
dayDown5=pow(1-dayFactor5,365)
print("dayUp={:.2f},dayDown={:.2f}".format(dayUp5,dayDown5))

dayFactor01=0.001
dayUp01=pow(1+dayFactor01,365)
dayDown01=pow(1-dayFactor01,365)
print("dayUp={:.2f},dayDown={:.2f}".format(dayUp01,dayDown01))

dayup,dayfactor=1.0,0.01
for i in range(365):
    if i % 7 in [6,0]:
        dayup*=(1-dayfactor)
    else:
        dayup*=1+dayfactor

print("向上5天，向下2天的力量，dayUp={:.2f}".format(dayup))


def dayUP(df):
    dayup=1.0
    for i in range(365):
        if i % 7 in [6, 0]:
            dayup *= (1 - 0.01)
        else:
            dayup *= 1 + df
    return dayup
dayfactor=0.01
while(dayUP(dayfactor)<37.78):
    dayfactor+=0.001
print("每天的实际努力参数是：{:.3f}。".format(dayfactor))
