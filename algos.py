import time
import asyncio
import os
from concurrent.futures import ProcessPoolExecutor

IO = 0
CPU = 1
ASYNC_IO = 2
ASYNC_CPU = 3


# ---- sync (blocking) functions ----
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
    elif task_type == CPU:
        for job in jobs:
            cpu_task(job)
    return True


# ---- async (non-blocking) functions ----

async def io_task_async(seconds) -> None:
    await asyncio.sleep(seconds)


async def async_IO_tasks(jobs: list, task_type: int) -> bool:
    if task_type == ASYNC_IO:
        tasks = [asyncio.create_task(io_task_async(job)) for job in jobs]
        await asyncio.gather(*tasks)
    return True

# ---- parallel functions ----

def multiprocessing_CPU_tasks(jobs: list, task_type: int) -> bool:
    workers = os.cpu_count()
    with ProcessPoolExecutor(max_workers=workers) as pool:
        list(pool.map(cpu_task, jobs))
    
    print(f'Cores used: {workers}')
    return True

