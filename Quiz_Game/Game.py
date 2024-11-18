
questions={
            
                 "What does 'CPU' stand for in computing?": ["A) Central Processing Unit", "B) Computer Processing Unit", "C) Central Printing Unit", "D) Computer Power Unit",'A'],
            
            
            
                "Which programming language is known as the language of the web?": ["A) Python", "B) JavaScript", "C) C++", "D) Java","B"],
                
            
            
                "Which of the following is used to write comments in Python?"
                : ["A) //", "B) #", "C) <!-- -->", "D) /* */","B"],
                
            
            
                 "What is the correct file extension for Python files?": ["A) .java", "B) .js", "C) .py", "D) .txt","C"],
                
            
       
        }




def playGame():
        score=0
        j=1
        print("                      Welcome to the Quiz Game")
        
        for i,q in (questions.items()):
            print(f"Question {j}: {i}")
            j+=1
            for option in range(3):
                print(q[option])

            ans=input("Answer: ").upper()

            if ans==q[4]:
                print("Correct Answer")
                score=score+2

            else:
                print("Wrong Answer")
                score=score-1
            
        print(f"            Your final Score is {score} out of 10")



playGame()
