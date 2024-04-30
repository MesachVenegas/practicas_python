from datetime import datetime
from dateutil.relativedelta import relativedelta

now= datetime.now()
print(now)


now = now + relativedelta(months=1, weeks=1, hour=10)
print(now)