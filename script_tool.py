from langchain_core.tools import tool
from rag import retriever
from llm import llm

@tool
def script_tool(movie_idea: str) -> str:
    """
Generate a complete movie script including story,
characters, dialogues, climax, ending,
screenplay structure, etc...
"""
    docs = retriever.invoke(movie_idea)
    context = "\n".join(
    doc.page_content[:300]
    for doc in docs
)

    prompt = f"""
    You are an expert screenplay writer.

    Context:
    {context}

    Movie Idea:
    {movie_idea}

    Write:
    - Title
    - Story
    - Characters
    - Plot
    - Ending
    """

    return llm.invoke(prompt).content