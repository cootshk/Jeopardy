import json
from pcolors import colors as c  #, backgrounds as b

with open("Answers.json", "r") as f:
    musclequestions = json.load(f)


class gameboard:

    def __init__(self, questions: dict) -> None:
        self.board = {}
        #Build board
        for question in questions:
            #Format
            question["Category"] = question["Category"].strip().title()
            question["Question"] = question["Question"].strip().title()
            question["Answer"] = question["Answer"].strip().lower().replace(
                "who is ","").replace(
                "who are ","").replace(
                "what is ","").replace(
                "what are ", "").title()

            try:
                self.board[question["Category"].strip().title()].append(
                    question)
            except:
                self.board[question["Category"].strip().title()] = [question]

    def print_board(self) -> str:
        output = c.g
        for category in self.board:
            output += "###"
            for char in category:
                output += "#"
            output += "###"
        output = output.replace("###","",1) #remove 2 extra hashtags
        output += f"{c.w}\n"
        for category in self.board:
            output += f"{c.g}#  {c.w}{category}  "
        output += f"{c.g}#{c.w}\n{c.g}"
        for category in self.board:
            output += "###"
            for char in category:
                output += "#"
            output += "##"
        output += f"#{c.w}\n"
        if __debug__:
            print(self.board)
        #display questions
        i = 0
        for category in self.board:
            pass
            i += 1
        return output
    def view_square(self, category: int | str, question: int) -> str:
        pass
    def answer_square(self, category: int | str, question: int, answer: str) -> bool:
        pass
        #get the category
        if isinstance(category,int):
            pass
        elif isinstance(category,str):
            category = category.strip().title()
            try:
                category = int(category)
            except:
                i = 1
                for group in self.board:
                    pass
                    if group[0]["Category"] == category:
                        break
                    else:
                        i += 1
                        if i > len(group):
                            raise ValueError
                        continue
                category = i
        else:
            raise TypeError("The category input should be either the # or the name of the category")
        question = int(question)
        if answer.startswith()


if __name__ == "__main__":
    board = gameboard(musclequestions)
    #while True:
    #game loop
    c.clear()
    print(board.print_board())
