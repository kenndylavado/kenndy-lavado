from datetime import datetime


time_now = datetime.strptime("2022/12/15 20:30:00", "%Y,%m,%d %H,%M,%S").timestamp()

print("la conversion de nuestro valor time now es: {}".format(time_now))
 
 