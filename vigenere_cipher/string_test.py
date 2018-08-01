import time

print("Doing string concatenation...")
time_start = time.time()
for run in range(10000):
    if run == 2500:
        print("25% complete...")
    elif run == 5000:
        print("50% complete...")
    elif run == 7500:
        print("75% complete...")
    build_str = ""
    for char in range(10000):
        build_str += "x"
print(format("String concatenation: %s" % (format(time.time() - time_start, ".5f"))))

print("\nDoing list append...")
time_start = time.time()
for run in range(10000):
    if run == 2500:
        print("25% complete...")
    elif run == 5000:
        print("50% complete...")
    elif run == 7500:
        print("75% complete...")
    append_str = []
    for char in range(10000):
        append_str.append("x")
    string = "".join(append_str)
print(format("List appending: %s" % (format(time.time() - time_start, ".5f"))))