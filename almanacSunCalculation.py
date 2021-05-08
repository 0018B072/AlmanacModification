#Get time zone (+1, +2, etc.)
#Feb24, 40*N, 60*W (sunrise)
# Get sunrise for latitude, N*40 = 06:40 (sunrise)
# Correct for longitude, convert time zone to standard meridian
# by simply multiplying it by 15 (4*15), if conversion = 60*W, no correction needed
# 
# +4Q, FEB 24, Sunrise, 40*N 65*W
# Find time of sunrise at latitude (40*N): 06:40
# Since 65*W isn't corresponding to standard meridian, we convert the arc to time
# Since it's a difference of 5 from real standard meridian, the back of the almanac states
# that 5 deg diff = 20 min, then you just add 20 min to latitude time (06:40)
#
#
# +4Q, FEB 24, Sunrise, 42*30'N 70*30'W
# Correct for latitude, choose values that are in between your number: 45 & 40
# Longitude has a 10 deg and 30 min difference
# almanac states 10 deg = 40 min, 30 min of arc = 2 min
# add this time since things happen later (70 = later, 50 from 60 = early)
# 06:42:30 + 42 = 07:24:30
#
#
#
# Ask the user to measure the time it takes to get from 45 deg sunrise to twilight
# have that value be subtracted to your current day sunrise time to find current time
#
#
# Userinputs:   Get time zone (+1, +2, etc.)
#               Find time of sunrise at latitude (40*N): 06:40 from almanac
#               Correct for longitude, convert time zone to standard meridian by multiplying time zone by 15
#               If no correction is needed, time is equal to calculated latitude time, else you would have to
#               find the difference from your "real" and "standard time". The difference would then be looked
#               up in the arc to time table. The arc to time would then be added or subtracted to your calculated 
#               latitude time depending on if your difference is negative or positive (add if positive).
#               Record the time it takes from expected angle of sun to twilight, then add that value to your
#               calculated sunrise time (subtract for sunset time) (output: the time at a specific 
#               sun angle for the next 3 weeks *time changes throughout the year*)