# Currency converter

from tkinter import *
import rates

fontStyle = ("Calibri", 22)


## Setup ##
root = Tk()

root.geometry("850x400")
root.config(bg="black")
root.wm_attributes('-transparentcolor', '#ab23ff')

title = Label(font=("Poppins", 48),
              text="Currency Converter",
              bg="black",
              fg="white")
title.pack()

currencies = ["USD", "GBP", "EUR", "INR"]


option1Text = StringVar()
option2Text = StringVar()
entryText = StringVar()
convertedText = StringVar()

option1Text.set("Select option")
option2Text.set(currencies[0])

excRates = rates.get()

ratesDict = {
    "EUR": excRates[0],
    "GBP": excRates[1],
    "INR": excRates[2]
}

currencySymbols = {
    "USD": "$",
    "GBP": "£",
    "EUR": "€",
    "INR": "₹"
}
############


def displayConverted(convertedVal):
    if "entered" in convertedVal:
        convertedLbl.config(fg="red")
    else:
        convertedLbl.config(fg="white")
    convertedText.set(convertedVal)

    convertedLbl.pack_forget()
    convertedLbl.pack()
    if len(convertedVal) > 15:
        convertedLbl.place(in_=opt1Entry, x=-125, y=100)
    elif len(convertedVal) >= 18:
        convertedLbl.place(in_=opt1Entry, x=-180, y=100)
    elif len(convertedVal) >= 20:
        convertedLbl.place(in_=opt1Entry, x=-225, y=100)
    else:
        convertedLbl.place(in_=opt1Entry, x=-40, y=100)


def opt1Callback(*args):
    if option1Text.get() == option2Text.get():  # The two dropdowns are the same.
        index = currencies.index(option2Text.get())
        # If the option selected is at the end of the list.
        if index+1 > len(currencies)-1:
            option2Text.set(currencies[0])
        else:
            option2Text.set(currencies[index+1])

    currency = StringVar()
    try:
        currency.set(currencySymbols[option1Text.get()])
    except:
        print("Please set the first currency first.")
    currencySign = Label(root, textvariable=currency)
    currencySign.config(font=("Consolas", 36),
                        bg="black",
                        fg="white")
    currencySign.pack()
    currencySign.place(in_=opt1Entry, x=-33, y=-8)

    opt1Entry.pack()
    opt1Entry.place(in_=title, x=175, y=175)

    convert.pack()
    convert.place(in_=opt1Entry, x=180, y=1)


def opt2Callback(*args):
    if option2Text.get() == option1Text.get():  # The two dropdowns are the same.
        index = currencies.index(option1Text.get())
        # If the option selected is at the end of the list.
        if index+1 > len(currencies)-1:
            option1Text.set(currencies[0])
        else:
            option1Text.set(currencies[index+1])

    opt1Callback()


def swap(*args):
    opt1 = option1Text.get()
    opt2 = option2Text.get()

    option1Text.set(opt2)
    option2Text.set(opt1)
    opt1Callback()


def conversion():
    print(excRates)
    currency1 = option1Text.get()
    currency2 = option2Text.get()
    try:
        if currency1 == "USD":
            convertedVal = float(entryText.get()) * \
                float(ratesDict[option2Text.get()])

        else:
            USDVal = float(entryText.get()) / \
                float(ratesDict[option1Text.get()])
            if currency2 != "USD":
                convertedVal = USDVal * float(ratesDict[option2Text.get()])
            else:
                convertedVal = USDVal

        convertedVal = f"= {currencySymbols[option2Text.get()]}{convertedVal:.2f}"
        # The f"{x:.2f}" gives the value to 2dp
        print(convertedVal)
        result = f"{currencySymbols[option1Text.get()]}{opt1Entry.get()} {convertedVal}"
        displayConverted(result)

    except ValueError:
        if entryText.get() == "":
            message = "No value entered."
        else:
            message = "Invalid value entered."
        displayConverted(message)


if option1Text.get() == option2Text.get():  # The two dropdowns are the same.
    index = currencies.index(option2Text.get())
    # If the option selected is at the end of the list.
    if index+1 > len(currencies)-1:
        option2Text.set(currencies[0])
    else:
        option2Text.set(currencies[index+1])

option1 = OptionMenu(root, option1Text, *currencies, command=opt1Callback)
option1.config(bg="white",
               fg="black",
               font=fontStyle,
               width=12)
option2 = OptionMenu(root, option2Text, *
                     currencies, command=opt2Callback,)
option2.config(bg="white",
               fg="black",
               font=fontStyle,
               width=12)

arrow = Label(bg="black",
              fg="white",
              text="→",
              font=("Consolas", 56))
arrow.pack()
arrow.place(in_=option1, x=240, y=-30)
arrow.bind("<Button-1>", lambda x: swap())

option1.pack()
option1.place(in_=title, x=60, y=100)
option2.pack()
option2.place(in_=title, x=375, y=100)


opt1Entry = Entry(root,
                  font=("Calibri", 30),
                  width=7,
                  textvariable=entryText)

convert = Button(root, font=("Calibri", 20), text="CONVERT",
                 command=lambda: conversion())

convertedLbl = Label(root, textvariable=convertedText)
convertedLbl.config(font=("Poppins", 45),
                    fg="white",
                    bg="black")


root.mainloop()
