import threading


class TicketBooking:
    def __init__(self):
        self._lock = threading.Lock()
        self._seat_owners = {}

    def book_seat(self, seat_id: str, visitor_id : str) -> bool:
        with self._lock:
            # Check
            if seat_id in self._seat_owners:
                return False
            # Update
            self._seat_owners[seat_id] = visitor_id
            return True
