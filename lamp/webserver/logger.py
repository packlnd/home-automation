from collections import defaultdict

class Logger:
    def __init__():
        on = defaultdict(lambda: 0)
        off = defaultdict(lambda: 0)
    def log_on(self):
        off[t] += 1
        t = datetime.now().strftime("%H:%M")
        print 'ON',t
    def log_off(self):
        t = datetime.now().strftime("%H:%M")
        on[t] += 1
        print 'OFF',t

    def get_stats(self):
        return {'on':on, 'off':off}
