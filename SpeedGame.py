words = ['Mango','Apple','Graphs','Lamon','BMW','Boy','dharmik','Harsh','Sunny','Web devlopment','CSE','Python devloper'
         ,'data science','data scientist','java','android devloper','machine learning','AI','IOT','IOS programming']

def labelSlider():
    global count,sliderWords
    text='<=WELCOME TO TYPING SPEED GAME=>'
    if(count >= len(text)):
        count=0
        sliderWords=''
    sliderWords += text[count]
    count += 1
    fontLabel.configure(text=sliderWords)
    fontLabel.after(150,labelSlider)

def time():
    global timeleft,score,miss
    if(timeleft > 11):
        pass
    else:
        timeLabelCount.configure(fg='red')
    if(timeleft > 0):
        timeleft -= 1
        timeLabelCount.configure(text=timeleft)
        timeLabelCount.after(1000,time)
    else:
        gamePlayDetailLabel.configure(text= 'Hit = {} | Miss = {} | Total Score = {}'.format(score,miss,score-miss))
        rr=messagebox.askretrycancel('Notification','Play Again ! Press The Retry Button ')
        if(rr==True):
            score = 0
            timeleft=60
            miss = 0
            timeLabelCount.configure(text=timeleft)
            wordLabel.configure(text=words[0])
            scoreLabelCount.configure(text=score)

def startGame(event):
    global score,miss
    if(timeleft==60):
        time()
    else:
        gamePlayDetailLabel.configure(text='')
    if(wordEntry.get() == wordLabel['text']):
        score += 1
        scoreLabelCount.configure(text=score)
    else:
        miss += 1
    random.shuffle(words)
    wordLabel.configure(text=words[0])
    wordEntry.delete(0,END)


from tkinter import *
import random
########################## Root Method #####################
root = Tk()
root.geometry('800x600+400+100')
root.configure(bg='light gray')
root.title('Typing Speed Game')

######################### VAriable Section ################
score=0
timeleft=60
count=0
sliderWords=''
miss = 0


#########################  Label Method ###################
fontLabel = Label(root,text='',font=('elephant',19,'bold')
                  ,bg='light gray',fg='dark blue',justify='center')
fontLabel.place(x=100,y=30)
labelSlider()

random.shuffle(words)


wordLabel= Label(root,text=words[0],font=('elephant',25,'bold'),bg='light gray')
wordLabel.place(x=300,y=230)

scoreLabel= Label(root,text='Your Score :',font=('elephant',25,'bold'),bg='light gray',justify='left',fg='red')
scoreLabel.place(x=10,y=150)

scoreLabelCount= Label(root,text=score,font=('elephant',25,'bold'),bg='light gray',justify='left',fg='red')
scoreLabelCount.place(x=80,y=200)

timerLable=Label(root,text='Time Left :',font=('elephant',25,'bold'),bg='light gray',justify='right',fg='green')
timerLable.place(x=600,y=150)

timeLabelCount= Label(root,text=timeleft,font=('elephant',25,'bold'),bg='light gray',justify='left',fg='green')
timeLabelCount.place(x=660,y=200)

gamePlayDetailLabel=Label(root,text='Type Word & Press Enter Button !',font=('elephant',25,'bold'),
                          bg='light gray',fg='blue')
gamePlayDetailLabel.place(x=120,y=450)



######################### Entry Method ###################
wordEntry= Entry(root,font=('elephant',25,'bold'),bd=10,justify='center')
wordEntry.place(x=180,y=300)
wordEntry.focus_set()

############################################################################
root.bind('<Return>',startGame)




root.mainloop()