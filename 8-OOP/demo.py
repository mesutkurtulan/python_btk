# Question class hold some questions and answers
class Question:
    def __init__(self, text, choices, answer): # Text of the question, List of choices of the question, and answers of the question
        self.text = text            # Text of the question
        self.choices = choices      # List of choices of the question
        self.answer = answer        # Answers of the question

    def checkAnswer(self, answer):
        return self.answer == answer


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Question {self.questionIndex + 1} of {len(self.questions)}: {question.text}")

        for q in question.choices:
            print(f"- {q}")

        answer = input("Answer: ")
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print(f"Score: {self.score}")

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1
        if questionNumber > totalQuestion:
            print("Quiz completed!")
        else:
            print(f"Question: {questionNumber} of {totalQuestion}".center(50, "-"))


q1 = Question("What is the best programming language? ", ["java", "python", "go", "ruby"],"java")
q2 = Question("What is the most popular programming language? ", ["java", "python", "go", "ruby"],"java")
q3 = Question("What is the most advantageous programming language? ", ["java", "python", "go", "ruby"],"java")
q4 = Question("What is the easiest programming language? ", ["java", "python", "go", "ruby"],"java")
questions = [q1, q2, q3, q4]

quiz = Quiz(questions)
quiz.loadQuestion()