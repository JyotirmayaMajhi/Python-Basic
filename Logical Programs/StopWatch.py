import time

start = input("Enter to start the timer")
print("The timer has started")
begin = time.time()
end=input('Enter to stop the timer')
end=time.time()
elapsed=end-begin
print('The time elapsed is',elapsed,'seconds')