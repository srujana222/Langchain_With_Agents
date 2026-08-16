from langchain_core.tools import tool
from rag import retriever
from llm import llm


@tool
def casting_tool(movie_story: str) -> str:
    """
    Suggest actors for the movie.
    """
    docs = retriever.invoke(movie_story)
    context = "\n".join(
    doc.page_content[:300]
    for doc in docs
)

    prompt = f"""
    You are a professional casting director.

    Context:
    {context}

    Movie:
    {movie_story}

    Suggest:
    - Hero
    - Heroine
    - Villain
    - Supporting Actors
    """

    return llm.invoke(prompt).content