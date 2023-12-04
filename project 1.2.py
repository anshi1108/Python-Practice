#!/usr/bin/env python
# coding: utf-8

# In[1]:


def budget_game():
    #welcome user
    print("Welcome to our Aquarium & Aquatic Conservatory!")
    #ask name
    user_name=input('What is your name? ')
    print("*"*30)
    #date time library to make another bot 
    import datetime
    time = datetime.datetime.now()
    hour=int(time.strftime("%H"))

    #greet based on time
    if hour>=9 and hour<18:
        if hour>=9 and hour<12:
            print('Good morning',user_name.title()+",")
        elif hour>=12 and hour<16:
            print('Good Afternoon',user_name.title()+",")
        else:
            print('Good Evening',user_name.title()+",")
        print('I will assist you with your aquatic exploration today!')
        print("*"*30)
        #ask budget
        budget=int(input("What is your budget today? "))
        print("*"*30)
        #>5000
        if budget>=5000:
            print("You can watch the dolphin show!")
        #1000-5000
        if budget>=1000 and budget<5000:
            print("You can visit the shark tanks!")
        #500-1000
        if budget>=500 and budget<1000:
            print("You can visit the stingray and eel tanks!")
        #100-500
        if budget>=100 and budget<500:
            print("You can visit the crab tank!")
        #10-100
        if budget>=50 and budget<100:
            print("You can visit the small fish tanks!")
        #50
        if budget<50:
            print("Sorry, doesnt seem like you can get any ticket with that budget!")
    else:
        print('Sorry',user_name.title(),"\nThe aqaurium is closed right now, visit us during working hours!")
    print('\nThanks for visiting! XD')


# In[2]:


def coin_toss():
    #anounce game
    #welcome user
    print("Hello, welcome to Heads or Tails!")
    print("*"*30)
    choice=input("Choose your side: ")
    print("*"*30)
    if choice.lower()=='heads' or choice.lower()=='tails':
        if choice.lower()=='heads':
            print("You chose Heads!")
            print("I choose Tails!")
        elif choice.lower()=='tails':
            print("You chose Tails!")
            print("I choose Heads!")
        print("*"*30)
        #coin toss
        import random 
        toss=int(random.randint(0,1))
        if toss==1:
            result="heads"
        if toss==0:
            result="tails"
        print("The result is:",result,end='\n\n')
        #if match => user wins
        if choice.lower()==result:
            print("You won!")
        #else computer wins
        else:
            print("You lost! Try again!")
    else:
        print("Invalid choice")


# In[3]:


def cube_game():
    #welcome user
    print("Hello! Welcome to the cube game!")
    print("*"*30)
    #take number
    num=int(input("Enter number: "))
    print("*"*30)
    #print cubes
    for i in range(1,num):
        print(str(num)+"^3 =",num*num*num)
        num=num-1


# In[4]:


def table():
    #welcome user
    print('Welcome to Table Generator')
    print("*"*30)
    #take input
    num=int(input('Enter your number: '))
    print("*"*30)
    #output table
    i=1
    while i<=10:
        print(f'{num} x {i} = {num*i}')
        i=i+1


# In[5]:


def factorial():
    #welcome user
    print('Welcome to Factorial calculator!')
    print("*"*30)
    #take input
    num=int(input("Enter number: "))
    print("*"*30)
    #calc factorial
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    #give output
    print(f"The factorial of {num} is {fact}.")


# In[6]:


def pass_gen():
    import random
    #welcome user
    print('Welcome to password generator!')
    print("*"*30)
    num=int(input('Enter length of password: '))
    #make while loop
    while num<8:
        print("Password too small, try again!\n")
        num=int(input('Enter length of password: '))
    print("*"*30)
    #create loop
    password=''
    for i in range (num):
        #create random number
        rand=random.randint(33,126)
        #convert ascii value
        password+=chr(rand)
    print(f'Password is: {password}')


# In[7]:


def fibonacci():
    # Welcome user
    print("Welcome to the Fibonacci sequence generator!")
    print("*" * 40)  # Asterisks for visual separation
    
    # Take input
    num = int(input("Enter the number of digits in the sequence: "))
    print("*" * 40)  # Asterisks for visual separation
    
    # Calculate Fibonacci sequence
    sequence = [0, 1]  # Initialize sequence
    
    for _ in range(2, num):
        next_num = sequence[-1] + sequence[-2]  # Calculate next number in sequence
        sequence.append(next_num)  # Add the next number to the sequence
    
    # Print the sequence
    print("The Fibonacci sequence with", num, "digits is:")    
    for num in sequence:
        print(num)


# In[8]:


import time
def timer():
    # Welcome message
    print("Welcome to the countdown timer!")
    print("*" * 40)  # Asterisks for visual separation    
    # Ask for minutes and validate input
    m = int(input("Enter minutes (0-59): "))
    while m >= 60 or m < 0:
        print("Invalid input! Minutes should be between 0 and 59.")
        m = int(input("Enter minutes (0-59): "))   
    # Ask for seconds and validate input
    s = int(input("Enter seconds (0-59): "))
    while s >= 60 or s < 0:
        print("Invalid input! Seconds should be between 0 and 59.")
        s = int(input("Enter seconds (0-59): "))   
    # Calculate total seconds
    total_seconds = s + 60 * m    
    # Display timer
    print("\nCountdown started!")
    while total_seconds >= 0:
        # Calculate minutes and seconds
        minutes, seconds = divmod(total_seconds, 60)        
        # Display time in MM:SS format
        print('{:02}:{:02}'.format(minutes, seconds), end='\r')  # Carriage return to overwrite output        
        # Wait for 1 second
        time.sleep(1)        
        # Decrement total seconds
        total_seconds -= 1    
    print("\nTime's up!")


# In[9]:


import random

def dice_game():
    # Welcome message
    print("Hello! Welcome to the Dice Game!")
    print("*" * 40)      
    while True:
        # Ask for user's chosen value
        choice = int(input("Choose a number between 1 and 6: "))
        print("*" * 40)  
        print("You chose:", choice,"")      
        # Validate the chosen value
        if 1 <= choice <= 6:
            # Roll the dice
            result = random.randint(1, 6)
            # Display the result
            print('The result is:', result)
            # Check if the user's choice matches the dice result
            if choice == result:
                print("Congratulations! You won!")
                break
            else:
                print("Sorry, you lost. Try again! :(\n")
                print("*" * 40)  
        else:
            print("Invalid choice! Please choose a number between 1 and 6.\n")
            print("*" * 40)  


# In[10]:


import time
from random import randint

def mind_reader():
    # Welcome message
    print("Welcome to the mind-reading game!")
    print("*" * 40)  # Asterisks for visual separation
    
    # Instructions for the user
    print("Choose a number between 1 and 10,000")
    time.sleep(5)
    print("Now multiply the number by 2")
    guess_num = 0
    
    # Generate 4 random numbers and add them to the guess
    for i in range(4):
        time.sleep(5)
        num = randint(1, 100)
        guess_num += num
        print(f"Now add {num}")
    
    # Display the guessed number
    time.sleep(4)
    print("Now divide the number by 2")
    time.sleep(4)
    print("Now subtract the original number from the answer")
    guess_num /= 2
    print(f"Your answer now is {guess_num}")


# In[11]:


def r_p_s():
    # Welcome message
    print("Hello! Welcome to the rock, paper, scissors game!")
    print("*" * 40)  # Asterisks for visual separation
    
    # Take input
    while True:
        choice = input("Enter choice (R/P/S): ")
        print("*" * 40)
        if choice.upper() in ['R', 'P', 'S']:
            # Find result
            import random
            res = random.choice("RSP")
            
            # Output user choice
            if choice.upper() == 'R':
                print("You chose Rock!")
            elif choice.upper() == 'P':
                print("You chose Paper!")
            else:
                print("You chose Scissors!")
            
            # Output computer choice
            if res.upper() == 'R':
                print("I chose Rock!")
            elif res.upper() == 'P':
                print("I chose Paper!")
            else:
                print("I chose Scissors!")
            
            # Compare choices
            if res == choice.upper():
                print("It's a Tie! Try again!")
                print("*" * 40)
            elif res == 'R':
                if choice.upper() == 'S':
                    print("You lost!")
                    print("*" * 40)
                else:
                    print("You won!")
                    break
            elif res == 'P':
                if choice.upper() == 'R':
                    print("You lost!")
                    print("*" * 40)
                else:
                    print("You won!")
                    break
            elif res == 'S':
                if choice.upper() == 'P':
                    print("You lost!")
                    print("*" * 40)
                else:
                    print("You won!")
                    break
        else:
            print("Invalid option, try again!")


# In[12]:


import random
def hangman():
    print("Welcome to Hangman!")
    print("*" * 40)
    word_bank = ['Apple', 'Mango','Apricot','Guava','Pineapple','Cherry','Banana','Avocado','Kiwi','Orange','Tangerine','Dragon Fruit']
    word = random.choice(word_bank)
    word = word.lower()
    guessed_letters = []
    attempts = 6
    displayed_word = ['_'] * len(word)
    while attempts > 0 and '_' in displayed_word:
        print(" ".join(displayed_word))
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You've already guessed that letter. Try a different one!")
            continue
        guessed_letters.append(guess)
        if guess in word:
            print("Good guess!")
            for i in range(len(word)):
                if word[i] == guess:
                    displayed_word[i] = guess
        else:
            print("Oops! That letter is not in the word.")
            attempts -= 1
        print("Attempts left:", attempts)
        print("*" * 40)
    if '_' not in displayed_word:
        print("Congratulations! You guessed the word:", word.capitalize())
    else:
        print("Oops! You ran out of attempts. The word was:", word.capitalize())


# In[33]:


import tkinter as tk

def create_tooltip(widget, text):
    widget.bind('<Enter>', lambda event, txt=text: show_tooltip(event, txt))
    widget.bind('<Leave>', lambda event: hide_tooltip())

def show_tooltip(event, text):
    x, y, width = event.widget.winfo_x(), event.widget.winfo_y(), event.widget.winfo_width()
    window_width = window.winfo_width()
    if window_width <= 500:
        tooltip_label.place(x=x + 70, y=y - 10)  # Adjust the position for smaller window size
    else:
        tooltip_label.place(x=x + width + 5, y=y - 10)  # Default position for larger window size
    tooltip_label.config(text=text)

def hide_tooltip():
    tooltip_label.place_forget()

# Main window
window = tk.Tk() 
window.title("Python Project") 
window.geometry('500x500') 

# Labels
tk.Label(window,text='Python Projects',font=('Helvetica',18)).place(x=157,y=20) 
tk.Label(window,text='Made by: Anshi Tiwari',font=('Helvetica',12)).place(x=163,y=70) 

# List of buttons with associated functions and tooltips
button_info = [
    ('Countdown Timer', timer, 35, 140, 'A simple timer application!'),
    ('Budget Game', budget_game, 185, 140, 'See what your budget gets you!'),
    ('Coin Toss', coin_toss, 335, 140, 'Play the coin toss game!'),
    ('Cube Game', cube_game, 35, 210, 'Find the cube of any number!'),
    ('Table Generator', table, 185, 210, 'Generate tables of any number!'),
    ('Factorial Calculator', factorial, 335, 210, 'Calculate the factorial of any number!'),
    ('Fibonacci Generator', fibonacci, 35, 280, 'Generate Fibonacci series!'),
    ('Dice Game', dice_game, 185, 280, 'Play a dice game!'),
    ('Password Generator', pass_gen, 335, 280, 'An application to generate passwords!'),
    ('Mind Reader Game', mind_reader, 35, 350, 'Play a mind reader game!'),
    ('Rock, Paper, Scissors', r_p_s, 185, 350, 'Play rock-paper-scissors with AI!'),
    ('Hangman', hangman, 335, 350, 'Play the Hangman game!'),
]

# Buttons with tooltips
for text, command, x, y, tooltip_text in button_info:
    btn = tk.Button(window, text=text, command=command, width=18, height=2)
    btn.place(x=x, y=y)
    create_tooltip(btn, tooltip_text)

tooltip_label = tk.Label(window, text='', relief='solid', wraplength=200)
tooltip_label.config(font=('Helvetica', 10), background='lightyellow')

# Run window
window.mainloop()


# In[ ]:




