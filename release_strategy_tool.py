from langchain_core.tools import tool
from rag import retriever
from llm import llm

@tool
def release_strategy_tool(movie_story: str) -> str:
    """
    Suggest the best release strategy
     for a movie based on its story, genre, and target audience.
    """

    docs = retriever.invoke(movie_story)
    context = "\n".join(
    doc.page_content[:300]
    for doc in docs
)

    prompt = f"""
    You are an experienced movie distribution and release strategy consultant.

    Use the context below to recommend the best release plan.

    Context:
    {context}

    Movie Details:
    {movie_story}

    Provide the following:

    1. Recommended Release Date
    2. Target Audience
    3. Release Type (Theatrical / OTT / Hybrid)
    4. Domestic Release Plan
    5. International Release Plan
    6. Film Festival Recommendations
    7. Distribution Strategy
    8. Marketing Timeline
    9. Box Office Strategy
    10. OTT Release Window
    11. Risk Analysis
    12. Final Recommendation

    Give the response in a clear and professional format.
    """

    response = llm.invoke(prompt)
    return response.content