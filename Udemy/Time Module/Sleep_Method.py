#It is used to stop execution of program temporarly for given amount of time.
#It is belonged to time module
import time
for i in range(20):
    print(i)
    if i==10:
        time.sleep(5)
