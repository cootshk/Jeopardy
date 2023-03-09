from pcolors import colors as c  #, backgrounds as b
import math

class gameboard:

    def __init__(self, questions: dict) -> None:
        self.answered = {}
        self.scores = []
        self.board = {}
        #Build board
        for question in questions:
            #Format
            question["Category"] = question["Category"].strip().title()
            question["Question"] = question["Question"].strip().capitalize()
            question["Answer"] = question["Answer"].strip().lower().replace(
                "who is ","").replace(
                "who are ","").replace(
                "what is ","").replace(
                "what are ", "").replace(
                ".", "").replace(
                "?","").capitalize()

            try:
                self.board[question["Category"].strip().title()].append(
                    question)
            except:
                self.board[question["Category"].strip().title()] = [question]
            i = 0
            for category in self.board:
               for question in list(self.board.values())[i]:
                   try:
                       self.answered[category].append(False)
                   except:
                        self.answered[category] = [False]

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
            output += f"{c.g}#  {c.w}{c.u}{category}{c.w}  "
        output += f"{c.g}#{c.w}\n{c.g}"
        for category in self.board:
            output += "###"
            for char in category:
                output += "#"
            output += "##"
        output += f"#{c.w}\n"
        #display questions
        num = 0
        for question in list(self.board.values())[0]:
            num += 1
        print("Total # of rows:",num)
        for points in range(num):
            for category in self.board:
                output += f"{c.g}#{c.b}"
                #number of spaces to insert
                insert = math.floor(len(category)/2)
                for space in range(insert):
                    output += " "
                if len(category) % 2 == 1:
                    output += " "
                #output = output.replace("  ",str(num*100),1)
                output += str((points+1)*100)
                for space in range(insert):
                    output += " "
                if len(category) % 2 == 0:
                    output + " "
                output += " "
            output += f"{c.g}#\n{c.w}"
            for category in self.board: #draw dividing line
                output += f"{c.g}###"
                for char in category:
                    output += "#"
                output += "##"
            output += f"#{c.w}\n"
        output += f"#{c.w}\n"
        output += f"{c.g}#\n"
        for category in self.board:
            output += "###"
            for char in category:
                output += "#"
            output += "##"
        output += f"#{c.w}\n"
        if not color:
            output = output.replace(c.w,"").replace(c.g,"").replace(c.b,"").replace(c.u,"")
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
        
    def answer_square(self, category: int | str, question: int, answer: str,team: int) -> bool:
        pass
        #get the category
        category = self.get_category(category)
        question = int(question)
        answer = answer.capitalize().strip().replace(".", "").replace("?","")
        if not (answer.startswith("What is") 
                or answer.startswith("Who is") 
                or answer.startswith("What are") 
                or answer.startswith("Who are")):
            raise ValueError("Your answer must start with 'who is', 'who are', 'what is', or 'what are'")
        #find which question is used
        for question in list(self.board.values())[category]:
            if True:
                break
        #change question to answered
        if True:
            pass
        else: 
            return False
        

if __name__ == "__main__": #If the file was run
    import json
    with open("Answers.json", "r") as f:
        musclequestions = json.load(f) #tested on muscle question data
    board = gameboard(musclequestions)
    #while True:
    #game loop
    c.clear()
    print(board.print_board())
