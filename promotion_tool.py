from langchain_core.tools import tool
from rag import retriever
from llm import llm


@tool
def promotion_tool(movie_story: str) -> str:
    """
    Create a movie promotion strategy.
    """
    docs = retriever.invoke(movie_story)
    context = "\n".join(
    doc.page_content[:300]
    for doc in docs
)
    prompt = f"""
    You are a movie marketing expert.

    Context:
    {context}

    Create:
    - Movie Poster Idea
    - Trailer Strategy
    - Social Media Campaign
    - Influencer Marketing
    - Release Promotions
    """

    return llm.invoke(prompt).content