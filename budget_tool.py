from langchain_core.tools import tool
from rag import retriever
from llm import llm


@tool
def budget_tool(movie_story: str) -> str:
    """
    Estimate the production budget.
    """
    docs = retriever.invoke(movie_story)
    context = "\n".join(
    doc.page_content[:300]
    for doc in docs
)

    prompt = f"""
    You are a movie budget analyst.

    Context:
    {context}

    Estimate:
    - Production Cost
    - Cast Cost
    - VFX Cost
    - Marketing Cost
    - Total Budget
    """

    return llm.invoke(prompt).content