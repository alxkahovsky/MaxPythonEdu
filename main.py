from datetime import datetime, timedelta, time


RANGE = (8, 20)
STEP = 15


def slots(cur_date: datetime):
    slots = []
    start_slot = cur_date.replace(hour=RANGE[0], minute=0, second=0, microsecond=0)
    end_slot = cur_date.replace(hour=RANGE[1], minute=0, second=0, microsecond=0)
    slot = start_slot
    while start_slot <= slot <= end_slot:
        slots.append(slot)
        slot = slot + timedelta(minutes=STEP)

    return tuple(slots)


def search(hour, minute, slotss):
    # ToDo [ ] запилить двоичный поиск!
    for slot in slotss:
        if slot.hour == hour:
            user_slot = slot.replace(minute=minute)
            check_slot = slot + timedelta(minutes=14)
            if user_slot <= check_slot:
                return slot


s = slots(datetime.now())
print(search(9, 38, s))












