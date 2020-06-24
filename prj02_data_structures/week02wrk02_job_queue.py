# python3

from collections import namedtuple
from queue import PriorityQueue

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs_naive(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(
            range(n_workers),
            key=lambda w: next_free_time[w]
        )
        result.append(
            AssignedJob(next_worker, next_free_time[next_worker])
        )
        next_free_time[next_worker] += job

    return result


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    pq = PriorityQueue()
    for idx in range(n_workers):
        pq.put((0, idx), block=False)
    for job in jobs:
        tm, idx = pq.get(block=False)
        result.append(
            AssignedJob(
                worker=idx,
                started_at=tm
            )
        )
        pq.put((tm+job, idx))

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
