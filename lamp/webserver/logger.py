from collections import defaultdict

class Logger:
    def __init__(self):
        self.on = defaultdict(lambda: 0)
        self.off = defaultdict(lambda: 0)
    def log_on(self):
        t = datetime.now().strftime("%H:%M")
	self.on[t] += 1
        print 'ON',t
    def log_off(self):
        t = datetime.now().strftime("%H:%M")
        self.off[t] += 1
        print 'OFF',t

    def get_stats(self):
        return {'on':on, 'off':off}
