import psutil, time
from winotify import Notification, audio
import time
#function to converts seconds to hours
def convert(seconds):
    return time.strftime("%H:%M:%S", time.gmtime(seconds))
#setting the function that returns battery values to battery so we can retrieve in a simple way the data we want
battery = psutil.sensors_battery()
#setting up our desktop notifications messages for each case using winotify
charging = Notification(app_id="Battery status",
                        title="Charging, current charge: %s%%" %(battery.percent),
                        msg="You are safe",
                        duration="long")
#setting up our notifications sounds for the desktop notification
charging.set_audio(audio.Default, loop=False)

high = Notification(app_id="Battery status",
                        title="Current charge: %s%%" %(battery.percent),     #secleft indicates how many seconds are left in the battery to run
                        msg="Keep grinding, time left: %s" %(convert(battery.secsleft)),
                        duration="long")
high.set_audio(audio.Default, loop=False)

lessThanFifty = Notification(app_id="Battery status",
                            title="Current charge: %s%%" %(battery.percent),                    
                            msg="You have used more than a half of your battery, time left: %s" %(convert(battery.secsleft)), 
                            duration="long")
lessThanFifty.set_audio(audio.Default, loop=False)

lessThanTwentyfive = Notification(app_id="Battery status",
                                  title="Low Battery, current charge: %s%%" %(battery.percent),
                                  msg="Attention, time left: %s" %(convert(battery.secsleft)), 
                                  duration="long")
lessThanTwentyfive.set_audio(audio.Default, loop=False)

lessThanFive = Notification(app_id="Battery status",
                            title="ATTENTION!, Current charge: %s%%" %(battery.percent),
                            msg="You need to charge your device , time left: %s" %(convert(battery.secsleft)), 
                            duration="long")
lessThanFive.set_audio(audio.LoopingAlarm, loop=True)

#while loop to make this script run every 30 minutes to check our battery
while True:
    battery = psutil.sensors_battery()
    #power_blugged returns a boolean that indicates if the device is charging
    if battery.power_plugged:
        charging.show()
    else:
        #battery percent returns a number that indicates the battery percentage 
        if battery.percent >= 50:
            high.show()
        elif battery.percent < 25:
            if battery.percent <= 5:
                lessThanFive.show()
            else:
                lessThanTwentyfive.show()
        else:
           lessThanFifty.show()
    # Check the battery status every 30 minutes (1800 seconds)
    time.sleep(1800) 



    
