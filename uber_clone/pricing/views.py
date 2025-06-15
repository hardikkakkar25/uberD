# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PricingConfig
from datetime import datetime

def get_active_config_for_day(day):
    return PricingConfig.objects.filter(is_active=True, days_applicable__contains=[day]).first()

class CalculatePriceAPI(APIView):
    def post(self, request):
        data = request.data
        distance_km = float(data.get("distance_km", 0))
        ride_minutes = float(data.get("ride_minutes", 0))
        wait_minutes = float(data.get("wait_minutes", 0))
        day = data.get("day", datetime.today().strftime("%a"))

        config = get_active_config_for_day(day)
        if not config:
            return Response({"error": "No active pricing config found for this day"}, status=400)

        # Base Distance Logic
        base_price = config.base_price
        if distance_km > config.base_distance_km:
            additional_distance = distance_km - config.base_distance_km
        else:
            additional_distance = 0

        dap = additional_distance * config.additional_price_per_km

        # Time Multiplier Logic
        time_multiplier = 1.0
        for tier in config.time_multipliers.all():
            if ride_minutes <= tier.upper_limit_minutes:
                time_multiplier = tier.multiplier
                break

        # Waiting Charges
        excess_wait = max(wait_minutes - config.free_wait_minutes, 0)
        wait_blocks = excess_wait // 3
        wait_cost = wait_blocks * config.wait_charge_per_3min

        final_price = (base_price + dap) * time_multiplier + wait_cost

        return Response({
            "base_price": base_price,
            "additional_distance": additional_distance,
            "distance_price": dap,
            "time_multiplier": time_multiplier,
            "wait_cost": wait_cost,
            "total_price": round(final_price, 2)
        })
