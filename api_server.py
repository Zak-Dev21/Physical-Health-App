from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from schedule_agent import SchedulerAgent, Context
from lifestyle_agent import LifestyleAgent
from workoutiming_agent import TimingAgent

app = FastAPI()

scheduler_agent = SchedulerAgent(address="some_seed_or_address")
lifestyle_agent = LifestyleAgent(address="some_seed_or_address")
timing_agent = TimingAgent(address="some_seed_or_address")

class Task(BaseModel):
    start_time: str
    end_time: str

class ScheduleData(BaseModel):
    tasks: List[Task]

class UserData(BaseModel):
    job_type: str
    activity_level: str
    goals: str

@app.post("/api/schedule")
async def receive_schedule(schedule_data: ScheduleData):
    task_list = [{"start_time": task.start_time, "end_time": task.end_time} for task in schedule_data.tasks]
    schedule_payload = {"tasks": task_list}
    await scheduler_agent.add_schedule(Context(scheduler_agent), schedule_payload)
    free_slots = await scheduler_agent.find_free_slots(Context(scheduler_agent))
    return {"free_slots": free_slots}

@app.post("/api/user_data")
async def receive_user_data(user_data: UserData):
    await lifestyle_agent.store_user_data(Context(lifestyle_agent), user_data.dict())
    return {"message": "User data stored"}

@app.get("/api/suggest_workout_time")
async def suggest_workout_time():
    # Assuming you already have free slots and energy level
    free_slots = await scheduler_agent.find_free_slots(Context(scheduler_agent))
    user_data = lifestyle_agent.user_data
    energy_level = "moderate"  # This could be dynamic based on more user info
    best_time = await timing_agent.suggest_best_time(Context(timing_agent), free_slots, energy_level)
    return {"best_workout_time": best_time}
