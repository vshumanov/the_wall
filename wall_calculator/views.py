from rest_framework import views, status
from rest_framework.response import Response

from wall_calculator.serializers import CostSerializer, QuantitySerializer
from wall_calculator.services import (
    get_ice_by_profile_and_day,
    get_cost_by_profile,
    get_overview_cost_for_day,
    get_full_cost,
)


class ProfileDay(views.APIView):
    def get(self, request, profile_num, day):
        try:
            return Response(
                QuantitySerializer(
                    {
                        "day": day,
                        "ice_amount": get_ice_by_profile_and_day(profile_num, day),
                    }
                ).data
            )
        except IndexError:
            return Response(
                {"error": "profile not found"}, status=status.HTTP_404_NOT_FOUND
            )


class ProfileOverview(views.APIView):
    def get(self, request, profile_num, day):
        try:
            return Response(
                CostSerializer(
                    {"day": day, "cost": get_cost_by_profile(profile_num, day)}
                ).data
            )
        except IndexError:
            return Response(
                {"error": "profile not found"}, status=status.HTTP_404_NOT_FOUND
            )


class FullOverview(views.APIView):
    def get(self, request):
        return Response(CostSerializer({"day": None, "cost": get_full_cost()}).data)


class FullOverviewDay(views.APIView):
    def get(self, request, day):
        return Response(
            CostSerializer({"day": day, "cost": get_overview_cost_for_day(day)}).data
        )
