import itertools

doctors = [
    {'name': 'Dr. A', 'available_hours': [(9, 12), (2, 5)]},  # 9-12, then 2-5 (PM)
    {'name': 'Dr. B', 'available_hours': [(1, 5)]},  # 1-5 (PM)
    {'name': 'Dr. C', 'available_hours': [(9, 1)]},  # 9-1 (midday)
]

patients = [
    {'name': 'Patient 1', 'preferred_doctor': 'Dr. A', 'preferred_time': (10, 11)},
    {'name': 'Patient 2', 'preferred_doctor': 'Dr. B', 'preferred_time': (1, 2)},
    {'name': 'Patient 3', 'preferred_doctor': 'Dr. A', 'preferred_time': (2, 3)},
    {'name': 'Patient 4', 'preferred_doctor': 'Dr. C', 'preferred_time': (9, 10)},
]

rooms = [1, 2]
clinic_hours = (9, 17)  # 9:00-17:00


def normalize_hour(h: int) -> int:
    if 1 <= h <= 5:
        return h + 12
    return h


def normalize_range(r: tuple[int, int]) -> tuple[int, int]:
    start, end = r
    start_n = normalize_hour(start)
    end_n = normalize_hour(end)
    if end_n <= start_n:
        if end == 1 and start >= 9:
            end_n = 13
    return start_n, end_n


def normalize_patient_time(window: tuple[int, int]) -> tuple[int, int]:
    return normalize_range(window)


def expand_range_to_slots(time_range: tuple[int, int]) -> list[int]:
    start, end = time_range
    slots = []
    for hour in range(start, end):
        slots.append(hour)
    return slots


def expand_ranges_to_slots(ranges: list[tuple[int, int]]) -> set[int]:
    all_slots = set()
    for r in ranges:
        slots = expand_range_to_slots(r)
        for s in slots:
            all_slots.add(s)
    return all_slots


def build_doctor_slot_map(doctors_data: list[dict]) -> dict[str, set[int]]:
    doctor_slot_map: dict[str, set[int]] = {}
    for d in doctors_data:
        name = d["name"]
        ranges_raw = d["available_hours"]
        ranges_norm = [normalize_range(r) for r in ranges_raw]
        doctor_slot_map[name] = expand_ranges_to_slots(ranges_norm)
    return doctor_slot_map


def patient_window_slots(window: tuple[int, int]) -> set[int]:
    slots = expand_range_to_slots(window)
    return set(slots)


def candidate_slots_for_patient(
        patient: dict,
        doctor_slot_map: dict[str, set[int]],
        clinic_hours_range: tuple[int, int],
) -> list[int]:
    doctor = patient["preferred_doctor"]
    if doctor not in doctor_slot_map:
        return []

    window_norm = normalize_patient_time(patient["preferred_time"])
    patient_slots = patient_window_slots(window_norm)
    doctor_slots = doctor_slot_map[doctor]
    clinic_slots = set(expand_range_to_slots(clinic_hours_range))

    common = patient_slots & doctor_slots & clinic_slots
    return sorted(list(common))


def init_doctor_booked(doctors_data: list[dict]) -> dict[str, set[int]]:
    booked: dict[str, set[int]] = {}
    for d in doctors_data:
        booked[d["name"]] = set()
    return booked


def init_room_booked(room_list: list[int]) -> dict[int, set[int]]:
    booked: dict[int, set[int]] = {}
    for r in room_list:
        booked[r] = set()
    return booked


def is_doctor_free(doctor_booked: dict[str, set[int]], doctor: str, slot: int) -> bool:
    return slot not in doctor_booked[doctor]


def find_free_room(room_booked: dict[int, set[int]], room_list: list[int], slot: int) -> int | None:
    for r in room_list:
        if slot not in room_booked[r]:
            return r
    return None


def candidate_assignments_for_patient(
        patient: dict,
        doctor_slot_map: dict[str, set[int]],
        doctor_booked: dict[str, set[int]],
        room_booked: dict[int, set[int]],
        room_list: list[int],
        clinic_hours_range: tuple[int, int],
) -> list[tuple[int, int]]:
    doctor = patient["preferred_doctor"]
    slots = candidate_slots_for_patient(patient, doctor_slot_map, clinic_hours_range)

    assignments: list[tuple[int, int]] = []
    for slot in slots:
        if not is_doctor_free(doctor_booked, doctor, slot):
            continue
        room = find_free_room(room_booked, room_list, slot)
        if room is None:
            continue
        assignments.append((slot, room))

    return assignments


def schedule_appointments(
        doctors_data: list[dict],
        patients_data: list[dict],
        room_list: list[int],
        clinic_hours_range: tuple[int, int],
) -> list[dict] | None:
    doctor_slot_map = build_doctor_slot_map(doctors_data)
    doctor_booked = init_doctor_booked(doctors_data)
    room_booked = init_room_booked(room_list)

    def count_candidates(p: dict) -> int:
        return len(candidate_assignments_for_patient(
            p, doctor_slot_map, doctor_booked, room_booked, room_list, clinic_hours_range
        ))

    patients_ordered = sorted(patients_data, key=count_candidates)
    schedule: list[dict] = []

    def backtrack(idx: int) -> bool:
        if idx == len(patients_ordered):
            return True

        patient = patients_ordered[idx]
        doctor = patient["preferred_doctor"]

        options = candidate_assignments_for_patient(
            patient, doctor_slot_map, doctor_booked, room_booked, room_list, clinic_hours_range
        )

        for slot, room in options:
            doctor_booked[doctor].add(slot)
            room_booked[room].add(slot)
            schedule.append({
                "patient": patient["name"],
                "doctor": doctor,
                "slot": slot,
                "room": room,
            })

            if backtrack(idx + 1):
                return True

            schedule.pop()
            doctor_booked[doctor].remove(slot)
            room_booked[room].remove(slot)

        return False

    if backtrack(0):
        schedule.sort(key=lambda x: (x["slot"], x["doctor"], x["room"]))
        return schedule

    return None


def print_schedule(schedule: list[dict] | None) -> None:
    if schedule is None:
        print("No valid schedule found.")
        return

    print("Final Schedule:")
    for appt in schedule:
        slot = appt["slot"]
        print(f"- {appt['patient']} | {appt['doctor']} | {slot}:00-{slot + 1}:00 | Room {appt['room']}")


if __name__ == "__main__":
    result = schedule_appointments(doctors, patients, rooms, clinic_hours)
    print_schedule(result)
