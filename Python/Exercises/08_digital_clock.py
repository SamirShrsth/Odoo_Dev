import time

input_time = int(input("Enter the countdown time in seconds: "))

for x in range(input_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600) % 12
    print(f"{hours:02}:{minutes:02}:{seconds:02}", end="\r", flush=True)
    time.sleep(1)
    
print("Time's Up!")