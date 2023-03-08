from pcolors import colors as c  #, backgrounds as b


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

    def print_board(self, *, color:bool=True) -> str:
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
        #display questions
        i = 0
        for category in self.board:
            pass
            i += 1
        if not color:
            output = output.replace(c.w,"").replace(c.g,"").replace(c.b,"")
        return output
    def get_category(self,category: int | str):
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
    def get_question(self,category: int | str, question: int | str) -> str: 
        pass
    def view_square(self, category: int | str, question: int) -> str:
        category = self.get_category(category)
        question = int(question)
        
    def answer_square(self, category: int | str, question: int, answer: str) -> bool:
        pass
        #get the category
        category = self.get_category(category)
        question = int(question)
        if answer.startswith():
            pass


if __name__ == "__main__":
    import json
    with open("Answers.json", "r") as f:
        musclequestions = json.load(f)
    board = gameboard(musclequestions)
    #while True:
    #game loop
    c.clear()
    print(board.print_board())
