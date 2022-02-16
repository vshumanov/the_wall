# The Wall

DRF server to calculate cost of building a wall

Given a series of numbers, representing the initial heights
of different mile-long sections of the wall(Wall profile), in feet. Each of these
sections has its own construction crew that can add 1 foot of height per day. All
crews work simultaneously, meaning all sections that aren’t
completed (are less than 30 feet high) grow by 1 foot every day. When a section of
the wall is completed, its crew is relieved. Each foot added uses 195 cubic yards of
ice. To process one cubic yard, it costs the Night’s Watch 1900 "Gold Dragon"
coins for salaries and food for the brothers who work on it.

To install:
`poetry install`

To run:
`poetry run manage.py runserver`

Tests:
`poetry run manage.py tests`
