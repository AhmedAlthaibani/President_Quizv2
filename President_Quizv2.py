import random

class President:
    def __init__(self, name, termStart, termEnd):
        self.name = name
        self.termStart = termStart
        self.termEnd = termEnd

def greeting():
    print("Hello! Please enter your name!")
    name = input()
    print("Hi", name)
    print("---Welcome to Ahmed's Presidential Quiz!---")

def rules():
    print("Would you like to play? Yes or No?")
    if input() == "Yes":
        print("The rules are simple! Just choose the President which served first out of the three options displayed! \nOne catch though! You only have three lives before you fail!\nLets get started!")

def choices():
    randomPresident = random.choice(presidentList)
    presidentList.remove(randomPresident)
    return President(randomPresident[0],randomPresident[1],randomPresident[2])

def correctAnswer(x):
    if x == "1":
        if p1.termStart < p2.termStart & p3.termStart:
            print("Correct!")
        elif p1.termEnd < p2.termEnd & p3.termEnd:
            print("Correct!")
        else:
            print("Incorrect!")
            return False
    elif x == "2":
        if p2.termStart < p1.termStart & p3.termStart:
            print ("Correct!")
        elif p2.termEnd < p1.termEnd & p3.termEnd:
            print ("Correct!")
        else:
            print("Incorrect!")
            return False
    elif x == "3":
        if p3.termStart < p1.termStart & p2.termStart:
            print ("Correct")
        if p3.termEnd < p1.termEnd & p2.termEnd:
            print ("Correct")
        else:
            print("Incorrect")
            return False

def checkResult(question,replay):
    if question == 10:
        print("Congrats! You've comepleted the game!")
        quit()
    else:
        question -= 1
    print ("You reached question ", question)
    print ("Would you like to try again? Yes or No?")
    replay = input()
    return replay




replay = "Yes"

while replay == "Yes":

    lives = 3
    question = 1

    presidentList = [
    ("George Washington", 1789, 1797),("John Adams", 1797, 1801),("Thomas Jefferson", 1801, 1809),
    ("James Madison", 1809, 1817),("James Monroe", 1817, 1825),("John Quincy Adams", 1825, 1829),
    ("Andrew Jackson", 1829, 1837),("Martin Van Buren", 1837, 1841),("William Henry Harrison", 1841, 1841),
    ("John Tyler", 1841, 1845),("James K. Polk", 1845, 1849),("Zachary Taylor", 1849, 1850),
    ("Millard Fillmore", 1850, 1853),("Franklin Pierce", 1853, 1857),("James Buchanan", 1857, 1861),
    ("Abraham Lincoln", 1861, 1863),("Andrew Johnson", 1865, 1869),("Ulysses S. Grant", 1869, 1877),
    ("Rutherford B. Hayes", 1877, 1881),("James Garfield", 1881, 1881),("Chester A. Arthur", 1881, 1885),
    ("Grover Cleaveland (1st Term)", 1885, 1889),("Benjamin Harrison", 1889, 1893),("Grover Cleaveland (2nd Term)", 1893, 1897),
    ("William McKinley", 1897, 1901),("Theodore Roosevelt", 1901, 1909),("William Howard Taft", 1909, 1913),
    ("Woodrow Wilson", 1913, 1921),("Warren G. Harding", 1921, 1923),("Calvin Coolidge", 1923, 1929),
    ("Herbert Hoover", 1929, 1933),("Franklin D. Roosevelt", 1933, 1945),("Harry S. Truman", 1945, 1953),
    ("Dwight D. Eisenhower", 1953, 1961),("John F. Kennedy", 1961, 1963),("Lyndon B. Johnson", 1963, 1969),
    ("Richard M. Nixon", 1969, 1974),("Gerald R. Ford", 1974, 1977),("James Carter", 1977, 1981),
    ("Ronald Reagan", 1981, 1989),("George H. W. Bush", 1989, 1993),("William J. Clinton", 1993, 2001),
    ("George W. Bush", 2001, 2009),("Barack Obama", 2009, 2017),("Donald Trump", 2017, 2021),("Joe Biden", 2021, 2025)
    ]
    
    greeting()
    rules()

    while lives > 0:
        print("Question", question)
        print("Which of these Presidents served first?")
        p1 = choices()
        p2 = choices()
        p3 = choices()
        print(p1.name, p2.name, p3.name)
        answer = input()
        answer = correctAnswer(answer)
        if answer == False:
            lives -= 1
        question += 1
        print("\n 1.", p1.name, "(", p1.termStart, "-", p1.termEnd, ")", "2.", p2.name, "(", p2.termStart, "-", p2.termEnd, ")", "3.", p3.name, "(", p3.termStart, "-", p3.termEnd, ")")
        print("\nLives remaining", lives,)
    replay = checkResult(question,replay)










