from datetime import datetime, time

t1 = datetime.strptime('15:30', '%H:%M')
t2 = datetime.strptime( '11:00', '%H:%M')
print(t1)
print(t2)
dt = abs(t2 - t1)
print(dt)

t = time(dt.seconds // 3600, (dt.seconds // 60) % 60)

t.strftime('%H:%M')