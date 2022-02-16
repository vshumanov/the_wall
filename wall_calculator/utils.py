from typing import List
from functools import cache


@cache
def parse_input_file(file_path: str) -> List[List[int]]:
    """Parse a file with the following format:
    21 22 24
    12
    7 21 23

    Returns each line as integers in a nested list
    """
    with open(file_path) as input_file:
        parsed_file = [list(map(int, line.split())) for line in input_file.readlines()]
    return parsed_file


def calc_crew_workdays(start_height: int, max_day: int) -> int:
    """Returns how many days would have a crew worked from a starting point `start_height`
    until a `max_day`, bounded to 30
    """
    return max_day if start_height + max_day <= 30 else 30 - start_height


def calc_profile_workdays(profile: List[int], max_day: int) -> int:
    crew_workdays = 0
    for crew_curr_height in profile:
        crew_workdays += calc_crew_workdays(crew_curr_height, max_day)
    return crew_workdays
