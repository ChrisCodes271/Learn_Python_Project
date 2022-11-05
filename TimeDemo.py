import time

print(time.ctime(0)) #Convert a time expressed in seconds since epoch to a readable string

print(time.time()) #Show current epoch time in seconds since Dec 31, 1969 at 1900 .

print(time.ctime(time.time()))

time_object = time.localtime() # Struct time object with many keyword arguments.
# output time.struct_time(tm_year=2022, tm_mon=11, tm_mday=5, tm_hour=0, tm_min=13, tm_sec=14, tm_wday=5, tm_yday=309, tm_isdst=1)
# its not very readable so we can use...

local_time = time.strftime('%B %d %y %H:%M:%S', time_object) # Need format and time object as argument. Format can be found on documentation.

time_string = "20 April, 2020"
mod_time = time.strptime(time_string, '%d %B, %Y') #This will convert a string date into a format.


time_tuple = (2020, 4, 20, 6, 9, 0, 12, 312, 0) #Tuple rep of time and date

tupled_time = time.asctime(time_tuple) # This can convert above

print(tupled_time)
