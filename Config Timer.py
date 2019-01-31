import time

time_text = input("Enter the cooking time (seconds please): ")

time_int = int(time_text)

print("Get cooking now, I'll warn you when time is up!")

time.sleep(time_int)

print("Time is up, you're done cooking for now")