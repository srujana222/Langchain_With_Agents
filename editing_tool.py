from langchain_core.tools import tool
from rag import retriever
from llm import llm



@tool
def editing_tool(movie_story: str) -> str:
    """
    Suggest editing and post-production plan.
    """
    docs = retriever.invoke(movie_story)
    context = "\n".join(
    doc.page_content[:300]
    for doc in docs
)

    prompt = f"""
    You are a professional film editor.

    Context:
    {context}

    Suggest:
    - Editing Style
    - Color Grading
    - Background Music
    - VFX
    - Final Runtime
    """

    return llm.invoke(prompt).content