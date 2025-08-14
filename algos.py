import time

IO = 0
CPU = 1

def cpu_task(seconds) -> int:
    """
    Spin the CPU for ~`seconds` by doing pointless math.
    `complexity` controls inner-loop work per iteration.
    Returns an accumulator so work can't be optimized away.
    """
    end = time.perf_counter() + seconds
    acc = 0
    x = 1.000001
    while time.perf_counter() < end:
        # inner loop to scale CPU work
        for _ in range(10):
            x = (x * 1.000001 + 3.14159) % 997.0
            acc += int(x * x) & 0xFFFF

def io_task(seconds):
    time.sleep(seconds)


def first_in_first_out(jobs: list, task_type: int) -> bool:
    
    if task_type == IO:
        for job in jobs:
            io_task(job)

    if task_type == CPU:
        for job in jobs:
            cpu_task(job)

    return True

