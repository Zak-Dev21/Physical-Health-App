from uagents import Agent, Context
from datetime import datetime, timedelta

class TimingAgent(Agent):
    def __init__(self, address: str):
        super().__init__(name="timing_agent", seed=address)

    async def suggest_best_time(self, ctx: Context, schedule: list, energy_level: str):
        """
        Suggests the best time for workouts based on user schedule and energy level.
        """
        best_time = None
        # Assuming energy levels can be 'low', 'moderate', 'high'
        if energy_level == "high":
            best_time = schedule[0] if schedule else "No available time today"
        elif energy_level == "moderate":
            # Pick the mid-point of free time slots
            best_time = schedule[len(schedule) // 2] if schedule else "No available time today"
        else:  # low energy
            # Suggest rest or light workout
            best_time = "Consider rest or light stretching today"

        ctx.logger.info(f"Suggested best time for workout: {best_time}")
        return best_time
