from geopy.geocoders import Nominatim
from apscheduler.schedulers.blocking import BlockingScheduler

def schedule_lamp_on():
        print "Decorated job"
        scheduler = BlockingScheduler()
        scheduler.add_job(some_job, 'interval', hours=1)
        scheduler.start()
