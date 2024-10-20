from uagents import Agent, Context
from datetime import datetime, timedelta

class SchedulerAgent(Agent):
    def __init__(self, address: str):
        super().__init__(name="scheduler_agent", seed=address)
        self.schedule = []

    @staticmethod
    def str_to_time(time_str: str) -> datetime:
        return datetime.strptime(time_str, "%H:%M")

    @staticmethod
    def time_to_str(time_obj: datetime) -> str:
        return time_obj.strftime("%H:%M")

    async def add_schedule(self, ctx: Context, schedule_data: dict):
        """
        Receives a schedule and stores it for the user.
        Example schedule: [{'start_time': '09:00', 'end_time': '10:30'}, ...]
        """
        self.schedule = [(self.str_to_time(task['start_time']), self.str_to_time(task['end_time'])) for task in schedule_data['tasks']]
        ctx.logger.info(f"Schedule received: {self.schedule}")

    async def find_free_slots(self, ctx: Context):
        """
        Find free time slots in the user's schedule for workouts.
        Returns a list of free time slots.
        """
        day_start = self.str_to_time("08:00")  # Start of the day
        day_end = self.str_to_time("22:00")    # End of the day
        free_slots = []
        current_time = day_start

        self.schedule.sort(key=lambda x: x[0])

        for task_start, task_end in self.schedule:
            if current_time < task_start:
                free_slots.append((self.time_to_str(current_time), self.time_to_str(task_start)))
            current_time = max(current_time, task_end)

        if current_time < day_end:
            free_slots.append((self.time_to_str(current_time), self.time_to_str(day_end)))

        ctx.logger.info(f"Free slots: {free_slots}")
        return free_slots

# Example usage
async def run_scheduler():
    # Create an instance of SchedulerAgent
    scheduler_agent = SchedulerAgent(address="some_seed_or_address_here")

    # Example schedule data
    schedule_data = {
        "tasks": [
            {"start_time": "09:00", "end_time": "10:30"},
            {"start_time": "12:00", "end_time": "13:00"},
            {"start_time": "15:30", "end_time": "17:00"}
        ]
    }

    # Add schedule
    await scheduler_agent.add_schedule(Context(scheduler_agent), schedule_data)

    # Find free slots
    free_slots = await scheduler_agent.find_free_slots(Context(scheduler_agent))
    print("Free slots for workouts:", free_slots)

# You would call run_scheduler() as part of your agent's lifecycle.
