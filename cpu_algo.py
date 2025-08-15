import threading

def cpu_task(cycles):
    count = 0
    x = 0.00001
    while count < cycles:
        x = (x * x) + (3.14159 / 2) % 10000
        count += 1 

def mt_cpu_task(cycles):
    batch = cycles // 10000
    threads = []
    for _ in range(10000):
        t = threading.Thread(target=cpu_task, args=(batch,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()


if __name__ == "__main__":
    cpu_task(100000000)

