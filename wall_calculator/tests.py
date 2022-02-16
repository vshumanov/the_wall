from django.test import TestCase, override_settings
from wall_calculator.services import (
    get_ice_by_profile_and_day,
    get_cost_by_profile,
    get_overview_cost_for_day,
    get_full_cost,
)


@override_settings(INPUT_FILE="test_input")
class TestOverviewPerProfile(TestCase):
    def test_ice_profile(self):
        ice = get_ice_by_profile_and_day(2, 1)
        self.assertEqual(ice, 195)

    def test_ice_exception(self):
        with self.assertRaises(IndexError):
            ice = get_ice_by_profile_and_day(5, 1)

    def test_profile_cost_day(self):
        cost = get_cost_by_profile(1, 1)
        self.assertEqual(cost, 1111500)

    def test_profile_cost_exception(self):
        with self.assertRaises(IndexError):
            cost = get_cost_by_profile(5, 1)


@override_settings(INPUT_FILE="test_input")
class TestFullOverview(TestCase):
    def test_cost_for_day(self):
        cost = get_overview_cost_for_day(1)
        self.assertEqual(cost, 1482000)

    def test_full_cost(self):
        cost = get_full_cost()
        self.assertEqual(cost, 13338000)
