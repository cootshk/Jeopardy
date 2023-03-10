from pcolors import colors as c#, backgrounds as b #Text coloring
import math

class gameboard:

    def __init__(self, questions: dict, teams: int=2) -> None:
        self.answered = []
        self.scores = []
        assert teams >= 1, "You need at least one team" #I love python 2
        for team in range(teams):
            self.scores.append(0)
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
                "?","").capitalize().strip()

            try:
                self.board[question["Category"].strip().title()].append(
                    question)
            except:
                self.board[question["Category"].strip().title()] = [question]
            i=0    
            for category in self.board: #build answered list
                for question in self.board[category]:
                   try:
                       self.answered[i].append(False)
                   except:
                        try:
                            self.answered[i] = [False]
                        except:
                            self.answered.append([False])
                i += 1

    def print_board(self, *, color:bool=True) -> str:
        #print(self.scores)
        #print(self.answered)
        output = c.g
        for category in self.board:
            output += "###"
            for char in category:
                output += "#"
            output += "##"
        #output = output.replace("###","",1) #remove the extra hashtags
        output += "#\n"
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
        #print("Total # of rows:",num)
        i=0
        for points in range(num):
            j=0
            for category in self.board:
                output += f"{c.g}#{c.r if self.answered[j][i] else c.b}"
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
                j += 1
            output += f"{c.g}#\n{c.w}"
            for category in self.board: #draw dividing line
                output += f"{c.g}###"
                for char in category:
                    output += "#"
                    
                output += "##"
            output += f"#{c.w}\n"
            i += 1
        output += f"\n{c.g}#######################\n#  {c.w}Team #   {c.g}#  {c.w}Score{c.g}  #\n#######################\n" if len(self.scores) < 10 else f"\n{c.g}########################\n#  {c.w}Team #    {c.g}#  {c.w}Score{c.g}  #\n########################\n"
        i = 0
        for team in self.scores: #display scores
            output += f"{c.g}#  {c.w}Team {i+1}:  {c.g}#{c.b}{f'    {team}    ' if len(str(self.scores[i])) == 1 else f'   {team}    ' if len(str(self.scores[i])) == 2 else f'   {team}   ' if len(str(self.scores[i])) == 3 else f'  {team}   '}{c.g}#\n"
            if i == 8:
                output = output.replace(":",": ").replace("#   #" ,"#    #")
            elif i == 98:
                output = output.replace(":",": ").replace("#   #" ,"#    #")
            #elif i == 10:
            #    output = output.replace("10: ","10:")
            #elif i == 100:
            #    output = output.replace("100: ","100:")
            i += 1
        output += f"{c.g}#######################{c.w}" if len(self.scores) < 10 else f"{c.g}########################{c.w}"
        if not color:
            output = output.replace(c.w,"").replace(c.g,"").replace(c.b,"").replace(c.u,"").replace(c.r, "")
        return output
    def get_category(self,category: int | str) -> int:
        try:
            category = int(category)
        except:
            pass
        if isinstance(category,int):
            #assert category > 0, "Please choose a valid category!"
            #print("category: ",category)
            if category >= len(list(self.board.keys())) or category < 1:
                raise AssertionError("Please choose a valid category!")
            category -= 1
        else: 
            category = category.strip().title()
            try:
                category = int(category)
            except:
                i = 1
                for group in list(self.board.values()):
                    pass
                    if group[i]["Category"] == category:
                        break
                    else:
                        i += 1
                        if i > len(group):
                            raise ValueError("That is not a category!")
                        continue
                category = i
        return int(category)
        #else:
        #    raise TypeError("The category input should be either the # or the name of the category")
    def get_scores(self, team:int=0):
        return self.scores if team == 0 else self.scores[team-1]
    def get_question(self,category: str, question: int) -> str:
        return list(self.board.values())[self.get_category(category)][int(question)-1]["Question"]
    def get_answer(self,category: int | str, question: int | str) -> str:
        return list(self.board.values())[self.get_category(category)][int(question)-1]["Answer"]
    def view_square(self, category: int | str, question: int,*,color:bool=True) -> str:
        try:
            category = int(category)
        except:
            category = str(category)
        question = self.get_question(category,question)
        category = self.get_category(category)
        #Draw box
        output = f"{c.g}###"
        for char in question:
            output += "#"
        output += f"###\n#  {c.b}{question}  {c.g}#\n###"
        for char in question:
            output += "#"
        output += f"###{c.w}"
        return output if color else output.replace(c.g,"").replace(c.w,"").replace(c.b,"").replace(c.u,"")
    def answer_square(self, category: int | str, question: int, answer: str,team: int) -> bool:
        pass
        #get the category
        category = self.get_category(category)
        question = int(question)-1
        answer = answer.capitalize().strip().replace(".", "").replace("?","")
        if not (answer.startswith("What is") 
                or answer.startswith("Who is") 
                or answer.startswith("What are") 
                or answer.startswith("Who are")):
            raise ValueError("Your answer must start with 'who is', 'who are', 'what is', or 'what are'")
        correct = self.get_answer(category+1,question) #i messed up the indexing. dont ask
        #change question to answered
        if answer.replace("Who is ", "").replace("Who are ","").replace("What is ","").replace("What are ","").strip().capitalize() == correct: 
            self.answered[category][question] = True
            return True
        else: 
            #print(f"category is {category} and question is {question}")
            self.answered[category][question] = True
            return False
    def __repr__(self):
        return self.print_board(color=False)
    def add_score(self, team: int, score: int):
        self.scores[team-1] += score
            

if __name__ == "__main__": #If the file was run
    import json
    with open("Answers.json", "r") as f:
        musclequestions = json.load(f) #tested on muscle question data
    while True: #setup
        try:
            players = int(input(f"{c.w}How many teams would you like? > {c.p}"))
            activeplayer = 1
            board = gameboard(musclequestions,players)
            break
        except Exception as e:
            if isinstance(e, KeyboardInterrupt):
                exit()
            elif isinstance(e, AssertionError):
                print(f"{c.w}Please enter a valid number of teams!")
            else:
                raise e
    while True: #game loop
        c.clear()
        print(board.print_board())
        category=input(f"{c.w}Choose a category # > {c.p}")
        question=int(input(f"{c.w}Choose a question (1, 2, etc.) > {c.p}").strip())
        try:
            c.clear()
            print(board.view_square(category,question))
            answer = input(f"{c.w}What is your answer? > {c.p}").capitalize().strip().replace(".", "").replace("?","")
            try:
                correct = board.answer_square(category, question, answer, activeplayer)
            except:
                activeplayer -= 1
                raise TypeError("Your answer must start with 'who is', 'who are', 'what is', or 'what are'")
            c.clear()
            if not correct:
                if input(f"{c.w}The answer was {board.get_answer(category,question)}.\nYou answered {answer}. Were you correct? (Y/N)> {c.p}").lower()[0] == "y":
                    c.clear()
                    correct = True
                    board.add_score(team=activeplayer, score=int(question*100))
                else:
                    board.add_score(activeplayer, int(question*-100))
            else:
                board.add_score(activeplayer, int(question*100))
            print(f"{c.g}##############\n#  {c.b}Correct!  {c.g}#\n##############{c.w}" if correct else f"{c.g}################\n#  {c.r}Incorrect!  {c.g}#\n################{c.w}")
            input(f"{c.w}press enter to continue")
        except Exception as e:
            if isinstance(e,KeyboardInterrupt):
                exit()
            elif isinstance(e,AssertionError):
                print(f"{c.r}Please choose a valid category!{c.w}")
            elif isinstance(e,ValueError):
                print(f"{c.r}Please choose a valid question!{c.w}")
            #elif isinstance(e,TypeError):
                print(f"{c.r}Your answer must start with 'who is' or 'what is'!{c.w}")
            else:
                raise e
            exit() if input("press enter to continue") == "exit" else print()
        activeplayer += 1
        if activeplayer > players:
            activeplayer = 1