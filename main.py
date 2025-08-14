import algos
import time

def compute_time(fn, algo_type):
    print(f'Running {algo_type}...')
    start = time.perf_counter_ns()
    result = fn()
    end = time.perf_counter_ns()
    return end - start

def display_data(duration, name) -> None:
    print(f'{name} took {duration} ns')
    print(f'{name} took {duration // 1000000} ms')

def fifo(jobs: list) -> None:
    duration_ns = compute_time(lambda: algos.first_in_first_out(jobs, 0), "FIFO IO")
    display_data(duration_ns, "FIFO IO")
    duration_ns = compute_time(lambda: algos.first_in_first_out(jobs, 1), "FIFO CPU")
    display_data(duration_ns, "FIFO CPU")


def main():
    jobs = [1, 1, 1, 1]
    fifo(jobs)

if __name__ == "__main__":
    main()
