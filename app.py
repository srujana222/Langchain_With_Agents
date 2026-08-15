from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agents import movie_agent

app = FastAPI(
    title="AI Movie Production Team",
    version="1.0.0",
    description="AI Movie Production Team using LangChain + RAG"
)

class MovieRequest(BaseModel):
    query: str



@app.post("/generate")
def generate(request: MovieRequest):
    try:
        response = movie_agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": request.query
                    }
                ]
            }
        )

        # Get the final AI message content
        result = response["messages"][-1].content

        return result

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )