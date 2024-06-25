from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import pyttsx3 as p
from register import Register


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    engine=p.init()
    rate=engine.getProperty('rate')
    engine.setProperty('rate',180)
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    print(voices)
    engine.say("Welcome To the Login Page")
    engine.runAndWait()
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry('1950x1050+0+0')
        self.bg=ImageTk.PhotoImage(file="D:\pic1/pic20.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relheight=1,relwidth=1)

        #===========================frame=========================
        frame=Frame(self.root,bg='blue')
        frame.place(x=710,y=210,height=520,width=370)
        #======================================firstpic===============================
        img1=Image.open("D:\pic/lo1.jpg")
        img1=img1.resize((90,90),Image.Resampling.LANCZOS)
        self.photo1=ImageTk.PhotoImage(img1)
        self.img1=Label(image=self.photo1)
        self.img1.place(x=830,y=210,width=90,height=90)
        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="gray")
        get_str.place(x=95,y=100)

        #label and entry
        username_lbl=Label(frame,text="User Name",font=("times new roman",20,"bold"),fg='white',bg="black")
        username_lbl.place(x=60,y=175)
        self.txtuser=ttk.Entry(frame,font=("times new roman",20,"bold"))
        self.txtuser.place(x=40,y=210,width=270)


        password=Label(frame,text="Password",font=("times new roman",20,"bold"),fg='white',bg="black")
        password.place(x=60,y=255)
        self.txtpass=ttk.Entry(frame,font=("times new roman",20,"bold"))
        self.txtpass.place(x=40,y=290,width=270)


        #=================icon imgs==============================================================
        img2=Image.open("D:\pic/user.jpg")
        img2=img2.resize((40,40),Image.Resampling.LANCZOS)
        self.photo2=ImageTk.PhotoImage(img2)
        self.img2=Label(frame,image=self.photo2)
        self.img2.place(x=0,y=210,width=40,height=37)




        img3=Image.open("D:\pic/pass.jpg")
        img3=img3.resize((40,40),Image.Resampling.LANCZOS)
        self.photo3=ImageTk.PhotoImage(img3)
        self.img3=Label(frame,image=self.photo3)
        self.img3.place(x=0,y=290,width=40,height=37)
        


        #====================Button login============================
        loginbtn=Button(frame,text="Login",command=self.login,font=("time new roman",20,"bold"),bd=3,bg='red',fg='white',activebackground="Green",activeforeground="white")

        loginbtn.place(x=110,y=340,width=120,height=40)


        #=================================       register button       ===================================

        registerbtn=Button(frame,text="New user register",command=self.Regis,font=("time new roman",12,"bold"),bg='black',fg='white',activebackground="black",activeforeground="white")

        registerbtn.place(x=20,y=420,width=150)
    

        #=================new def login ========================
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields are Required")
        elif self.txtuser.get()=="kapu" and  self.txtpass.get()=="ashu":
            messagebox.showinfo("Success","Welcome to Login Page")
        else:
            conn=mysql.connector.connect(host='localhost',user='root',password='awan1234',database='management')
            my_cursor=conn.cursor()
            self=self.app
            my_cursor.execute("select * from register where email=%s and password=%s",(self.var_email.get(),self.var_pass.get()))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("INavalid","Inavlid User name and password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=self.root
                    self.new_window=Toplevel(self.new_window)
                    self.app=Criminal(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    


            #=======================new class===============================================
    def  Regis(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

        #===========================Criminal class=========================================================

class Criminal:
    def __init__(self,root):
        
        self.root=root
        self.root.geometry('1950x1050+0+0')
        self.root.title('Criminal Management System')
        #variable
        self.var_case_id=StringVar()
        self.var_criminal_no=StringVar()
        self.var_name=StringVar()
        self.var_nickname=StringVar()
        self.var_arrest_date=StringVar()
        self.var_date_of_crime=StringVar()
        self.var_address=StringVar()
        self.var_age=StringVar()
        self.var_occupation=StringVar()
        self.var_birthMark=StringVar()
        self.var_crime_type=StringVar()
        self.var_father_name=StringVar()
        self.var_gender=StringVar()
        self.var_wanted=StringVar()



        lbl_title=Label(self.root,text="Criminal Management  System Software ",font=('Yu Gothic UI',60,'bold'),bg='black',fg='gold')
        lbl_title.place(x=0,y=0,width=1990,height=90)



        img_logo=Image.open("C:\pic/lo.png")
        img_logo=img_logo.resize((85,85),Image.Resampling.LANCZOS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)
        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=160,y=3,width=85,height=85)


#img_frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        img_frame.place(x=0,y=85,width=1950,height=190)

        img1=Image.open('C:\pic/pic3.jpg')
        img1=img1.resize((370,180),Image.Resampling.LANCZOS)
        self.photo1=ImageTk.PhotoImage(img1)
        self.img1=Label(img_frame,image=self.photo1)
        self.img1.place(x=0,y=0,width=370,height=180)



        img2=Image.open('C:\pic/pic5.jpg')
        img2=img2.resize((370,180),Image.Resampling.LANCZOS)
        self.photo2=ImageTk.PhotoImage(img2)
        self.img2=Label(img_frame,image=self.photo2)
        self.img2.place(x=380,y=0,width=370,height=180)



        img3=Image.open('C:\pic/pic4.jpg')
        img3=img3.resize((370,180),Image.Resampling.LANCZOS)
        self.photo3=ImageTk.PhotoImage(img3)
        self.img3=Label(img_frame,image=self.photo3)
        self.img3.place(x=760,y=0,width=370,height=180)



        
        img4=Image.open('C:\pic/pic1.jpg')
        img4=img4.resize((370,180),Image.Resampling.LANCZOS)
        self.photo4=ImageTk.PhotoImage(img4)
        self.img4=Label(img_frame,image=self.photo4)
        self.img4.place(x=1140,y=0,width=370,height=180)



        
        img5=Image.open('C:\pic/pic2.jpg')
        img5=img5.resize((370,180),Image.Resampling.LANCZOS)
        self.photo5=ImageTk.PhotoImage(img5)
        self.img5=Label(img_frame,image=self.photo5)
        self.img5.place(x=1520,y=0,width=370,height=180)



        #main frame
        

        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=10,y=278,width=1900,height=700)

#upper frame
        
        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Criminal Information ',font=("time new roman",12,'bold'),fg='red',bg='white')
        upper_frame.place(x=10,y=2,width=1875,height=380)

        #label Entry
        #case Id
        caseid=Label(upper_frame,text='Case ID',font=('time new roman',15,'bold'),bg='white')
        caseid.grid(row=0,column=0, padx=2,sticky=W)
        #Entry
        caseentry=ttk.Entry(upper_frame,textvariable=self.var_case_id,width=22,font=("arial",12,'bold'))
        caseentry.grid(row=0,column=1,padx=2,sticky=W)


                #case no
        lbl_Criminal_no=Label(upper_frame,text='Case no',font=('time new roman',15,'bold'),bg='white')
        lbl_Criminal_no.grid(row=0,column=2, padx=2,pady=7,sticky=W)
        #Entry
        lbl_Criminal_no=ttk.Entry(upper_frame,textvariable=self.var_criminal_no,width=22,font=("arial",12,'bold'))
        lbl_Criminal_no.grid(row=0,column=3,padx=2,pady=7,sticky=W)



                        #case name
        lbl_Criminal_name=Label(upper_frame,text='Name',font=('time new roman',15,'bold'),bg='white')
        lbl_Criminal_name.grid(row=1,column=0, padx=2,pady=7,sticky=W)
        #Entry
        lbl_Criminal_name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=("arial",12,'bold'))
        lbl_Criminal_name.grid(row=1,column=1,padx=2,pady=7,sticky=W)



                        #nickname
        lbl_Criminal_nickname=Label(upper_frame,text='Nick Nmae',font=('time new roman',15,'bold'),bg='white')
        lbl_Criminal_nickname.grid(row=1,column=2, padx=2,pady=7,sticky=W)
        #Entry
        lbl_Criminal_nickname=ttk.Entry(upper_frame,textvariable=self.var_nickname,width=22,font=("arial",12,'bold'))
        lbl_Criminal_nickname.grid(row=1,column=3,padx=2,pady=7,sticky=W)




                        #Arrest Darte
        arrest=Label(upper_frame,text='Date of Arrest',font=('time new roman',15,'bold'),bg='white')
        arrest.grid(row=2,column=0, padx=2,pady=7,sticky=W)
        #Entry
        lbl_arrest=ttk.Entry(upper_frame,textvariable=self.var_arrest_date,width=22,font=("arial",12,'bold'))
        lbl_arrest.grid(row=2,column=1,padx=2,pady=7,sticky=W)




                        #Date of Crime
        lbl_Crime_date=Label(upper_frame,text='Date of Crime',font=('time new roman',15,'bold'),bg='white')
        lbl_Crime_date.grid(row=2,column=2, padx=2,pady=7,sticky=W)
        #Entry
        lbl_Crime_date=ttk.Entry(upper_frame,textvariable=self.var_date_of_crime,width=22,font=("arial",12,'bold'))
        lbl_Crime_date.grid(row=2,column=3,padx=2,pady=7,sticky=W)




                        #Address
        lbl_address=Label(upper_frame,text='Criminal Address',font=('time new roman',15,'bold'),bg='white')
        lbl_address.grid(row=3,column=0, padx=2,pady=7,sticky=W)
        #Entry
        lbl_Address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=("arial",12,'bold'))
        lbl_Address.grid(row=3,column=1,padx=2,pady=7,sticky=W)




                        #age
        lbl_age=Label(upper_frame,text='Age',font=('time new roman',15,'bold'),bg='white')
        lbl_age.grid(row=3,column=2, padx=2,pady=7,sticky=W)
        #Entry
        lbl_age=ttk.Entry(upper_frame,textvariable=self.var_age,width=22,font=("arial",12,'bold'))
        lbl_age.grid(row=3,column=3,padx=2,pady=7,sticky=W)





                        #occupation
        lbl_occupation=Label(upper_frame,text='Occupation',font=('time new roman',15,'bold'),bg='white')
        lbl_occupation.grid(row=4,column=0, padx=2,pady=7,sticky=W)
        #Entry
        lbl_occupation=ttk.Entry(upper_frame,textvariable=self.var_occupation,width=22,font=("arial",12,'bold'))
        lbl_occupation.grid(row=4,column=1,padx=2,pady=7,sticky=W)





                       #birthMark
        lbl_birthMark=Label(upper_frame,text='Date of Birth',font=('time new roman',15,'bold'),bg='white')
        lbl_birthMark.grid(row=4,column=2, padx=2,pady=7,sticky=W)
        #Entry
        lbl_birthMark=ttk.Entry(upper_frame,textvariable=self.var_birthMark,width=22,font=("arial",12,'bold'))
        lbl_birthMark.grid(row=4,column=3,padx=2,pady=7,sticky=W)




                       #crime type
        lbl_crimetype=Label(upper_frame,text='Crime Type',font=('time new roman',15,'bold'),bg='white')
        lbl_crimetype.grid(row=0,column=4, padx=2,pady=7,sticky=W)
        #Entry
        lbl_crimetype=ttk.Entry(upper_frame,textvariable=self.var_crime_type,width=22,font=("arial",12,'bold'))
        lbl_crimetype.grid(row=0,column=5,padx=2,pady=7,sticky=W)




                        #fatrher name
        lbl_fatrhername=Label(upper_frame,text='Fatrher Name',font=('time new roman',15,'bold'),bg='white')
        lbl_fatrhername.grid(row=1,column=4, padx=2,pady=7,sticky=W)
        #Entry
        lbl_fatrhername=ttk.Entry(upper_frame,textvariable=self.var_father_name,width=22,font=("arial",12,'bold'))
        lbl_fatrhername.grid(row=1,column=5,padx=2,pady=7,sticky=W)





        #gender
        lbl_criminal_gen=Label(upper_frame,text='GENDER:',font=("times new roman",15,'bold'),bg='white')
        lbl_criminal_gen.grid(row=2,column=4,sticky=W,padx=2,pady=7)

#wanted
        lbl_criminal_wanted=Label(upper_frame,text='Most Wanted:',font=("times new roman",15,'bold'),bg='white')
        lbl_criminal_wanted.grid(row=3,column=4,sticky=W,padx=2,pady=12)

#Radio button gender
        radio_frame_gender=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_gender.place(x=870,y=94,width=210,height=35)
        male=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Male',value='male',font=("arial",9,'bold'),bg='white')
        male.grid(row=0,column=0,padx=5,pady=2,sticky=W)
        female=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Female',value='female',font=("arial",9,'bold'),bg='white')
        female.grid(row=0,column=1,padx=5,pady=2,sticky=W)

        #Radio button wanted
        radio_frame_wanted=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_wanted.place(x=870,y=140,width=210,height=35)
        yes=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='Yes',value='yes',font=("arial",9,'bold'),bg='white')
        yes.grid(row=0,column=0,padx=5,pady=2,sticky=W)
        no=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='NO',value='no',font=("algerian",9,'bold'),bg='white',fg="black")
        no.grid(row=0,column=1,padx=5,pady=2,sticky=W)



        #button
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=10,y=250,width=885,height=80)
#add button
        btn_add=Button(button_frame,command=self.add_data,text='Record Save',font=("arial",14,'bold'),width=17,height=2,bg='black',fg='white')
        btn_add.grid(row=0,column=0,padx=3,pady=5)
        #update
        btn_update=Button(button_frame,command=self.update_date,text='update',font=("arial",14,'bold'),width=17,height=2,bg="blue",fg='white')
        btn_update.grid(row=0,column=1,padx=3,pady=5)
        #delete
        btn_delete=Button(button_frame,command=self.delete_data,text='Delete',font=("arial",14,'bold'),width=17,height=2,bg='Black',fg='white')
        btn_delete.grid(row=0,column=2,padx=3,pady=5)
        #clear   
        btn_clear=Button(button_frame,command=self.clear_data,text='Clear',font=("arial",14,'bold'),width=17,height=2,bg='Blue',fg='white')
        btn_clear.grid(row=0,column=3,padx=3,pady=5)



        #right side img in upper frame 
        img7=Image.open("C:\pic/pic6.jpg")
        img7=img7.resize((500,320),Image.Resampling.LANCZOS)
        self.photo7=ImageTk.PhotoImage(img7)
        self.img7=Label(upper_frame,image=self.photo7)
        self.img7.place(x=1200,y=0,width=500,height=320)







         #Down Frame
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text="CRIMINAL Information Tabel",font=("times new roman",12,'bold'),fg='red',bg='white')
        down_frame.place(x=10,y=390,width=1875,height=280)#down ki palce


        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text="SearchCRIMINALRecord",font=("times new roman",11,'bold'),fg='red',bg='white')
        search_frame.place(x=2,y=0,width=1860,height=67)#down  under search name ki ak or frame ki place bani ha  ki

        search_by=Label(search_frame,text='Search By:',font=("arial",11,'bold'),bg='red',fg='white')
        search_by.grid(row=0,column=0,sticky=W,padx=5)

#combobox
        self.var_com_search=StringVar()
        self.var_search=StringVar()
        combo_search_box=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=("arial",11,'bold'),width=18,state='readonly')
        combo_search_box['values']=('Select Option','Case_id','Criminal_no')
        combo_search_box.current(0)
        combo_search_box.grid(row=0,column=1,sticky=W,padx=5)
        
#search entry
        search_txt=ttk.Entry(search_frame,textvariable=self.var_search,width=18,font=("arial",12,'bold'))
        search_txt.grid(row=0,column=2,sticky=W,padx=5)

#search button
        btn_search=Button(search_frame,command=self.serch_data,text='Search',font=("arial",12,'bold'),width=12,bg='Blue',fg='white')
        btn_search.grid(row=0,column=3,padx=5)
#search all
        btn_all=Button(search_frame,command=self.fetch_data,text='Show All',font=("arial",12,'bold'),width=12,bg='blue',fg='white')
        btn_all.grid(row=0,column=4,padx=5)



#crime agency ka ma sa  label
        crimeagency=Label(search_frame,font=("arial",35,'bold'),text="National Crime AGENCY",bg='white',fg='crimson')
        crimeagency.grid(row=0,column=50,sticky=W,padx=300,pady=0)

#table frame
        table_frame=Frame(down_frame,bd=2,relief=RIDGE)
        table_frame.place(x=2,y=70,width=1860,height=170)
#scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.criminal_table=ttk.Treeview(table_frame,column=("1","2","3","4","5","6","7","8","9",'10','11','12','13','14'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)
        self.criminal_table.heading('1',text="Case_Id")
        self.criminal_table.heading('2',text="Crime_no")
        self.criminal_table.heading('3',text="Criminal_name")
        self.criminal_table.heading('4',text="Nickname")
        self.criminal_table.heading('5',text="Arrest Date")
        self.criminal_table.heading('6',text="Crime date")
        self.criminal_table.heading('7',text="Address")
        self.criminal_table.heading('8',text="Age")
        self.criminal_table.heading('9',text="Occupation")
        self.criminal_table.heading('10',text="Birth Mark")
        self.criminal_table.heading('11',text="Crime Type")
        self.criminal_table.heading('12',text="Father Name")
        self.criminal_table.heading('13',text="Gender")
        self.criminal_table.heading('14',text="Wanted")
        self.criminal_table['show']='headings'
        self.criminal_table.column("1",width=140)
        self.criminal_table.column("2",width=140)
        self.criminal_table.column("3",width=140)
        self.criminal_table.column("4",width=140)
        self.criminal_table.column("5",width=140)
        self.criminal_table.column("6",width=140)
        self.criminal_table.column("7",width=140)
        self.criminal_table.column("8",width=140)
        self.criminal_table.column("9",width=140)
        self.criminal_table.column("10",width=140)
        self.criminal_table.column("11",width=140)
        self.criminal_table.column("12",width=140)
        self.criminal_table.column("13",width=140)
        self.criminal_table.column("14",width=140)
        self.criminal_table.pack(fill=BOTH,expand=1)



        self.criminal_table.bind("<ButtonRelease>",self.get_cursor)



        self.fetch_data()



    #add function
    
    def add_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',user='root',password='awan1234',database='management')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into crminal1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                                            self.var_case_id.get(),
                                                                                                            self.var_criminal_no.get(),
                                                                                                            self.var_name.get(),
                                                                                                            self.var_nickname.get(),
                                                                                                            self.var_arrest_date.get(),
                                                                                                            self.var_date_of_crime.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_age.get(),
                                                                                                            self.var_occupation.get(),
                                                                                                            self.var_birthMark.get(),
                                                                                                            self.var_crime_type.get(),
                                                                                                            self.var_father_name.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_wanted.get()
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success','Criminal record has been Added')
            except Exception as es:
                messagebox.showerror('Error',f'Due to{str(es)}')
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',user='root',password='awan1234',database='management')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from Crminal1')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert('',END,values=i)
            conn.commit()
        conn.close()


    def get_cursor(self,event=""):
        cursur_row=self.criminal_table.focus()
        content=self.criminal_table.item(cursur_row)
        data=content['values']
        self.var_case_id.set(data[0])
        self.var_criminal_no.set(data[1])
        self.var_name.set(data[2])
        self.var_nickname.set(data[3])
        self.var_arrest_date.set(data[4])
        self.var_date_of_crime.set(data[5])
        self.var_address.set(data[6])
        self.var_age.set(data[7])
        self.var_occupation.set(data[8])
        self.var_birthMark.set(data[9])
        self.var_crime_type.set(data[10])
        self.var_father_name.set(data[11])
        self.var_gender.set(data[12])
        self.var_wanted.set(data[13])
    #update function
    def update_date(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                update=messagebox.askyesno('update',"Are you sure update this crimminal ")
                if update>0:
                    conn=mysql.connector.connect(host='localhost',user='root',password='awan1234',database='management')
                    my_cursor=conn.cursor()
                    my_cursor.execute('Update Crminal1 set Criminal_no=%s,Criminal_name=%s,Nick_name=%s,arrest_date=%s,dateofcrime=%s,address=%s,age=%s,occupation=%s,BirthMark=%s,crimeType=%s,fatherName=%s,gender=%s,wanted=%s where iCase_id=%s',(self.var_criminal_no.get(),self.var_name.get(),self.var_nickname.get(),self.var_arrest_date.get(),self.var_date_of_crime.get(),self.var_address.get(),self.var_age.get(),self.var_occupation.get(),self.var_birthMark.get(),self.var_crime_type.get(),self.var_father_name.get(),self.var_gender.get(),self.var_wanted.get(),self.var_case_id.get(),))
        
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showerror('Success','Criminal record has been successfuly Update ')
            except Exception as es:
                messagebox.showerror('Error',f'Due to{str(es)}')
   #delete id
    def delete_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error',' All Fields or Required ')
        else:
            try:
                Delete=messagebox.askyesno('Delete',"Are you sure Delete this crimminal ")
                if Delete>0:
                        conn=mysql.connector.connect(host='localhost',user='root',password='awan1234',database='management')
                        my_cursor=conn.cursor()
                        sql='delete from crminal1 where iCase_id=%s'
                        value=(self.var_case_id.get(),)
                        my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showerror('DElete success','Criminal record has been successfuly DELETE ')
            except Exception as es:
                messagebox.showerror('Error',f'Due to{str(es)}')
#clear
    def clear_data(self):
        self.var_case_id.set("")
        self.var_criminal_no.set("")
        self.var_name.set("")
        self.var_nickname.set("")
        self.var_arrest_date.set("")
        self.var_date_of_crime.set("")
        self.var_address.set("")
        self.var_age.set("")
        self.var_occupation.set("")
        self.var_birthMark.set("")
        self.var_crime_type.set("")
        self.var_father_name.set("")
        self.var_gender.set("")
        self.var_wanted.set("")


        #define search button
    def serch_data(self):
        if self.var_com_search.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',user='root',password='awan1234',database='management')
                my_cursor=conn.cursor()
                my_cursor('select * from crminal1 where iCase_id=%s' +str(self.var_com_search.get()) +" LIKE' %" +str(self.var_search.get() +" %'"))
                rows=my_cursor.fetchall()
                if len(rows) !=0:
                        self.criminal_table.delete(*self.criminal_table.get_children())
                        for i in rows:
                                self.criminal_table.insert('',END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('Error',f'Due to{str(es)}')


if __name__=="__main__":
    main()
