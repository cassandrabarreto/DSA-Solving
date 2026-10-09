"""
    You're building a monitoring tool for a fleet of servers. Each server
    writes its own log file, and within a single server's log, entries are
    already in chronological order (timestamps only increase). However,
    different servers' logs are completely separate files.

    Write a function, merge_server_logs, that takes in a list of server
    logs, where each log is a list of (timestamp, message) tuples, already
    sorted by timestamp within each individual server's log.

    Return a single list of (timestamp, message) tuples representing all
    log entries from every server, merged together in overall chronological
    order.

    Example:
    merge_server_logs([
        [(1, "server-A: boot"), (5, "server-A: ready")],
        [(2, "server-B: boot"), (4, "server-B: ready"), (9, "server-B: shutdown")],
    ])
    # -> [(1, "server-A: boot"), (2, "server-B: boot"), (4, "server-B: ready"),
    #     (5, "server-A: ready"), (9, "server-B: shutdown")]

    Assume timestamps across all servers are unique (no ties to worry about).

"""
import heapq
def merge_server_logs(logs):
    final_result = []

    # we need to retrieve each logs elem
    my_heap = []

    pass

