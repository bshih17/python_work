def add_time(start, duration, starting_day=''):

  split_start = start.split()
  split_time = split_start[0].split(':')
  period = split_start[1]

  split_duration = duration.split(':')

  # If the starting hours is 12, then represent that with 0.
  # 12:13 AM would be represented by 0:13 AM.
  # From 0:00 to 11:59 AM would be one period.
  starting_hrs = int(split_time[0])
  if starting_hrs == 12:
    starting_hrs = 0
  
  total_hrs = int(split_time[0]) + int(split_duration[0])
  total_mins = int(split_time[1]) + int(split_duration[1])

  periods_passed = 0
  days_passed = 0

  # If no need to adjust minutes
  if total_mins < 60:
    ending_mins = total_mins

    # If no need to adjust hours (0 <= total_hours < 12)
    ending_hrs = total_hrs
    
    # If need to adjust hours (total hours is 12 or more)
    # This means at least one period has passed.
    while ending_hrs >= 12:
      ending_hrs -= 12
      periods_passed +=1
      
  # If need to adjust minutes
  else:
    # Convert extra minutes into hours.
    extra_mins_in_hrs = int(total_mins / 60)
    ending_mins = total_mins - 60*extra_mins_in_hrs

    total_hrs += extra_mins_in_hrs

    # If no need to adjust hours
    ending_hrs = total_hrs

    # If need to adjust hours
    while ending_hrs >= 12:
      ending_hrs -= 12
      periods_passed +=1


  # Determine days passed
  if period == 'AM':
    days_passed = int(periods_passed / 2)
  if period == 'PM':
    days_passed = int((periods_passed + 1) / 2)

  # Update AM or PM
  if periods_passed %2 == 1:
    if period == 'AM':
      period = 'PM'
    else:
      period = 'AM'
  

  # Convert 0 back to 12.
  if ending_hrs == 0:
    ending_hrs = 12
  
  if ending_mins < 10:
    ending_mins = "0" + f"{ending_mins}"


  new_time = f"{ending_hrs}:{ending_mins} {period}"

  # days_later string to be displayed
  if days_passed == 1:
    new_time += " (next day)"
  elif days_passed >= 2:
    new_time += f" ({days_passed} days later)"


  if starting_day:
    days_of_the_week = [
      'sunday', 'monday', 'tuesday', 'wednesday',
      'thursday', 'friday', 'saturday'
      ]
    
    starting_day = starting_day.lower()

    starting_day_number = days_of_the_week.index(starting_day)
    
    ending_day_number = (starting_day_number + days_passed) %7
    ending_day = days_of_the_week[ending_day_number].title()

    new_time = f"{ending_hrs}:{ending_mins} {period}, {ending_day}"

    if days_passed == 1:
      new_time += " (next day)"
    elif days_passed >= 2:
      new_time += f" ({days_passed} days later)"


  return new_time


print(add_time("12:20 PM", "8:33", "Tuesday"))

print(add_time("11:06 PM", "2:02"))
