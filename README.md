# **Jeopardy**

## Using as a library
```py
import main
board = gameboard(questions=[]) #See input structure below
print(board.print_board())
```

## Using as a file
The program will load an `Answers.json` file from the active directory, then use it as an input.

## Input Structure
```json
[
    {
        "Question": "your question here",
        "Answer": "what is your answer",
        "Points": 100,
        "Category": "What is your category 1"
    },
    {
        "Question": "your question here",
        "Answer": "what is your answer",
        "Points": 200,
        "Category": "What is your category 2"
    },
    ...
    {
        "Question": "your question here",
        "Answer": "what is your answer",
        "Points": 300,
        "Category": "What is your category"
    }
]
```