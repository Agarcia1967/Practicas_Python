import datetime

def hms(time:int)->str:
    h : int = time // 3600
    m : int = (time -  h * 3600) // 60
    s : int = (time - h * 3600 - m * 60)
    return "%02d:%02d:%02d"%(h,m,s)

def datetime_to_float(d:datetime)->float:
    epoch = d.utcfromtimestamp(0)
    total_seconds =  (d - epoch).total_seconds()
    # total_seconds will be in decimals (millisecond precision)
    return total_seconds
