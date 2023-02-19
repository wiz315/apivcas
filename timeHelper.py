from datetime import datetime, timedelta
import pytz



def timeNow():
    dt = pytz.utc.localize(datetime.now())
    ist_dt = dt.astimezone(pytz.timezone('Asia/Damascus'))
    return ist_dt

def nextOrderTime(days):
    day =  timeNow()+timedelta(days)
    return day

