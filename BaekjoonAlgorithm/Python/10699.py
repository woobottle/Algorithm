from datetime import datetime, timezone, timedelta

now_utc = datetime.now()
timeDiff = timedelta(hours=3)
now_kst = now_utc + timeDiff
print(now_kst.strftime("%Y-%m-%d"))