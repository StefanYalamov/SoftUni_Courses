speed = float(input())

if speed <= 10:
    print("slow")
if speed in range(10, 50):
    print("average")
if speed in range(50, 150):
    print("fast")
if speed in range(150, 1000):
    print("ultra fast")
if speed > 1000:
    print("extremely fast")
