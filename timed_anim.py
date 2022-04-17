import time

num = None


def numbers(nums):
    t1 = time.time()
    for x in reversed(range(1, nums + 1)):
        num = x
        time.sleep(0.99)
        print(num)
    t2 = time.time()
    print("Time %s seconds" % (t2 - t1))


numbers(60)
