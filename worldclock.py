import datetime  

while (True):
  ## get the name of the city from the user
  city = input("Enter city: ")

  ## get the current time 
  current_time = datetime.datetime.now()

  ## save hours, minutes and second of the current time 
  ## in their corresponding variables 
  hour = current_time.hour
  minute = current_time.minute
  second = current_time.second
  
  if city == "Boston":
    hour = hour - 4 

  elif city == "Tokyo":
    hour = hour + 9

  elif city == "Chicago":
    hour = hour - 5 

  elif city == "Seattle":
    hour = hour - 7
  
  elif city == "exit": 
    break

  else:
    print(city, "is not added")
    city = "GMT" 

  # print the name of the city and the its corresponding time
  print(city, str(hour) + ":" + str(minute) + ":" + str(second))
