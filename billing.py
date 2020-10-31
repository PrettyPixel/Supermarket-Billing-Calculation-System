from tkinter import *
from PIL import ImageTk,Image
import math,random
from tkinter import messagebox


class Supermarket_Billing:
	def __init__(self,root):
		self.root=root
		self.root.title("Super Market Billing System")
		self.root.iconbitmap('c:/billingsystem/bag_icon.ico')
		self.root.geometry("1600x1600+0+0")
		title=Label(self.root,text="SUPERMARKET  BILLING  SYSTEM",bg="pink",fg="crimson",font=("Alice",30,"bold"),pady=2,bd=8,relief=GROOVE).pack(fill=X)
		frame_1=LabelFrame(self.root,text="Customer Details",fg="crimson",bg="pink",font=("Times New Roman",20,"bold"),bd=10)
		frame_1.place(x=5,y=70,relwidth=1)


		#------------MY VARIABLES FOR ITEMS-----------
		self.pulse=IntVar()
		self.rice=IntVar()
		self.amul=IntVar()
		self.sauce=IntVar()
		self.oreo=IntVar()

		self.juice=IntVar()
		self.frooti=IntVar()
		self.tea=IntVar()
		self.thandai=IntVar()
		self.horlicks=IntVar()

		self.clinic=IntVar()
		self.himalayan=IntVar()
		self.oil=IntVar()
		self.lotion=IntVar()
		self.sanitizer=IntVar()

		self.harpic=IntVar()
		self.cell=IntVar()
		self.pril=IntVar()
		self.surf=IntVar()
		self.rin=IntVar()

		#         MY VARIBALES FOR TOTAL COST AND GST      
		self.food_cost=IntVar()
		self.beverages_cost=IntVar()
		self.personal_care_cost=IntVar()
		self.homecare_cost=IntVar()
		self.total_money=IntVar()

		self.gst1=IntVar()
		self.gst2=IntVar()
		self.gst3=IntVar()
		self.gst4=IntVar()

		#         MY ENTRIES
		self.myemail=StringVar()
		self.mob=StringVar()
		self.bill_username=StringVar()
		self.bill_nosearch=StringVar()
		ran=random.randint(1000,9999)
		self.bill_nosearch.set(str(ran))
		self.search=StringVar()

		

        
		user_email=Label(frame_1,text="Email Id",font=("Times New Roman",15,"bold"),fg="crimson",bg="pink").grid(row=0,column=0)
		email_entry=Entry(frame_1,textvariable=self.myemail,width=18,font=("arial",15),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=5)

		user_number=Label(frame_1,text="Mobile Number",font=("Times New Roman",15,"bold"),fg="crimson",bg="pink").grid(row=0,column=2)
		email_entry=Entry(frame_1,textvariable=self.mob,width=18,font=("arial",15),bd=5,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=5)

		user_bill_no=Label(frame_1,text="Bill Number",font=("Times New Roman",15,"bold"),fg="crimson",bg="pink").grid(row=0,column=4)
		bill_no_entry=Entry(frame_1,textvariable=self.bill_nosearch,width=18,font=("arial",15),bd=5,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=5)

		user_name=Label(frame_1,text="Your Name",font=("Times New Roman",15,"bold"),fg="crimson",bg="pink").grid(row=0,column=6)
		name_entry=Entry(frame_1,textvariable=self.bill_username,width=18,font=("arial",15),bd=5,relief=SUNKEN).grid(row=0,column=7,pady=5,padx=5)


		#------------FOOD FRAME--------
		frame_2=LabelFrame(self.root,text="FOOD",font=("Times New Roman",15,"bold"),fg="crimson",bg="pink",bd=5)
		frame_2.place(x=5,y=180,width=250,height=350)
        
		q1=Label(frame_2,text="Quantity",font=("Times New Roman",13,"bold"),fg="crimson",bg="pink",bd=5).grid(row=0,column=1)
		p1=Label(frame_2,text="Items",font=("Times New Roman",16,"bold"),fg="crimson",bg="pink",bd=5).grid(row=0,column=0)

		pulses=Label(frame_2,text="Rajma (Rs40/kg)",font=("Times New Roman",14,"bold"),fg="crimson",bg="pink",bd=5,padx=5,pady=5).grid(row=2,column=0,sticky="W")
		pulses_quantity=Entry(frame_2,textvariable=self.pulse,font=("Times New Roman",14,"bold"),bd=5,width=4,relief=SUNKEN).grid(row=2,column=1)

		rice=Label(frame_2,text="Rice (Rs30/kg)",font=("Times New Roman",14,"bold"),fg="crimson",bg="pink",bd=5,padx=5,pady=5).grid(row=3,column=0,sticky="W")
		rice_quantity=Entry(frame_2,textvariable=self.rice,font=("Times New Roman",14,"bold"),bd=5,width=4,relief=SUNKEN).grid(row=3,column=1)

		amul=Label(frame_2,text="Butter (Rs90/kg)",font=("Times New Roman",14,"bold"),fg="crimson",bg="pink",bd=5,padx=5,pady=5).grid(row=4,column=0,sticky="W")
		amul_quantity=Entry(frame_2,textvariable=self.amul,font=("Times New Roman",14,"bold"),bd=5,width=4,relief=SUNKEN).grid(row=4,column=1)

		ketchup=Label(frame_2,text="Ketchup (Rs35/-)",font=("Times New Roman",14,"bold"),fg="crimson",bg="pink",bd=5,padx=5,pady=5).grid(row=5,column=0,sticky="W")
		ketchup_quantity=Entry(frame_2,textvariable=self.sauce,font=("Times New Roman",14,"bold"),bd=5,width=4,relief=SUNKEN).grid(row=5,column=1)

		buiscuits=Label(frame_2,text="Oreo (Rs25/-)",font=("Times New Roman",14,"bold"),fg="crimson",bg="pink",bd=5,padx=5,pady=5).grid(row=6,column=0,sticky="W")
		buiscuits_quantity=Entry(frame_2,textvariable=self.oreo,font=("Times New Roman",14,"bold"),bd=5,width=4,relief=SUNKEN).grid(row=6,column=1)

		#------BILLING AREA------
		frame_3=Frame(self.root,relief=GROOVE,bd=8,bg="crimson")
		frame_3.place(x=505,y=180,width=520,height=350)
		bill_head=Label(frame_3,text="BILL GENERATION",font=("Times New Roman",14,"bold")).pack(fill=X)
		scrollbar=Scrollbar(frame_3,orient=VERTICAL)
		self.textplace=Text(frame_3,yscrollcommand=scrollbar.set,bg="white",fg="black")
		scrollbar.pack(side=RIGHT,fill=Y)
		scrollbar.config(command=self.textplace.yview)
		self.textplace.pack(fill=BOTH,expand=1)


		#------BEVERAGES--------
		frame_4=LabelFrame(self.root,text="BEVERAGES",font=("Times New Roman",15,"bold"),fg="crimson",bg="pink",bd=5)
		frame_4.place(x=255,y=180,width=250,height=350)

		q2=Label(frame_4,text="Quantity",font=("Times New Roman",13,"bold"),fg="crimson",bg="pink",bd=5).grid(row=0,column=1)
		p2=Label(frame_4,text="Items",font=("Times New Roman",16,"bold"),fg="crimson",bg="pink",bd=5).grid(row=0,column=0)

		real_juice=Label(frame_4,text="Juice (Rs50/-)",font=("Times New Roman",14,"bold"),fg="crimson",bg="pink",bd=5,padx=5,pady=5).grid(row=1,column=0,sticky="W")
		real_juice_quantity=Entry(frame_4,textvariable=self.juice,font=("Times New Roman",14,"bold"),bd=5,width=4,relief=SUNKEN).grid(row=1,column=1)

		frooti=Label(frame_4,text="Frooti (Rs35/-)",font=("Times New Roman",14,"bold"),fg="crimson",bg="pink",bd=5,padx=5,pady=5).grid(row=2,column=0,sticky="W")
		frooti_quantity=Entry(frame_4,textvariable=self.frooti,font=("Times New Roman",14,"bold"),bd=5,width=4,relief=SUNKEN).grid(row=2,column=1)

		tea=Label(frame_4,text="Tea (Rs60/-)",font=("Times New Roman",14,"bold"),fg="crimson",bg="pink",bd=5,padx=5,pady=5).grid(row=3,column=0,sticky="W")
		tea_quantity=Entry(frame_4,textvariable=self.tea,font=("Times New Roman",14,"bold"),bd=5,width=4,relief=SUNKEN).grid(row=3,column=1)

		thandai=Label(frame_4,text="Sharbat (Rs40/-)",font=("Times New Roman",14,"bold"),fg="crimson",bg="pink",bd=5,padx=5,pady=5).grid(row=4,column=0,sticky="W")
		thandai_quantity=Entry(frame_4,textvariable=self.thandai,font=("Times New Roman",14,"bold"),bd=5,width=4,relief=SUNKEN).grid(row=4,column=1)

		horlicks=Label(frame_4,text="Horlicks (Rs38/-)",font=("Times New Roman",14,"bold"),fg="crimson",bg="pink",bd=5,padx=5,pady=5).grid(row=5,column=0,sticky="W")
		horlicks_quantity=Entry(frame_4,textvariable=self.horlicks,font=("Times New Roman",14,"bold"),bd=5,width=4,relief=SUNKEN).grid(row=5,column=1)

		#--------PERSONAL CARE PRODUCTS FRAME-------
		frame_6=LabelFrame(self.root,text="PERSONAL CARE",font=("Times New Roman",15,"bold"),fg="crimson",bg="pink",bd=5)
		frame_6.place(x=1025,y=180,width=250,height=350)

		q3=Label(frame_6,text="Quantity",font=("Times New Roman",13,"bold"),fg="crimson",bg="pink",bd=5).grid(row=0,column=1)
		p3=Label(frame_6,text="Items",font=("Times New Roman",16,"bold"),fg="crimson",bg="pink",bd=5).grid(row=0,column=0)

		shampoo=Label(frame_6,text="Pantene (Rs70/-)",font=("Times New Roman",14,"bold"),fg="crimson",bg="pink",bd=5,padx=5,pady=5).grid(row=1,column=0,sticky="W")
		shampoo_quantity=Entry(frame_6,textvariable=self.clinic,font=("Times New Roman",14,"bold"),bd=5,width=4,relief=SUNKEN).grid(row=1,column=1)

		cream=Label(frame_6,text="Vaseline (Rs90/-)",font=("Times New Roman",14,"bold"),fg="crimson",bg="pink",bd=5,padx=5,pady=5).grid(row=2,column=0,sticky="W")
		cream_quantity=Entry(frame_6,textvariable=self.himalayan,font=("Times New Roman",14,"bold"),bd=5,width=4,relief=SUNKEN).grid(row=2,column=1)

		oil=Label(frame_6,text="Hair Oil (Rs40/-)",font=("Times New Roman",14,"bold"),fg="crimson",bg="pink",bd=5,padx=5,pady=5).grid(row=3,column=0,sticky="W")
		oil_quantity=Entry(frame_6,textvariable=self.oil,font=("Times New Roman",14,"bold"),bd=5,width=4,relief=SUNKEN).grid(row=3,column=1)

		dove=Label(frame_6,text="Dove (Rs15/-)",font=("Times New Roman",14,"bold"),fg="crimson",bg="pink",bd=5,padx=5,pady=5).grid(row=4,column=0,sticky="W")
		dove_quantity=Entry(frame_6,textvariable=self.lotion,font=("Times New Roman",14,"bold"),bd=5,width=4,relief=SUNKEN).grid(row=4,column=1)

		sanitizer=Label(frame_6,text="Sanitizer (Rs10/-)",font=("Times New Roman",14,"bold"),fg="crimson",bg="pink",bd=5,padx=5,pady=5).grid(row=5,column=0,sticky="W")
		sanitizer_quantity=Entry(frame_6,textvariable=self.sanitizer,font=("Times New Roman",14,"bold"),bd=5,width=4,relief=SUNKEN).grid(row=5,column=1)

		#-----------HOME CARE PRODUCTS-----------
		frame_7=LabelFrame(self.root,text="HOME CARE",font=("Times New Roman",15,"bold"),fg="crimson",bg="pink",bd=5)
		frame_7.place(x=1275,y=180,width=250,height=350)

		q4=Label(frame_7,text="Quantity",font=("Times New Roman",13,"bold"),fg="crimson",bg="pink",bd=5).grid(row=0,column=1)
		p4=Label(frame_7,text="Items",font=("Times New Roman",16,"bold"),fg="crimson",bg="pink",bd=5).grid(row=0,column=0)

		harpic=Label(frame_7,text="Harpic (Rs70/-)",font=("Times New Roman",14,"bold"),fg="crimson",bg="pink",bd=5,padx=5,pady=5).grid(row=1,column=0,sticky="W")
		harpic_quantity=Entry(frame_7,textvariable=self.harpic,font=("Times New Roman",14,"bold"),bd=5,width=4,relief=SUNKEN).grid(row=1,column=1)

		cell=Label(frame_7,text="Cell (Rs20/-)",font=("Times New Roman",14,"bold"),fg="crimson",bg="pink",bd=5,padx=5,pady=5).grid(row=2,column=0,sticky="W")
		cell_quantity=Entry(frame_7,textvariable=self.cell,font=("Times New Roman",14,"bold"),bd=5,width=4,relief=SUNKEN).grid(row=2,column=1)

		pril=Label(frame_7,text="Pril (Rs22/-)",font=("Times New Roman",14,"bold"),fg="crimson",bg="pink",bd=5,padx=5,pady=5).grid(row=3,column=0,sticky="W")
		pril_quantity=Entry(frame_7,textvariable=self.pril,font=("Times New Roman",14,"bold"),bd=5,width=4,relief=SUNKEN).grid(row=3,column=1)

		surf=Label(frame_7,text="Tide (Rs50/-)",font=("Times New Roman",14,"bold"),fg="crimson",bg="pink",bd=5,padx=5,pady=5).grid(row=4,column=0,sticky="W")
		surf_quantity=Entry(frame_7,textvariable=self.surf,font=("Times New Roman",14,"bold"),bd=5,width=4,relief=SUNKEN).grid(row=4,column=1)

		rin=Label(frame_7,text="Rin Bar (Rs10/-)",font=("Times New Roman",14,"bold"),fg="crimson",bg="pink",bd=5,padx=5,pady=5).grid(row=5,column=0,sticky="W")
		rin_quantity=Entry(frame_7,textvariable=self.rin,font=("Times New Roman",14,"bold"),bd=5,width=4,relief=SUNKEN).grid(row=5,column=1)

		#------BILLING FRAME 1-----

		frame_8=LabelFrame(self.root,text="BILLING",font=("Times New Roman",15,"bold"),fg="crimson",bg="pink",bd=5)
		frame_8.place(x=5,y=530,width=500,height=260)
		row_1=Label(frame_8,text="Food Cost",font=("Times New Roman",15,"bold"),bg="pink",fg="crimson").grid(row=0,column=0,padx=10,pady=2,sticky="W")
		row_1_entry=Entry(frame_8,textvariable=self.food_cost,width=6,font=("Times New Roman",15,"bold"),bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=2)

		row_2=Label(frame_8,text="Beverages Cost",font=("Times New Roman",15,"bold"),bg="pink",fg="crimson").grid(row=1,column=0,padx=10,pady=2,sticky="W")
		row_2_entry=Entry(frame_8,textvariable=self.beverages_cost,width=6,font=("Times New Roman",15,"bold"),bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=2)
		row_3=Label(frame_8,text="Personal Care Cost",font=("Times New Roman",15,"bold"),bg="pink",fg="crimson").grid(row=2,column=0,padx=10,pady=2,sticky="W")
		row_3_entry=Entry(frame_8,textvariable=self.personal_care_cost,width=6,font=("Times New Roman",15,"bold"),bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=2)
        
        

		
		row_4=Label(frame_8,text="HomeCare Cost",font=("Times New Roman",15,"bold"),bg="pink",fg="crimson").grid(row=3,column=0,padx=10,pady=2,sticky="W")
		row_4_entry=Entry(frame_8,textvariable=self.homecare_cost,width=6,font=("Times New Roman",15,"bold"),bd=7,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=2)

		row_5=Label(frame_8,text="TOTAL",font=("Times New Roman",15,"bold"),bg="pink",fg="crimson").grid(row=4,column=0,padx=10,pady=2,sticky="W")
		row_5_entry=Entry(frame_8,textvariable=self.total_money,width=6,font=("Times New Roman",15,"bold"),bd=7,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=2)

		#---------GST BLOCK---------

		next_1=Label(frame_8,text="GST",font=("Times New Roman",15,"bold"),bg="pink",fg="crimson").grid(row=0,column=2,padx=10,pady=2,sticky="W")
		next_1_entry=Entry(frame_8,textvariable=self.gst1,width=6,font=("Times New Roman",15,"bold"),bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=2)

		next_2=Label(frame_8,text="GST",font=("Times New Roman",15,"bold"),bg="pink",fg="crimson").grid(row=1,column=2,padx=10,pady=2,sticky="W")
		next_2_entry=Entry(frame_8,textvariable=self.gst2,width=6,font=("Times New Roman",15,"bold"),bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=2)

		next_3=Label(frame_8,text="GST",font=("Times New Roman",15,"bold"),bg="pink",fg="crimson").grid(row=2,column=2,padx=10,pady=2,sticky="W")
		next_3_entry=Entry(frame_8,textvariable=self.gst3,width=6,font=("Times New Roman",15,"bold"),bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=2)

		next_4=Label(frame_8,text="GST",font=("Times New Roman",15,"bold"),bg="pink",fg="crimson").grid(row=3,column=2,padx=10,pady=2,sticky="W")
		next_4_entry=Entry(frame_8,textvariable=self.gst4,width=6,font=("Times New Roman",15,"bold"),bd=7,relief=SUNKEN).grid(row=3,column=3,padx=10,pady=2)
        
        
        #----BUTTON FRAMES 2-----
		frame_9=LabelFrame(self.root,text="BILLING",font=("Times New Roman",15,"bold"),fg="crimson",bg="pink",bd=5)
		frame_9.place(x=1025,y=530,width=500,height=260)

		 #------right bottom framee----
		my_buttons=Frame(frame_9,bd=5,relief=GROOVE)
		my_buttons.place(x=15,y=2,width=460,height=220)

		thankyou=Label(my_buttons,text="Thank You For Shopping!",font=("Times new Roman",20,"bold"),fg="crimson")
		thankyou.place(x=70,y=5)


		b1=Button(my_buttons,command=self.total,bd=3,text="Total",fg="white",bg="crimson",pady=5,font=("Times New Roman",15,"bold"),width=10,height=1)
		b1.place(x=10,y=50)

		b2=Button(my_buttons,command=self.konoha_bill2,bd=3,text="Create Bill",fg="white",bg="crimson",pady=5,font=("Times New Roman",15,"bold"),width=10,height=1)
		b2.place(x=300,y=50)

		b3=Button(my_buttons,command=self.reset_info,bd=3,text="Reset",fg="white",bg="crimson",pady=5,font=("Times New Roman",15,"bold"),width=10,height=1)
		b3.place(x=300,y=120)

		b4=Button(my_buttons,bd=3,command=self.quit,text="Quit",fg="white",bg="crimson",pady=5,font=("Times New Roman",15,"bold"),width=10,height=1)
		b4.place(x=10,y=120)
		

	def total(self):
		self.pulse1=self.pulse.get()
		self.rice1=self.rice.get()
		self.amul1=self.amul.get()
		self.sauce1=self.sauce.get()
		self.oreo1=self.oreo.get()
		self.totalfoodprice=float(
			            (self.pulse1*40)+
			            (self.rice1*30)+
			            (self.amul1*90)+
			            (self.sauce1*35)+
			            (self.oreo1*25)

                       )
		self.food_cost.set(str(self.totalfoodprice))
		self.gst1.set(str(self.totalfoodprice*0.05))


		self.juice1=self.juice.get()
		self.frooti1=self.frooti.get()
		self.tea1=self.tea.get()
		self.thandai1=self.thandai.get()
		self.horlicks1=self.horlicks.get()
		self.totalbeverageprice=float(
			            (self.juice1*50)+
			            (self.frooti1*35)+
			            (self.tea1*60)+
			            (self.thandai1*40)+
			            (self.horlicks1*38)
                        )
		self.beverages_cost.set(str(self.totalbeverageprice))
		self.gst2.set(str(self.totalbeverageprice*0.02))


		self.clinic1=self.clinic.get()
		self.himalayan1=self.himalayan.get()
		self.oil1=self.oil.get()
		self.lotion1=self.lotion.get()
		self.sanitizer1=self.sanitizer.get()
		self.totalpersonal_care_price=float(
			            (self.clinic1*70)+
			            (self.himalayan1*90)+
			            (self.oil1*40)+
			            (self.lotion1*15)+
			            (self.sanitizer1*10)

                       )
		self.personal_care_cost.set(str(self.totalpersonal_care_price))
		self.gst3.set(str(self.totalpersonal_care_price*0.05))


		self.harpic1=(self.harpic.get())
		self.cell1=self.cell.get()
		self.pril1=self.pril.get()
		self.surf1=self.surf.get()
		self.rin1=self.rin.get()

		self.totalhome_care_price=float(
			            (self.harpic1*70)+
			            (self.cell1*20)+
			            (self.pril1*22)+
			            (self.surf1*50)+
			            (self.rin1*10)

                       )
		self.homecare_cost.set(str(self.totalhome_care_price))
		self.gst4.set(str(self.totalhome_care_price*0.05))

		self.total_rs=float(self.totalfoodprice+self.totalbeverageprice+self.totalpersonal_care_price+self.totalhome_care_price)

		self.total_money.set(str(self.total_rs)) 

	def konoha_bill2(self):
		self.textplace.insert(END,"\t---------------Kohona Supermarket--------------")
		self.textplace.insert(END,f"\n                      ******WELCOME******")
		self.textplace.insert(END,f"\n                    Contact : 7833449010")
		self.textplace.insert(END,f"\n                    Email : konoha@gmail.com")
		self.textplace.insert(END,"\n************************************************************")
		self.textplace.insert(END,f"\n          BILL NUMBER      {self.bill_nosearch.get()}")
		self.textplace.insert(END,f"\n          EMAIL ID         {self.myemail.get()}")
		self.textplace.insert(END,f"\n          MOBILE NUMBER    {self.mob.get()}")
		self.textplace.insert(END,f"\n          YOUR NAME        {self.bill_username.get()}")
		self.textplace.insert(END,f"\n**WELCOME********WELCOME*****WELCOME**********WELCOME******")
		self.textplace.insert(END,f"\n   \tITEMS \t\tQUANTITY  \t\tCOST")
		self.textplace.insert(END,f"\n------------------------------------------------------------")
		if self.pulse1!=0:
			self.textplace.insert(END,f"\n   \tPulse \t\t{self.pulse1}  \t\t{self.pulse1 * 40}")
		if self.rice1!=0:
			self.textplace.insert(END,f"\n   \tRice \t\t{self.rice1}  \t\t{self.rice1 * 30}")
		if self.amul1!=0:
			self.textplace.insert(END,f"\n   \tAmul Butter \t\t{self.amul1}  \t\t{self.amul1 * 90}")
		if self.sauce1!=0:
			self.textplace.insert(END,f"\n   \tSauce \t\t{self.sauce1}  \t\t{self.sauce1 * 35}")
		if self.oreo1!=0:
			self.textplace.insert(END,f"\n   \tOreo \t\t{self.oreo1}  \t\t{self.oreo1 * 25}")

		if self.juice1!=0:
			self.textplace.insert(END,f"\n   \tReal Juice \t\t{self.juice1}  \t\t{self.juice1 * 50}")
		if self.frooti1!=0:
			self.textplace.insert(END,f"\n   \tFrooti \t\t{self.frooti1}  \t\t{self.frooti1 * 35}")
		if self.tea1!=0:
			self.textplace.insert(END,f"\n   \tTea Powder \t\t{self.tea1}  \t\t{self.tea1 * 60}")
		if self.thandai1!=0:
			self.textplace.insert(END,f"\n   \tThandai \t\t{self.thandai1}  \t\t{self.thandai1 * 40}")
		if self.horlicks1!=0:
			self.textplace.insert(END,f"\n   \tHorlicks \t\t{self.horlicks1}  \t\t{self.horlicks1 * 38}")
		if self.clinic1!=0:
			self.textplace.insert(END,f"\n   \tPantene \t\t{self.clinic1}  \t\t{self.clinic1 * 70}")
		if self.himalayan1!=0:
			self.textplace.insert(END,f"\n   \tVaseline \t\t{self.himalayan1}  \t\t{self.himalayan1 * 90}")
		if self.oil1!=0:
			self.textplace.insert(END,f"\n   \tHair Oil \t\t{self.oil1}  \t\t{self.oil1 * 40}")
		if self.lotion1!=0:
			self.textplace.insert(END,f"\n   \tDove Lotion \t\t{self.lotion1}  \t\t{self.lotion1 * 15}")
		if self.sanitizer1!=0:
			self.textplace.insert(END,f"\n   \tSanitizer \t\t{self.sanitizer1}  \t\t{self.sanitizer1 * 10}")

		if self.harpic1!=0:
			self.textplace.insert(END,f"\n   \tHarpic\t\t{self.harpic1}  \t\t{self.harpic1 * 70}")
		if self.cell1!=0:
			self.textplace.insert(END,f"\n   \tCell\t\t{self.cell1}  \t\t{self.cell1 * 22}")
		if self.pril1!=0:
			self.textplace.insert(END,f"\n   \tPril\t\t{self.pril1}  \t\t{self.pril1 * 20}")
		if self.surf1!=0:
			self.textplace.insert(END,f"\n   \tTide\t\t{self.surf1}  \t\t{self.surf1 * 50}")
		if self.rin1!=0:
			self.textplace.insert(END,f"\n   \tRin Bar\t\t{self.rin1}  \t\t{self.rin1 * 10}")

	def reset_info(self):
		self.pulse.set(0)
		self.rice.set(0)
		self.amul.set(0)
		self.sauce.set(0)
		self.oreo.set(0)

		self.juice.set(0)
		self.frooti.set(0)
		self.tea.set(0)
		self.thandai.set(0)
		self.horlicks.set(0)

		self.clinic.set(0)
		self.himalayan.set(0)
		self.oil.set(0)
		self.lotion.set(0)
		self.sanitizer.set(0)

		self.harpic.set(0)
		self.cell.set(0)
		self.pril.set(0)
		self.surf.set(0)
		self.rin.set(0)

		self.food_cost.set(0)
		self.beverages_cost.set(0)
		self.personal_care_cost.set(0)
		self.homecare_cost.set(0)
		self.total_money.set(0)

		self.gst1.set(0)
		self.gst2.set(0)
		self.gst3.set(0)
		self.gst4.set(0)

		#         MY ENTRIES
		self.myemail.set("")
		self.mob.set("")
		self.bill_nosearch=StringVar("")
		ran=random.randint(1000,9999)
		self.bill_nosearch.set(str(ran))
		self.search.set(0)
		self.beverages_cost.set(0)
		self.personal_care_cost.set(0)
		self.homecare_cost.set(0)
		self.total_money.set(0)

		self.textplace.delete(0.1,END)
	def quit(self):
		display=messagebox.askyesno("Exit","Are you sure you want to exit the program?")
		if display>0:
			self.root.destroy()

root=Tk()
amul_image=ImageTk.PhotoImage(Image.open("market.jpeg"))
bgimage=Label(image=amul_image,width=518,height=250)
bgimage.place(x=505,y=532)

obj=Supermarket_Billing(root)
root.mainloop()
