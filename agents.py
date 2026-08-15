from langchain.agents import create_agent
from llm import llm

from tools.script_tool import script_tool
from tools.casting_tool import casting_tool
from tools.budget_tool import budget_tool
from tools.location_tool import location_tool
from tools.editing_tool import editing_tool
from tools.promotion_tool import promotion_tool
from tools.release_strategy_tool import release_strategy_tool

print("script_tool:", type(script_tool))
print("casting_tool:", type(casting_tool))
print("budget_tool:", type(budget_tool))
print("location_tool:", type(location_tool))
print("editing_tool:", type(editing_tool))
print("promotion_tool:", type(promotion_tool))
print("release_strategy_tool:", type(release_strategy_tool))

movie_agent = create_agent(
    model=llm,
    tools=[
        script_tool,
        casting_tool,
        budget_tool,
        location_tool,
        editing_tool,
        promotion_tool,
        release_strategy_tool,
    ],
    system_prompt="""
You are an AI Movie Production Team with seven specialized departments.

Departments:
1. Script Department
   - Write movie stories, screenplays, dialogues, and character development.

2. Casting Department
   - Recommend actors, actresses, directors, and supporting cast.

3. Budget Department
   - Estimate production, cast, VFX, equipment, and marketing costs.

4. Location Department
   - Recommend filming locations, studios, and countries.

5. Editing Department
   - Suggest editing style, VFX, sound design, background music, and color grading.

6. Promotion Department
   - Create posters, trailers, social media campaigns, and promotional strategies.

7. Release Strategy Department
   - Recommend release dates, theatrical or OTT release, film festivals,
     international distribution, marketing timeline, and box office strategy.

Always select ONLY the most relevant tool based on the user's request.
Do not call unnecessary tools.
If the user asks about multiple departments, use the required tools and combine their results into a single response.
"""
)