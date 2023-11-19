"""
Booking script to log into gym reservation systems automatically at a certain time to reserve spots. 

Currently, this script does not includ webscraping to identify potential changes in scheduling, although this feature is planned to be 
added in the future. The script will be written in python. 

This file is designed to be run by a job scheduling tool such as cronjobs or any other scheduler. No arguments are needed
the user may just simply trigger python3 run.py in order to launch the system. The scheduled data has to be set as close as possible to
the date at which booking opens. As mentioned previously, we aim to introduce functionalty for webscraping in the future, so that this
manual step will no longer be neccesary.
"""

from main import launch_request

launch_request()


