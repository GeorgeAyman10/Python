#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='https://www.udemy.com/user/joseportilla/'><img src='../Pierian_Data_Logo.png'/></a>
# ___
# <center><em>Content Copyright by Pierian Data</em></center>

# # Milestone Project 1: Walkthrough Steps Workbook
# 
# Below is a set of steps for you to follow to try to create the Tic Tac Toe Milestone Project game!

# #### Some suggested tools before you get started:
# To take input from a user:
# 
#     player1 = input("Please pick a marker 'X' or 'O'")
#     
# Note that input() takes in a string. If you need an integer value, use
# 
#     position = int(input('Please enter a number'))
#     
# <br>To clear the screen between moves:
# 
#     from IPython.display import clear_output
#     clear_output()
#     
# Note that clear_output() will only work in jupyter. To clear the screen in other IDEs, consider:
# 
#     print('\n'*100)
#     
# This scrolls the previous board up out of view. Now on to the program!

# **Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.**

# In[1]:


from IPython.display import clear_output

def display_board(board):
    print (board[6],'   |  ',board[7],'  |  ',board[8])
    print ('----','|','-----','|','----')
    print (board[3],'   |  ',board[4],'  |  ',board[5])
    print ('----','|','-----','|','----')
    print (board[0],'   |  ',board[1],'  |  ',board[2])
    

def display_board_pos():
    print ('6','   |  ','7','  |  ','8')
    print ('----','|','-----','|','----')
    print ('3','   |  ','4','  |  ','5')
    print ('----','|','-----','|','----')
    print ('0','   |  ','1','  |  ','2')


# **TEST Step 1:** run your function on a test version of the board list, and make adjustments as necessary

# In[2]:


#test_board = ['#','X','O','X','O','X','O','X','O','X']
#display_board(test_board)
#display_board_pos()


# **Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using *while* loops to continually ask until you get a correct answer.**

# In[3]:


def player_input():
    XOChoice = False
    XOset = ['X','O']
    global XOPlayer
    global marker
    while XOChoice == False:
        XO=input("Please Player ONE Choose X or O: ")
        
        if XO in XOset:
            XOChoice = True
            marker = XO
            print("Player ONE Chose {} as his choise".format(XO))
            if XO =='X':
                print("Player TWO Will Be O")
                XOPlayer = [1,2]
            else:
                print("Player TWO Will Be X")
                XOPlayer = [2,1]
        else:
            XOChoice = False
            print("Please insert Correct Value X or O only !! {} this is incorrect value".format(XO))


# **TEST Step 2:** run the function to make sure it returns the desired output

# In[4]:


#player_input()


# **Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.**

# In[5]:


def place_marker(board, marker, position):
    board[int(position)]= marker


# **TEST Step 3:** run the place marker function using test parameters and display the modified board

# In[6]:


#place_marker(test_board,'$',8)
#display_board(test_board)


# **Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won. **

# In[7]:


def win_check(board, mark):
    if (board[0] == mark and board[1] == mark and board[2]== mark) or (board[3] == mark and board[4] == mark and board[5]== mark)  or (board[6] == mark and board[7] == mark and board[8]== mark)  or (board[6] == mark and board[3] == mark and board[0]== mark)  or (board[7] == mark and board[4] == mark and board[1]== mark)  or (board[8] == mark and board[5] == mark and board[2]== mark)  or (board[6] == mark and board[4] == mark and board[2]== mark)  or (board[8] == mark and board[4] == mark and board[0]) :
        print ("Winner !")
        return True
    else:
        return False
    


# **TEST Step 4:** run the win_check function against our test_board - it should return True

# In[8]:


#win_check(test_board,'X')


# **Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.**

# In[9]:


import random

def choose_first():
    global marker
    if random.randint(0,1) == 0:
        print("Player X Starts !")
        marker = 'X'
        return 'X'
    else:
        print("Player O Starts !")
        marker = 'O'
        return 'O'


# **Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.**

# In[10]:


def space_check(board, position):
    return board[int(position)] == ' '


# **Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.**

# In[11]:


def full_board_check(board):
    board_size = 0
    for i in range (0,9) :
        if board[i] == 'X' or board[i] == 'O':
            board_size+=1
    
    return board_size == 9


# **Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.**

# In[12]:


def player_choice(board):
    POSChoice = False
    global INTPOS 
    while POSChoice == False :
        POS=input("Please enter a value from 0-8 to indicate your play position: ")
        if POS.isdigit() and int(POS) in range(0,9):
            INTPOS=int(POS)
            POSChoice = True           
        else:
            pass
    return INTPOS


# **Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.**

# In[13]:


def replay():
    XOreplay = False
    XOreplaySet = ['Y','N']
    global XOPlay
    global NOofPLAYES
    global board
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    while XOreplay == False:
        XOPlay=input("Do You Want To Play Again??  Y or N: ")
        NOofPLAYES = 0
        if XOPlay in XOreplaySet:
            XOreplay = True
        else:
            XOreplay = False
            print("Please insert Correct Value Y or N only !! {} this is incorrect value".format(XOPlay))
    return XOPlay == 'Y'
        


# In[14]:


#pass


# **Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!**

# In[15]:


print('Welcome to Tic Tac Toe!')
print("Let's Start The Game !!! EA Sports To The GAMEEEEEEE !!!")
XOPlay = 'Y'
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
NOofPLAYES = 0
oldmarker = ''

while XOPlay == 'Y' or NOofPLAYES <=9:
    
    ## For The First Time Only Show The Empty Board And Choose Which Player Starts With Either X or O
    if NOofPLAYES == 0 :
        display_board_pos()
        player_input()
        choose_first()
     
    ## Take Value From 0-8
    player_choice(board)
    
    ## While 0-8 already taken please insert in empty position
    while space_check(board, INTPOS) == False:
            print("This Position Already Contain {} , Please Choose Another Position ".format(board[INTPOS]))
            player_choice(board)
    
    ## Toggle between X and O
    if oldmarker == 'X':
        marker = 'O'
    elif oldmarker == 'O':
        marker ='X'
    else:
        oldmarker = ''
        
    ## add the chosen value in the board and add number of plays +1
    place_marker(board, marker, INTPOS)
    NOofPLAYES+=1
        
    ## check if any player wins !!
    if win_check(board, marker):
        if marker == 'X':
            print("Player {} Wins !!".format(XOPlayer[0]))
        else:
            print("Player {} Wins !!".format(XOPlayer[1]))
        display_board(board)
        if replay() == False:
            break
       
    oldmarker = marker
    
    ## check if the game is draw!!
    if full_board_check(board):
        print("The Game is Draw !!")
        display_board(board)
        if replay() == False:
            break
        
    if NOofPLAYES != 0 :    
        display_board(board)


# ## Good Job!
