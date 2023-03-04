import tkinter as t
import tkinter.messagebox as m
from tkmacosx import Button as b    #have to use this to influence color on a mac with tkinter
from PIL import Image, ImageTk


class RegistrationForm():
    def __init__(self):


        self.main_window = t.Tk()
        self.main_window.geometry('350x425')
        self.main_window.title("Responsive Registration Form")

        self.frame1 = t.Frame(self.main_window)
        self.frame2 = t.Frame(self.main_window)
        self.frame3 = t.Frame(self.main_window)
        self.frame4 = t.Frame(self.main_window)
        self.frame5 = t.Frame(self.main_window)
        self.frame6 = t.Frame(self.main_window)
        self.frame7 = t.Frame(self.main_window)
        self.frame8 = t.Frame(self.main_window)
        self.frame9 = t.Frame(self.main_window)
        self.frame10 = t.Frame(self.main_window)
        self.frame11= t.Frame(self.main_window)
        self.frame12 = t.Frame(self.main_window)
        self.frame13 = t.Frame(self.main_window)
        self.frame14 = t.Frame(self.main_window)


        #-Email - 
        self.dlabel1 = t.Label(self.frame1,text="")
        self.dlabel1.pack(side="left")

        self.email_var = t.StringVar()

        # This an email like image i have downloaded - if you dont want to test my path, then comment out the next 4 lines and uncomment line 43
        mail_image = Image.open('/Users/dbraedencole/Documents/AdvPython/mail.png',mode="r") 
        mail_icon = mail_image.resize((30,30))
        mail_img = ImageTk.PhotoImage(mail_icon)
        self.email_label = t.Label(self.frame2,image=mail_img)
                                   
        # self.email_label = t.Label(self.frame2,text="Email",font=('Open Sans',14))
        self.email_entry = t.Entry(self.frame2,width=24,textvariable=self.email_var) # orig width of 30 w/o image
        self.email_entry.focus()

        # self.email_var.set("Email") # This was used to set the default, but I couldn't get it to work without the useer deleting it

        self.email_label.pack(side="left")
        self.email_entry.pack(side="left")

        
        #-Password-
        self.dlabel2 = t.Label(self.frame3,text="")
        self.dlabel2.pack(side="left")

        self.password_var = t.StringVar()

        # This is a lock image i have downloaded - if you do not want to test my path then comment out the next 4 lines, and line 83
        #  and uncomment lines 66 & 85 
        lock_image = Image.open('/Users/dbraedencole/Documents/AdvPython/lock.png',mode="r") 
        lock_icon = lock_image.resize((30,30))
        lock_img = ImageTk.PhotoImage(lock_icon)

        self.password_label = t.Label(self.frame4,image=lock_img)

        # self.password_label = t.Label(self.frame4,text="Password",font=('Open Sans',14))
        self.password_entry = t.Entry(self.frame4,width=24,textvariable=self.password_var,show="*") # orig width of 27 w/o image 

        # self.password_var.set("Password") # This was used to set the default, but I couldn't get it to work without the useer deleting it

        self.password_label.pack(side="left")
        self.password_entry.pack(side="left")

        
        #-Re-type password-
        self.dlabel3 = t.Label(self.frame5,text="")
        self.dlabel3.pack(side="left")

        self.re_password_var = t.StringVar()

        # Image for the re-type password
        self.re_password_label = t.Label(self.frame6,image=lock_img)

        # self.re_password_label = t.Label(self.frame6,text="Re-type Password",font=('Open Sans',14))
        self.re_password_entry = t.Entry(self.frame6,width=24,textvariable=self.re_password_var,show="*") # orig width of 21 w/o image

        #self.re_password_var.set("Re-type Password") # This was used to set the default, but I couldn't get it to work without the useer deleting it

        self.re_password_label.pack(side="left")
        self.re_password_entry.pack(side="left")


        #-First Name & Last Name-
        self.dlabel4 = t.Label(self.frame7,text="")
        self.dlabel4.pack(side="left")

        self.fn_var = t.StringVar()

        # This is a person image i have downloaded - if you do not want to test my path then comment out the next 4 lines, and line 114
        #  and uncomment lines 107 & 85 
        person_image = Image.open('/Users/dbraedencole/Documents/AdvPython/human.png',mode="r") 
        person_icon = person_image.resize((25,25))
        person_img = ImageTk.PhotoImage(person_icon)
        self.fn_label = t.Label(self.frame8,image=person_img)

        # self.fn_label = t.Label(self.frame8,text="First Name",font=('Open Sans',13))
        self.fn_entry = t.Entry(self.frame8,width=10,textvariable=self.fn_var)

        # self.fn_var.set("First Name")

        self.ln_var = t.StringVar()

        # image Last name entry
        self.ln_label = t.Label(self.frame8,image=person_img)

        # self.ln_label = t.Label(self.frame8,text="Last Name",font=('Open Sans',13))
        self.ln_entry = t.Entry(self.frame8,width=10,textvariable=self.ln_var)

        # self.ln_var.set("Last Name")

        self.fn_label.pack(side="left")
        self.fn_entry.pack(side="left")
        self.ln_label.pack(side="left")
        self.ln_entry.pack(side="left")


        # Male & Female - radio buttins
        self.dlabel5 = t.Label(self.frame9,text="")
        self.dlabel5.pack(side="left")

        self.radio_var = t.IntVar()
        self.rb_male = t.Radiobutton(self.frame10,text="Male",variable=self.radio_var,value=1,font=('Open Sans',14))
        self.rb_female = t.Radiobutton(self.frame10,text="Female",variable=self.radio_var,value=2,font=('Open Sans',14))


        self.rb_male.pack(side="left")
        self.rb_female.pack(side="left")


        # Checkboxes
        self.dlabel6 = t.Label(self.frame11,text="")
        self.dlabel6.pack(side="left")

        self.cb_var1 = t.IntVar()
        self.cb_var2 = t.IntVar()

        self.option1 = t.Checkbutton(self.frame12,text="I agree with the terms and conditions",variable=self.cb_var1,font=('Open Sans',14))
        self.option2 = t.Checkbutton(self.frame12,text="I want to receive the newsletter",variable=self.cb_var2,font=('Open Sans',14))

        self.option1.pack(anchor="w")
        self.option2.pack(anchor="w")


        # Register button
        self.dlabel7 = t.Label(self.frame13,text="")
        self.dlabel7.pack(side="left")

        # self.register_btn = t.Button(self.frame14,text="Register",command=self.validate,width=30,font=('Open Sans',14))

        self.register_btn = b(self.frame14,text="Register",command=self.validate,width=300,font=('Open Sans',14),bg="gold",fg='white')
        self.register_btn.pack(anchor="c")



        # Pack all the frames
        self.frame1.pack(anchor="w")
        self.frame2.pack(anchor="w")
        self.frame3.pack(anchor="w")
        self.frame4.pack(anchor="w")
        self.frame5.pack(anchor="w")
        self.frame6.pack(anchor="w")
        self.frame7.pack(anchor="w")
        self.frame8.pack(anchor="w")
        self.frame9.pack(anchor="w")
        self.frame10.pack(anchor="w")
        self.frame11.pack(anchor="w")
        self.frame12.pack(anchor="w")
        self.frame13.pack(anchor="w")
        self.frame14.pack(anchor="c")

        t.mainloop()


    def validate(self):
        if self.radio_var.get() != 1 and self.radio_var.get() != 2:
            m.showinfo("Missing Gender", "Please select a gender")
            return
        elif self.cb_var1.get() != 1 or self.cb_var2.get() !=1:
            m.showinfo("Missing Consent", "Please select all the checkboxes")
            return
        elif self.password_var.get() != self.re_password_var.get() or self.password_var.get() == "" or self.re_password_var == "":
            m.showinfo("Password Does Not Match", "Please enter matching passwords")
            return
        elif self.email_var.get() == "":
            m.showinfo("Enter Email","Please enter your email address to register")
            return
        elif self.fn_var.get() == "" or self.ln_var.get() =="":
            m.showinfo("Enter Name","Please enter your name to register")
            return
        else:
            valid = True
        
        if valid:
            m.showinfo("Registered", "Thank you. You are registered.")


instance = RegistrationForm()
