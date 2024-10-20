from uagents import Agent, Context

class LifestyleAgent(Agent):
    def __init__(self, address: str):
        super().__init__(name="lifestyle_agent", seed=address)
        self.user_data = {}

    async def store_user_data(self, ctx: Context, user_data: dict):
        """
        Stores user information: job type, activity level, and goals.
        """
        self.user_data = {
            "job_type": user_data["job_type"],
            "activity_level": user_data["activity_level"],
            "goals": user_data["goals"]
        }
        ctx.logger.info(f"User data stored: {self.user_data}")

# Example usage
async def run_lifestyle_agent():
    # Create an instance of LifestyleAgent
    lifestyle_agent = LifestyleAgent(address="some_seed_or_address")

    # Example user data
    user_data = {
        "job_type": "sedentary",  # Can be 'sedentary' or 'physical'
        "activity_level": "low",  # Can be 'low', 'moderate', 'high'
        "goals": "increase strength"  # User goal
    }

    # Store user data
    await lifestyle_agent.store_user_data(Context(lifestyle_agent), user_data)
