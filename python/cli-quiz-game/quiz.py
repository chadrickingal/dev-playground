# CLI QUIZ GAME

def englishCheckAnswer(answer, question):
    match question :
        case 1: 
            if answer == "a":
                return 0
            else:
                return 1
        case 2: 
            if answer == "b":
                return 0
            else:
                return 1
        case 3: 
            if answer == "c":
                return 0
            else:
                return 1
        case 4: 
            if answer == "c":
                return 0
            else:
                return 1
        case 5: 
            if answer == "b":
                return 0
            else:
                return 1
        case 6: 
            if answer == "b":
                return 0
            else:
                return 1
        case 7: 
            if answer == "a":
                return 0
            else:
                return 1
        case 8: 
            if answer == "d":
                return 0
            else:
                return 1
        case 9: 
            if answer == "c":
                return 0
            else:
                return 1
        case 10: 
            if answer == "d":
                return 0
            else:
                return 1
        case _: 
            return 1


def englishQuestion(item):
    match item:
        case 1:
            print("1. Which sentence is grammatically correct?")
            print("  A. She don't like coffee.")
            print("  B. She doesn't likes coffee.")
            print("  C. She doesn't like coffee.")
            print("  D. She don't likes coffee.") 
            answer = input("Answer: ")
            return answer
        case 2:
            print("2. What is the synonym of \"rapid\"?")
            print("  A. Slow")
            print("  B. Fast")
            print("  C. Weak")
            print("  D. Quiet") 
            answer = input("Answer: ")
            return answer
        case 3:
            print("3. Which word is an adjective?")
            print("  A. Quickly")
            print("  B. Happiness")
            print("  C. Beautiful")
            print("  D. Run") 
            answer = input("Answer: ")
            return answer
        case 4:
            print("4. \"Neither John nor his friends ___ available.\"")
            print("  A. is")
            print("  B. was")
            print("  C. are")
            print("  D. be") 
            answer = input("Answer: ")
            return answer
        case 5:
            print("5. What is the opposite of \"ancient\"")
            print("  A. Historic")
            print("  B. Modern")
            print("  C. Traditional")
            print("  D. Old") 
            answer = input("Answer: ")
            return answer
        case 6:
            print("6. Which sentence uses the correct punctuation?")
            print("  A. \"Where are you going\".")
            print("  B. \"Where are you going?\"")
            print("  C. \"Where are you going\",")
            print("  D. \"Where are you going\"!") 
            answer = input("Answer: ")
            return answer
        case 7:
            print("7. What does \"ambiguous\" mean?")
            print("  A. Having more than one possible meaning")
            print("  B. Extremely difficult")
            print("  C. Completely false")
            print("  D. Easy to understand") 
            answer = input("Answer: ")
            return answer
        case 8:
            print("8. Which sentence is in the past perfect tense?")
            print("  A. She eats dinner.")
            print("  B. She ate dinner.")
            print("  C. She has eaten dinner.")
            print("  D. She had eaten dinner.")
            answer = input("Answer: ")
            return answer
        case 9:
            print("9. Choose the correct spelling.")
            print("  A. Definately")
            print("  B. Definitly")
            print("  C. Definitely")
            print("  D. Definetely") 
            answer = input("Answer: ")
            return answer
        case 10:
            print("10. In the sentence \"The cat quickly climbed the tree,\" what is \"quickly\"?")
            print("  A. Noun")
            print("  B. Verb")
            print("  C. Adjective")
            print("  D. Adverb") 
            answer = input("Answer: ")
            return answer
        case _:
            print("Question not found")
    



if __name__ == "__main__":
    expectedScore = 10
    totalScore = 0
    print("welcome to cli quiz\n")

    for item in range(1, expectedScore + 1):
       scorePerQuestion = englishCheckAnswer(englishQuestion(item), item)
       totalScore = expectedScore - scorePerQuestion

    print(totalScore)

## still in progress

