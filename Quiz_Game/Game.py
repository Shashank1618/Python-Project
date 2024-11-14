class QuizGame:
    def __init__(self):
        self.questions=[
            {
                "question": "What does 'CPU' stand for in computing?",
                "options": ["A) Central Processing Unit", "B) Computer Processing Unit", "C) Central Printing Unit", "D) Computer Power Unit"],
                "answer": "A"
            },
            {
                "question": "Which programming language is known as the language of the web?",
                "options": ["A) Python", "B) JavaScript", "C) C++", "D) Java"],
                "answer": "B"
            },
            {
                "question": "Which of the following is used to write comments in Python?",
                "options": ["A) //", "B) #", "C) <!-- -->", "D) /* */"],
                "answer": "B"
            },
            {
                "question": "What is the correct file extension for Python files?",
                "options": ["A) .java", "B) .js", "C) .py", "D) .txt"],
                "answer": "C"
            },
            {
                "question": "Which keyword is used to define a function in Python?",
                "options": ["A) function", "B) func", "C) def", "D) define"],
                "answer": "C"
            },
            {
                "question": "What symbol is used to terminate statements in Python?",
                "options": ["A) ;", "B) :", "C) .", "D) None"],
                "answer": "D"
            },
            {
                "question": "Which programming language is known for its simplicity and readability?",
                "options": ["A) C++", "B) JavaScript", "C) Python", "D) Java"],
                "answer": "C"
            },
            {
                "question": "What does 'HTML' stand for?",
                "options": ["A) HyperText Markup Language", "B) Hyperlink Text Mark Language", "C) Home Tool Markup Language", "D) Hyperlinking Text Management Language"],
                "answer": "A"
            },
            {
                "question": "Which of the following is NOT a programming language?",
                "options": ["A) Python", "B) HTML", "C) Java", "D) C++"],
                "answer": "B"
            },
            {
                "question": "What does 'IDE' stand for in software development?",
                "options": ["A) Integrated Development Environment", "B) Internet Development Environment", "C) Integrated Data Environment", "D) Intelligent Development Editor"],
                "answer": "A"
            }
       
        ]

        self.score=0

    def playGame(self):
        print("                      Welcome to the Quiz Game")\
        
        for i,q in enumerate(self.questions,1):
            print(f"Question {i}: {q['question']}")
            for option in q['options']:
                print(option)

            ans=input("Answer: ").upper()

            if ans==q['answer']:
                print("Correct Answer")
                self.score+=2

            else:
                print("Wrong Answer")
                self.score-=1
            
        print(f"            Your final Score is {self.score} out of 20")


game=QuizGame()
game.playGame()
