alarms = []

def set_alarm(time):
    s = time.split(' : ')
    s2 = s[1].split()
    s2.insert(0, s[0])
    alarm = tuple(s2)
    alarms.append(alarm)

def get_alarms():
    return alarms
