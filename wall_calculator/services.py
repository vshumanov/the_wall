from django.conf import settings
from wall_calculator.utils import parse_input_file, calc_profile_workdays

from functools import cache


@cache
def get_ice_by_profile_and_day(profile_num: int, day: int) -> int:
    input_ = parse_input_file(settings.INPUT_FILE)
    return calc_profile_workdays(input_[profile_num - 1], day) * settings.ICE_PER_FT


@cache
def get_cost_by_profile(profile_num: int, day: int) -> int:
    input_ = parse_input_file(settings.INPUT_FILE)
    return (
        calc_profile_workdays(input_[profile_num - 1], day)
        * settings.ICE_PER_FT
        * settings.COST_PER_YARD_CUBED
    )


@cache
def get_overview_cost_for_day(day: int) -> int:
    input_ = parse_input_file(settings.INPUT_FILE)
    full_workdays = 0
    for profile in input_:
        full_workdays += calc_profile_workdays(profile, day)
    return full_workdays * settings.ICE_PER_FT * settings.COST_PER_YARD_CUBED


@cache
def get_full_cost() -> int:
    input_ = parse_input_file(settings.INPUT_FILE)
    full_workdays = 0
    for profile in input_:
        full_workdays += calc_profile_workdays(profile, 31)
    return full_workdays * settings.ICE_PER_FT * settings.COST_PER_YARD_CUBED
