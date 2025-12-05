from apscheduler.schedulers.background import BackgroundScheduler
import datetime
from . models import *

def save_expired_stock(stock):
    ExpiredStock.objects.create(
        name= stock.name,
        quantity= stock.quantity,
        expired_date= stock.expired_date,
    )

def process_stock():
    
    today= datetime.date.today()
    
    expired_stock= Stock.objects.filter(expired_date=today)
    
    for item in expired_stock:
        save_expired_stock(item)
        item.delete()
    
def start_scheduler():
    scheduler= BackgroundScheduler()
    scheduler.add_job(process_stock,"cron",hour=0,minutes=0)
    scheduler.start()