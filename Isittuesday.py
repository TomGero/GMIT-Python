# Tom Geraghty 14/02/2018
# Is it Tuesday

import datetime

if datetime.datetime.today().weekday() == 2:
    print("Yes, it is Wednesday")
else:
    print("Nope, its not Wednesday")

