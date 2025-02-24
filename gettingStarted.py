### welcome_assignment_answers
### Input - All nine questions given in the assignment.
### Output - The right answer for the specific question.

def welcome_assignment_answers(question):
    #Students do not have to follow the skeleton for this assignment.
    #Another way to implement is using a "case" statements similar to C.
    if question == "In Slack, what is the secret passphrase posted in the lab channel? : ":
        result1 = input(question)
        if result1.lower() == "tiktok":
            answer = "Correct"
        else:
            answer = "Incorrect"
    
    elif question == "Are encoding and encryption the same? - Yes/No : ":
        result2 = input(question)
        if result2.lower() == "no":
            answer = "Correct"
        else:
            answer = "Incorrect"
    
    elif question == "Is it possible to decrypt a message without a key? - Yes/No : ":
        result3 = input(question)
        if result3.lower() == "no":
            answer = "Correct"
        else:
            answer = "Incorrect"

    elif question == "Is it possible to decode a message without a key? - Yes/No : ":
        result4 = input(question)
        if result4.lower() == "yes":
            answer = "Correct"
        else:
            answer = "Incorrect"
    
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No : ":
        result5 = input(question)
        if result5.lower() == "yes":
            answer = "Correct"
        else:
            answer = "Incorrect"
    
    elif question == "What is the SHA256 hashing value of your NYU email? - enter hashcode : ":
        result6 = input(question)
        if result6.lower() == "sha256":
            answer = "Correct"
        else:
            answer = "Incorrect"
    
    elif question == "Is MD5 a secured hashing algorithm? - Yes/No : ":
        result7 = input(question)
        if result7.lower() == "yes":
            answer = "Correct"
        else:
            answer = "Incorrect"
    
    elif question == "What layer of the TCP/IP model does the protocol DNS belong to? - enter integer number : ":
        result8 = int(input(question))
        if result8 == 4:
            answer = "Correct"
        else:
            answer = "Incorrect"
    
    elif question == "What layer of the TCP/IP model does the protocol ICMP belong to? - enter integer number : ":
        result9 = int(input(question))
        if result9 == 3:
            answer = "Correct"
        else:
            answer = "Incorrect"
    
    else: 
        ### you should understand why this else case should be included
        ### what happens if there is a typo in one of the questions?
        ### maybe put something here to flag an issue and catch errors
        answer = "This is not my beautiful wife! This is not my beautiful car! How did I get here?"
    return(answer)
# Complete all the questions.


if __name__ == "__main__":
    #use this space to debug and verify that the program works
    question1 = "In Slack, what is the secret passphrase posted in the lab channel? : "
    print(welcome_assignment_answers(question1))

    question2 = "Are encoding and encryption the same? - Yes/No : "
    print(welcome_assignment_answers(question2))

    question3 = "Is it possible to decrypt a message without a key? - Yes/No : "
    print(welcome_assignment_answers(question3))

    question4 = "Is it possible to decode a message without a key? - Yes/No : "
    print(welcome_assignment_answers(question4))

    question5 = "Is a hashed message supposed to be un-hashed? - Yes/No : "
    print(welcome_assignment_answers(question5))

    question6 = "What is the SHA256 hashing value of your NYU email? - enter hashcode : "
    print(welcome_assignment_answers(question6))

    question7 = "Is MD5 a secured hashing algorithm? - Yes/No : "
    print(welcome_assignment_answers(question7))

    question8 = "What layer of the TCP/IP model does the protocol DNS belong to? - enter integer number : "
    print(welcome_assignment_answers(question8))

    question9 = "What layer of the TCP/IP model does the protocol ICMP belong to? - enter integer number : "
    print(welcome_assignment_answers(question9))

#Questions:
#"In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
#"Are encoding and encryption the same? - Yes/No":
#"Is it possible to decrypt a message without a key? - Yes/No":
#"Is it possible to decode a message without a key? - Yes/No":
#"Is a hashed message supposed to be un-hashed? - Yes/No":
#"What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
#"Is MD5 a secured hashing algorithm? - Yes/No":
#"What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
#"What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
