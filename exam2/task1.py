import random
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class VM:
    vm_id: str
    capacity: float          # total CPU capacity (GHz)
    available: float         # remaining CPU (GHz)

    def can_host(self, demand: float) -> bool:
        return self.available >= demand

    def allocate(self, demand: float) -> None:
        self.available -= demand


@dataclass
class Task:
    task_id: str
    demand: float

def best_fit_vm(vms: List[VM], demand: float) -> Optional[VM]:
    candidates = [vm for vm in vms if vm.can_host(demand)]
    if not candidates:
        return None
    return min(candidates, key=lambda vm: vm.available - demand)


def simulate_tasks(num_tasks: int, min_ghz: float, max_ghz: float, seed: Optional[int] = None) -> List[Task]:
    if seed is not None:
        random.seed(seed)

    tasks = []
    for i in range(1, num_tasks + 1):
        demand = round(random.uniform(min_ghz, max_ghz), 2)
        tasks.append(Task(task_id=f"T{i}", demand=demand))
    return tasks


def main():
    vms = [
        VM("VM1", capacity=4.0, available=4.0),
        VM("VM2", capacity=6.0, available=6.0),
        VM("VM3", capacity=8.0, available=8.0),
    ]

    tasks = simulate_tasks(
        num_tasks=10,
        min_ghz=1.0,
        max_ghz=5.0,
        seed=42
    )

    print("=== Initial VM State ===")
    for vm in vms:
        print(f"{vm.vm_id}: capacity={vm.capacity} GHz, available={vm.available} GHz")

    print("\n=== Task Allocation Results (Best-Fit) ===")
    for task in tasks:
        vm = best_fit_vm(vms, task.demand)
        if vm is None:
            print(f"{task.task_id} needs {task.demand} GHz -> Task cannot be allocated")
        else:
            vm.allocate(task.demand)
            print(
                f"{task.task_id} needs {task.demand} GHz -> assigned to {vm.vm_id} "
                f"(remaining on {vm.vm_id}: {vm.available:.2f} GHz)"
            )

    print("\n=== Final VM State ===")
    for vm in vms:
        used = vm.capacity - vm.available
        print(f"{vm.vm_id}: used={used:.2f} GHz, available={vm.available:.2f} GHz, capacity={vm.capacity:.2f} GHz")


if __name__ == "__main__":
    main()
