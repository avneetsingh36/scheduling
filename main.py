import algos
import time
import asyncio
import cpu_algo

def compute_time(fn, algo_type):
    print(f'Running {algo_type}...')
    start = time.perf_counter_ns()
    if algo_type == "ASYNC IO":
        asyncio.run(fn())
    else:
        result = fn()
    end = time.perf_counter_ns()
    return end - start

def display_data(duration, name) -> None:
    print(f'{name} took {duration} ns')
    print(f'{name} took {duration // 1000000} ms')
    print()

def fifo_tasks(jobs: list) -> None:
    duration_ns = compute_time(lambda: algos.first_in_first_out(jobs, 0), "FIFO IO")
    display_data(duration_ns, "FIFO IO")

    duration_ns = compute_time(lambda: algos.first_in_first_out(jobs, 1), "FIFO CPU")
    display_data(duration_ns, "FIFO CPU")
    
def async_tasks(jobs: list) -> None:
    duration_ns = compute_time(lambda: algos.async_IO_tasks(jobs, 2), "ASYNC IO")
    display_data(duration_ns, "ASYNC IO")

def mp_tasks(jobs: list) -> None:
    duration_ns = compute_time(lambda: algos.multiprocessing_CPU_tasks(jobs, 3), "MP CPU")
    display_data(duration_ns, "MP CPU")

def cpu_tasks(cycles):
    duration_ns = compute_time(lambda: cpu_algo.cpu_task(cycles), "Single Threaded CPU Task")
    display_data(duration_ns, "Single Threaded CPU Task")

    duration_ns = compute_time(lambda: cpu_algo.mt_cpu_task(cycles), "Multithreaded CPU Task")
    display_data(duration_ns, "Multithreaded CPU Task")

def main():
    jobs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    # print(f"We are running {len(jobs)} jobs take each take approx 1 second to compute.")
    # fifo(jobs)

    cpu_tasks(100000000)

if __name__ == "__main__":
    main()
