from collections import defaultdict
from datetime import datetime

class Logger:
    def __init__(self):
        self.on = defaultdict(lambda: 0)
        self.off = defaultdict(lambda: 0)
        self.stats = []
        self.alarms = []

    def log_on(self):
        self.lastOn = datetime.now()
        t = self.lastOn.strftime("%H:%M")
        self.on[t] += 1
        print 'ON',t

    def log_off(self):
        now = datetime.now()
        t = now.strftime("%H:%M")
        self.off[t] += 1
        duration = (now-self.lastOn).total_seconds()
        print 'OFF',t,' was on for',duration,'seconds'
        if duration < 5*60: # 5 minutes
            return
        self.stats.append({
            'on': self.lastOn,
            'off': now,
            'duration': duration,
            'energy': 0.0
        })

    def get_stats(self):
        return {'stats': self.stats, 'counts': len(self.stats)}

    def add_alarm(self, alarm):
        self.alarms.append(alarm)
