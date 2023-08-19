import time

start = time.time()
a = 0
for i in range(10**8):
    a = i
end = time.time()
excution_time = end - start

print(f"Code executed in",excution_time,"seconds.")