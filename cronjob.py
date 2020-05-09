# Package Scheduler.
from apscheduler.schedulers.blocking import BlockingScheduler

# Main cronjob function.
from app import send_message

# Create an instance of scheduler and add function.
scheduler = BlockingScheduler()
scheduler.add_job(send_message, "interval", seconds=30)

scheduler.start()
