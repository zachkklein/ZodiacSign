from tkinter import *
import tkinter as tk

months_list = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

window = Tk()
window.geometry("390x844")
window.title('Zodiac Sign Finder')
window.configure(background='white')

header1 = Label(window, text='Astrological Sign Finder', bg='white', fg='black', font='none 25 bold')
header1.pack()

text1 = Label(window, text='What month were you born?', bg='white', fg='black', font='none 15 bold')
text1.pack()

month = Entry(window, width=50, bg='white', fg='black')
month.pack()

text2 = Label(window, text='What day were you born?', bg='white', fg='black', font='none 15 bold')
text2.pack()

day = Entry(window, width=50, bg='white', fg='black')
day.pack()

def sign():
    def zodiac():
        months_new = month.get().lower()
        num = int(day.get())
        message = 'Your sign is '
        while months_new in months_list:
            if months_new == 'january':
                if num <= 19:
                    return message + 'Capricorn'
                elif num > 31:
                    return 'Error, please try again.'
                else:
                    return message + 'Aquarius'
            elif months_new == 'february':
                if num <= 18:
                    return message + 'Aquarius'
                elif num > 31:
                    return 'Error, please try again.'
                else:
                    return message + 'Pisces'
            elif months_new == 'march':
                if num <= 21:
                    return message + 'Pisces'
                elif num > 31:
                    return 'Error, please try again.'
                else:
                    return message + 'Aries'
            elif months_new == 'april':
                if num <= 20:
                    return message + 'Aries'
                elif num > 31:
                    return 'Error, please try again.'
                else:
                    return message + 'Taurus'
            elif months_new == 'may':
                if num <= 21:
                    return message + 'Taurus'
                elif num > 31:
                    return 'Error, please try again.'
                else:
                    return message + 'Gemini'
            elif months_new == 'june':
                if num <= 20:
                    return message + 'Gemini'
                elif num > 31:
                    return 'Error, please try again.'
                else:
                    return message + 'Cancer'
            elif months_new == 'july':
                if num <= 22:
                    return message + 'Cancer'
                elif num > 31:
                    return 'Error, please try again.'
                else:
                    return message + 'Leo'
            elif months_new == 'august':
                if num <= 22:
                    return message + 'Leo'
                elif num > 31:
                    return 'Error, please try again.'
                else:
                    return message + 'Virgo'
            elif months_new == 'september':
                if num <= 22:
                    return message + 'Virgo'
                elif num > 31:
                    return 'Error, please try again.'
                else:
                    return message + 'Libra'
            elif months_new == 'october':
                if num <= 22:
                    return message + 'Libra'
                elif num > 31:
                    return 'Error, please try again.'
                else:
                    return message + 'Scorpio'
            elif months_new == 'november':
                if num <= 21:
                    return message + 'Scorpio'
                elif num > 31:
                    return 'Error, please try again.'
                else:
                    return message + 'Sagittarius'
            elif months_new == 'december':
                if num <= 21:
                    return message + 'Sagittarius'
                elif num > 31:
                    return 'Error, please try again.'
                else:
                    return message + 'Capricorn'
        else:
            return 'Error, please try again.'
    myLabel = Label(window, text=zodiac(), bg='white', fg='black')
    myLabel.pack()

zodiacButton = Button(window, text='submit', command=sign)
zodiacButton.pack()

break1 = Label(window, text='', bg='white', fg='black', font='none 15 bold')
break1.pack()

header2 = Label(window, text='Chinese Zodiac Finder', bg='white', fg='black', font='none 25 bold')
header2.pack()

year = Entry(window, width=50, bg='white', fg='black')
year.pack()

def lunar():
    def animal():
        year_new = int(year.get())
        message2 = 'Your Chinese Zodiac Sign is '
        if (year_new - 2000) % 12 == 0:
            return message2 + 'Dragon' 
        elif (year_new - 2000) % 12 == 1:
            return message2 + 'Snake'
        elif (year_new - 2000) % 12 == 2:
            return message2 + 'Horse'
        elif (year_new - 2000) % 12 == 3:
            return message2 + 'Sheep'
        elif (year_new - 2000) % 12 == 4:
            return message2 + 'Monkey'
        elif (year_new - 2000) % 12 == 5:
            return message2 + 'Rooster'
        elif (year_new - 2000) % 12 == 6:
            return message2 + 'Dog'
        elif (year_new - 2000) % 12 == 7:
            return message2 + 'Pig'
        elif (year_new - 2000) % 12 == 8:
            return message2 + 'Rat'
        elif (year_new - 2000) % 12 == 9:
            return message2 + 'Ox'
        elif (year_new - 2000) % 12 == 10:
            return message2 + 'Tiger'
        elif (year_new - 2000) % 12 == 11:
            return message2 + 'Rabbit'
        else:
            return 'Error, please try again.'
    animalLabel = Label(window, text=animal(), bg='white', fg='black')
    animalLabel.pack()

animalButton = Button(window, text='submit', command=lunar)
animalButton.pack()

break2 = Label(window, text='', bg='white', fg='black', font='none 15 bold')
break2.pack()

results = Label(window, text='Results:', bg='white', fg='black', font='none 20 bold' )
results.pack()

end = Button(window, text='Close Program', command=window.destroy)
end.pack(side=BOTTOM)

window.mainloop()
