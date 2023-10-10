#BATTERY STATUS CHECK WITH PYTHON :robot:
This is a simple python app that gives you feedback about your battery status with a desktop audio notification, it runs every 30 minutes :clock1230:. Interrupt the script manually with ctrl+c

##Pip installation
Install psutils and winotify, utils will help us with the battery statistics and winotify to send desktop notification.
So let's run this in your terminal when you fork this code
` ` ` 
pip install psutils
pip install winotify
` ` ` 

##Usage
You just need to launch the script with the command 
` ` ` 
python battery.py
` ` ` 
when you want to stop it just press ctrl+c in your terminal
