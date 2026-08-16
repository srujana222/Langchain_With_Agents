from langchain_core.tools import tool
from rag import retriever
from llm import llm


@tool
def location_tool(movie_story: str) -> str:
    """
    Recommend filming locations.
    """
    docs = retriever.invoke(movie_story)
    context = "\n".join(
    doc.page_content[:300]
    for doc in docs
)

    prompt = f"""
    You are a movie location expert.

    Context:
    {context}

    Recommend:
    - Indoor Locations
    - Outdoor Locations
    - Country
    - City
    - Studio
    """

    return llm.invoke(prompt).content