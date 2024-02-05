from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from config import Config




# Configure the Job Store
jobstores = {
    'default': SQLAlchemyJobStore(url=Config.DATABASE_URI)
}

# Initialize the Scheduler with the Job Store
scheduler = BackgroundScheduler(jobstores=jobstores)