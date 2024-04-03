from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.memory import MemoryJobStore


scheduler = BackgroundScheduler()
scheduler.add_jobstore(MemoryJobStore())
