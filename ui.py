from cgitb import text
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Separator
from main import *
from utils import *
  
window = Tk()
window.title("Ad Prediction")
window.geometry('1000x600')

data = StringVar()
data.set('Choose dataset...')
lbl = Label(window, text = "Select the dataset from which you want to predict.", font=("Arial Bold", 10))
lbl.grid(column=0, row=0)
drop = OptionMenu(window, data, 'social network ads', 'covid predict')
drop.grid(column=1, row=0)

fram2 = Frame(window)
fram2.grid(column=0, row=1)

frame1 = Frame(window)
frame1.grid(column=1, row=1)



def clear_frame(frame):
  for widgets in frame.winfo_children():
      widgets.destroy()

def show():
  if data.get() == 'social network ads':
    clear_frame(fram2)
    gender = IntVar()
    gender.set(1)

    lbl = Label(frame1, text=" Sex: ")
    lbl.grid(column=1, row=1)
    Radiobutton(frame1, text= "Male", variable=gender, value=1).grid(column=2, row=1)
    Radiobutton(frame1, text= "Female", variable=gender, value=0).grid(column=3, row=1)

    lbl = Label(frame1, text=" Age")
    lbl.grid(column=1, row=2)
    age = Entry(frame1,width=20)
    age.grid(column=2, row=2)
    age.focus()

    lbl = Label(frame1, text=" Salary")
    lbl.grid(column=1, row=3)
    sal = Entry(frame1,width=30)
    sal.grid(column=2, row=3)
    sal.focus()

    def social_submit_clicked():
        new_input = list(map(int, [gender.get(), age.get(), sal.get()]))
        X_train, X_test, y_train, y_test, means, stdevs = social_preprocess()
        for i in range(len(new_input)):
          new_input[i] = (new_input[i] - means[i]) / stdevs[i]
        new_input = np.reshape(new_input, (1, len(new_input)))
        print(new_input, np.shape(X_test), np.shape(new_input))
        classifier = social_get_model(X_train, y_train)
        output = classifier.predict(new_input)
        print(output)

        if (output[0] == 1):
            s = 'You have purchased'
        else:
            s = "You haven't purchased"
          
        messagebox.showinfo('Result', s)

    def social_clear_clicked():
      gender.set(1)
      age.delete(0, END)
      sal.delete(0, END)

    btn = Button(frame1, text="Submit", command=social_submit_clicked)
    btn.grid(column=1, row=5)

    clr = Button(frame1, text="Reset", command=social_clear_clicked)
    clr.grid(column=2, row=5)

  elif data.get() == 'covid predict':
    clear_frame(frame1)
    lbl1 = Label(fram2, text=" Check if you have any of the following symptoms")
    lbl1.grid(column=2, row=2)

    breathing_problem = IntVar()
    breathing_problem.set(0)
    fever = IntVar()
    fever.set(0)
    dry_cough = IntVar()
    dry_cough.set(0)
    sore_throat = IntVar()
    sore_throat.set(0)
    running_nose = IntVar()
    running_nose.set(0)
    headache = IntVar()
    headache.set(0)
    fatigue = IntVar()
    fatigue.set(0)

    check11 = Checkbutton(fram2, text='Breathing Problem', var=breathing_problem)
    check11.grid(column=1,row=3)
    check12 = Checkbutton(fram2, text='Fever', var=fever)
    check12.grid(column=2,row=3)
    check13 = Checkbutton(fram2, text='Dry Cough', var=dry_cough)
    check13.grid(column=1,row=4)
    check14 = Checkbutton(fram2, text='Running Nose', var=running_nose)
    check14.grid(column=2,row=4)
    check15 = Checkbutton(fram2, text='Headache', var=headache)
    check15.grid(column=1,row=5)
    check16 = Checkbutton(fram2, text='Fatigue', var=fatigue)
    check16.grid(column=2,row=5)

    separator = Separator(fram2, orient='horizontal')
    separator.grid(row=6)

    lbl2 = Label(fram2, text=" Check if you have following health condition")
    lbl2.grid(column=2, row=7)

    asthma = IntVar()
    asthma.set(0)
    chronic_lung = IntVar()
    chronic_lung.set(0)
    heart_disease = IntVar()
    heart_disease.set(0)
    diabetes = IntVar()
    diabetes.set(0)
    hyper_tension = IntVar()
    hyper_tension.set(0)
    gastro = IntVar()
    gastro.set(0)

    check11 = Checkbutton(fram2, text='Asthma', var=asthma)
    check11.grid(column=1,row=8)
    check12 = Checkbutton(fram2, text='Chronic Lung Disease', var=chronic_lung)
    check12.grid(column=2,row=8)
    check13 = Checkbutton(fram2, text='Heart Disease', var=heart_disease)
    check13.grid(column=1,row=9)
    check14 = Checkbutton(fram2, text='Diabetes', var=diabetes)
    check14.grid(column=2,row=9)
    check15 = Checkbutton(fram2, text='Hyper Tension', var=hyper_tension)
    check15.grid(column=1,row=10)
    check16 = Checkbutton(fram2, text='Gastrointestinal', var=gastro)
    check16.grid(column=2,row=10)\

    separator = Separator(fram2, orient='horizontal')
    separator.grid(row=11)

    lbl3 = Label(fram2, text=" Check if you have performed following activities lately")
    lbl3.grid(column=2, row=12)

    abroad = IntVar()
    abroad.set(0)
    contact = IntVar()
    contact.set(0)
    attend = IntVar()
    attend.set(0)
    visit = IntVar()
    visit.set(0)

    check11 = Checkbutton(fram2, text='Travelled Abroad', var=abroad)
    check11.grid(column=2,row=13)
    check12 = Checkbutton(fram2, text='Came in contact with COVID Patient', var=contact)
    check12.grid(column=2,row=14)
    check13 = Checkbutton(fram2, text='Attended Large Gathering', var=attend)
    check13.grid(column=2,row=15)
    check14 = Checkbutton(fram2, text='Visited Pulblic Exposed Place', var=visit)
    check14.grid(column=2,row=16)

    separator = Separator(fram2, orient='horizontal')
    separator.grid(row=17)

    family = IntVar()
    family.set(0)
    lbl = Label(fram2, text=" Do any of your family member work in public exzposed place: ")
    lbl.grid(column=2, row=18)
    Radiobutton(fram2, text= "Yes", variable=family, value=1).grid(column=1, row=19)
    Radiobutton(fram2, text= "No", variable=family, value=0).grid(column=2, row=19)

    def covid_submit_clicked():
        new_input = list(map(int, [breathing_problem.get(), fever.get(), dry_cough.get(), sore_throat.get(), running_nose.get(), asthma.get(), chronic_lung.get(), headache.get(), heart_disease.get(), diabetes.get(), hyper_tension.get(), fatigue.get(), gastro.get(), abroad.get(), contact.get(), attend.get(), visit.get(), family.get()]))
        X_train, X_test, y_train, y_test = covid_preprocess()
        new_input = np.reshape(new_input, (1, len(new_input)))
        print(new_input, np.shape(X_test), np.shape(new_input))
        classifier = covid_get_model(X_train, y_train)
        output = classifier.predict(new_input)
        print(output)

        if (output[0] == 1):
            s = 'You are COVID-19 positive'
        else:
            s = 'You are COVID-19 negative'
          
        messagebox.showinfo('Result', s)

    btn = Button(fram2, text="Submit", command=covid_submit_clicked)
    btn.grid(column=2, row=21)

  else:
    messagebox.showinfo('Warning', 'Select any one data')

btn = Button(window, text='Continue', command=show)
btn.grid(column=2, row=0)

window.mainloop()
