

""" 
Write a function, prereqs_possible, that takes in a number of courses (n) 
and prerequisites as arguments. Courses have ids ranging from 0 through n - 1. 
A single prerequisite of (A, B) means that course A must be taken before course B. 
The function should return a boolean indicating whether or not it is possible to complete all courses.

numCourses = 6
prereqs = [
  (0, 1),
  (2, 3),
  (0, 2),
  (1, 3),
  (4, 5),
]
"""
def prereqs_possible(num_courses: int, prereqs:list[tuple]):
    visiting = set()
    visited = set()

    graph = convert(prereqs, num_courses)

    for node in graph:
        if has_cycle(graph, node, visiting, visited):
            return False
    return True



def convert(prerequisites: list[tuple], courses_number: int) -> dict[str, list[str]]:
    graph = {}

    for i in range(0, courses_number):
        graph[i] = []

    for prerequisite in prerequisites:
        course_a , course_b = prerequisite
        graph[course_a].append(course_b)
    return graph

def has_cycle(graph: dict[str, list[str]], node, visiting, visited):
    if node in visited:
        return False
    
    if node in visiting:
        return True
    
    visiting.add(node)

    for neighbour in graph[node]:
        if has_cycle(graph, neighbour, visiting, visited):
            return True
    
    visiting.remove(node)
    visited.add(node)
    return False