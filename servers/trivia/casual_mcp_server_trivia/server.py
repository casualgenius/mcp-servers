from fastmcp import FastMCP
from pydantic import BaseModel, Field
from typing import Annotated, List, Optional, Literal
import random
import requests
from .cli import start_mcp

mcp = FastMCP(
    instructions=(
        "Trivia Quiz questions using the OpenTDB API.\n\n"
        "Use the `start_quiz` tool to retrieve the full set of questions you plan to use in a quiz session, "
        "always provide the `total_questions_for_quiz` parameter with the number of questions "
        "(e.g 5, 10, 20) needed for session."
    )
)


# --- Models ---

class TriviaCategory(BaseModel):
    id: int
    name: str

class TriviaQuestion(BaseModel):
    type: Literal["multiple choice", "true or false"]
    category: str
    difficulty: str
    question: str
    choices: Optional[List[str]] = None
    correct_answer: str

class TriviaResponse(BaseModel):
    questions: List[TriviaQuestion]

# --- Helpers ---

def map_question_type(api_type: str) -> str:
    return {
        "multiple": "multiple choice",
        "boolean": "true or false"
    }.get(api_type, "unknown")


def map_question_type_param(api_type: str) -> str:
    return {
        "multiple choice": "multiple",
        "true or false": "boolean"
    }.get(api_type, "unknown")

@mcp.tool(description="Get a list of available trivia categories.")
def list_categories() -> List[TriviaCategory]:
    response = requests.get("https://opentdb.com/api_category.php")
    response.raise_for_status()
    data = response.json()
    return [TriviaCategory(**cat) for cat in data.get("trivia_categories", [])]

@mcp.tool(description="Start a quiz by fetching the questions to be asked.")
def start_quiz(
    total_questions_for_quiz: Annotated[
        int, 
        Field(
            ge=1, 
            le=50, 
            description="Total questions to fetch at once for this quiz session (avoid multiple API calls)"
        )
    ],
    type: Annotated[
        Literal["multiple choice", "true or false", "mixture"], 
        Field(description="The types of questions to fetch: 'multiple choice', 'true or false' or 'mixture'.")
    ],
    category_id: Annotated[
        Optional[int],
        Field(description="Optional category to fetch questions from.")
    ] = None
) -> TriviaResponse:
    params = {"amount": total_questions_for_quiz}
    if category_id:
        params["category"] = category_id
    if not type == "mixture":
        params["type"] = map_question_type_param(type)

    response = requests.get("https://opentdb.com/api.php", params=params)
    response.raise_for_status()
    data = response.json()

    questions = []
    for item in data.get("results", []):
        choices = None
        if item["type"] == "multiple":
            choices = []
            choices.append(item["correct_answer"])
            choices.extend(item.get("incorrect_answers"))
            random.shuffle(choices)

        questions.append(
            TriviaQuestion(
                type=map_question_type(item["type"]),
                category=item["category"],
                difficulty=item["difficulty"],
                question=item["question"],
                correct_answer=item["correct_answer"],
                choices=choices
            )
        )

    return TriviaResponse(questions=questions)

# --- Entrypoint ---

def main() -> None:
    """Run the Trivia MCP server."""
    start_mcp(mcp, "Start the Trivia MCP server.")

if __name__ == "__main__":
    main()
