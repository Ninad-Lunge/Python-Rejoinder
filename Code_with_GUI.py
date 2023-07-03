import tkinter as tk
from tkinter import *
import math

LARGEFONT =("Verdana", 10)

class tkinterApp(tk.Tk):
    
    def __init__(self, *args, **kwargs):
    
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for F in (homepage, Page1, Page2, Page3):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")
        self.show_frame(homepage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class homepage(tk.Frame):

    def __init__(self, parent, contoller):
        tk.Frame.__init__(self, parent)

        choice = "Enter a : For Thin Film Interference\nEnter b : For Newton's Rings\nEnter c : For Optical Fibre"
        msg = Message(self, text=choice, width=300)
        msg.config(bg="lightblue")
        msg.grid(row=0, column=1)

        tk.Label(self, text="Enter your choice: ").grid(row=5, column=0)
        e1 = tk.Entry(self)
        e1.grid(row=5, column=1)		

        def display():
            if e1.get() == "a":
                contoller.show_frame(Page1)
            if e1.get() == "b":
                contoller.show_frame(Page2)
            if e1.get() == "c":
                contoller.show_frame(Page3)

        b1 = tk.Button(self, text="Enter", command = display, width=10)
        b1.grid(row=6, column=1, pady=5)

class Page1(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text ="Thin film Interfernce", font = LARGEFONT)
        label.grid(row = 0, column = 0)
        
        choice = '''Enter 1 - To find : Minimum thickness of a thin flim if it appears dark
Enter 2 - To find : Minimum thickness of a thin film if it appears bright
Enter 3 - To find : Wavelength of light if thin film appears dark
Enter 4 - To find : Wavelength of light if thin film appears bright
Enter 5 - To find : Refractive Index of Film if thin film appears dark
Enter 6 - To find : Refractive Index of Film if thin film appears bright'''
        msg = Message(self, text=choice, width=450)
        msg.config(bg="lightblue")
        msg.grid(row=1, column=0)

        tk.Label(self, text="Enter your choice: ").grid(row=7, column=0)
        e1 = tk.Entry(self)
        e1.grid(row=8, column=0)

        def display():
            if e1.get() == "1":
                Label(self, text="Enter the wavelength : ").grid(row=10, column=0)
                e2 = tk.Entry(self)
                e2.grid(row=10, column=1)
                Label(self, text="Enter the refractive index : ").grid(row=11, column=0)
                e3 = tk.Entry(self)
                e3.grid(row=11, column=1)
                Label(self, text="Enter the angle of refraction : ").grid(row=12, column=0)
                e4 = tk.Entry(self)
                e4.grid(row=12, column=1)
                n = 1

                def compute():
                    wavelength = float(e2.get())
                    refractive_index = float(e3.get())
                    theta = float(e4.get())

                    tmin = (n*wavelength)/(2*refractive_index*math.cos(theta))
                    l1 = Label(self, text=f"The minimum thickness of the film is : {tmin}")
                    l1.grid(row=14, column=0)

                b2 = Button(self, text="Compute", command=compute)
                b2.grid(row=13,column=0)
                
            if e1.get() == "2":
                Label(self, text="Enter the wavelength (in nm) : ").grid(row=10, column=0)
                e2 = tk.Entry(self)
                e2.grid(row=10, column=1)
                Label(self, text="Enter the refractive index : ").grid(row=11, column=0)
                e3 = tk.Entry(self)
                e3.grid(row=11, column=1)
                Label(self, text="Enter the angle of refraction (in degree) : ").grid(row=12, column=0)
                e4 = tk.Entry(self)
                e4.grid(row=12, column=1)
                n = 0

                def compute():
                    wavelength = float(e2.get())
                    refractive_index = float(e3.get())
                    theta = float(e4.get())

                    tmin = ((2*n+1)*wavelength)/(4*refractive_index*math.cos(theta))
                    l1 = Label(self, text=f"The minimum thickness of the film is : {tmin}")
                    l1.grid(row=14, column=0)

                b2 = Button(self, text="Compute", command=compute)
                b2.grid(row=13,column=0)

            if e1.get() == "3":
                Label(self, text="Enter the thickness of the film : ").grid(row=10, column=0)
                e2 = tk.Entry(self)
                e2.grid(row=10, column=1)
                Label(self, text="Enter the refractive index : ").grid(row=11, column=0)
                e3 = tk.Entry(self)
                e3.grid(row=11, column=1)
                Label(self, text="Enter the angle of refraction : ").grid(row=12, column=0)
                e4 = tk.Entry(self)
                e4.grid(row=12, column=1)
                n = 1

                def compute():
                    thickness = float(e2.get())
                    refractive_index = float(e3.get())
                    theta = float(e4.get())

                    wavelength = (2*refractive_index*thickness*math.cos(theta))/n
                    l1 = Label(self, text=f"Wavelength of light is : {wavelength}")
                    l1.grid(row=14, column=0)

                b2 = Button(self, text="Compute", command=compute)
                b2.grid(row=13,column=0)

            if e1.get() == "4":
                Label(self, text="Enter the thickness of the film : ").grid(row=10, column=0)
                e2 = tk.Entry(self)
                e2.grid(row=10, column=1)
                Label(self, text="Enter the refractive index : ").grid(row=11, column=0)
                e3 = tk.Entry(self)
                e3.grid(row=11, column=1)
                Label(self, text="Enter the angle of refraction : ").grid(row=12, column=0)
                e4 = tk.Entry(self)
                e4.grid(row=12, column=1)
                n = 0

                def compute():
                    thickness = float(e2.get())
                    refractive_index = float(e3.get())
                    theta = float(e4.get())

                    wavelength = (4*refractive_index*thickness*math.cos(theta))/(2*n+1)
                    l1 = Label(self, text=f"Wavelength of light is : {wavelength}")
                    l1.grid(row=14, column=0)

                b2 = Button(self, text="Compute", command=compute)
                b2.grid(row=13,column=0)

            if e1.get() == "5":
                Label(self, text="Enter the wavelength : ").grid(row=10, column=0)
                e2 = tk.Entry(self)
                e2.grid(row=10, column=1)
                Label(self, text="Enter the thickness of the film : ").grid(row=11, column=0)
                e3 = tk.Entry(self)
                e3.grid(row=11, column=1)
                Label(self, text="Enter the angle of refraction : ").grid(row=12, column=0)
                e4 = tk.Entry(self)
                e4.grid(row=12, column=1)
                n = 1

                def compute():
                    wavelength = float(e2.get())
                    thickness = float(e3.get())
                    theta = float(e4.get())

                    refractive_index = (n*wavelength)/(2*thickness*math.cos(theta))
                    l1 = Label(self, text=f"Refractive Index of film is : {refractive_index}")
                    l1.grid(row=14, column=0)

                b2 = Button(self, text="Compute", command=compute)
                b2.grid(row=13,column=0)

            if e1.get() == "6":
                Label(self, text="Enter the wavelength : ").grid(row=10, column=0)
                e2 = tk.Entry(self)
                e2.grid(row=10, column=1)
                Label(self, text="Enter the thickness of the film : ").grid(row=11, column=0)
                e3 = tk.Entry(self)
                e3.grid(row=11, column=1)
                Label(self, text="Enter the angle of refraction : ").grid(row=12, column=0)
                e4 = tk.Entry(self)
                e4.grid(row=12, column=1)
                n = 0

                def compute():
                    wavelength = float(e2.get())
                    thickness = float(e3.get())
                    theta = float(e4.get())

                    refractive_index = ((2*n+1)*wavelength)/(4*thickness*math.cos(theta))
                    l1 = Label(self, text=f"Refractive Index of film is : {refractive_index}")
                    l1.grid(row=14, column=0)

                b2 = Button(self, text="Compute", command=compute)
                b2.grid(row=13,column=0)

        b1 = tk.Button(self, text="Enter", command = display, width=10)
        b1.grid(row=9, column=0, pady=5)

        bexit = tk.Button(self, text="Home Page", command = lambda : controller.show_frame(homepage), width=10)
        bexit.grid(row=20, column=0, pady=5)

class Page2(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text ="Newton's Rings", font = LARGEFONT)
        label.grid(row = 0, column = 0)
        
        choice = '''Enter 1 - To find : Thickness of film
Enter 2 - To find : Radius of Curvature of lens
Enter 3 - To find : Distance of film from point of contact
Enter 4 - To find : Wavelength of ligth if thin film appears bright
Enter 5 - To find : Radius of Curvature if diameter of two rings is given'''
        msg = Message(self, text=choice, width=450)
        msg.config(bg="lightblue", justify="left")
        msg.grid(row=1, column=0)

        tk.Label(self, text="Enter your choice: ").grid(row=7, column=0)
        e1 = tk.Entry(self)
        e1.grid(row=8, column=0)

        def display():
            if e1.get() == "1":
                Label(self, text="Enter distance of film from point of contact : ").grid(row=10, column=0)
                e2 = tk.Entry(self)
                e2.grid(row=10, column=1)
                Label(self, text="Enter the Radius of Curvature of the Lens : ").grid(row=11, column=0)
                e3 = tk.Entry(self)
                e3.grid(row=11, column=1)

                def compute():
                    distance = float(e2.get())
                    rad_curvature = float(e3.get())

                    thickness = (distance*distance)/2*rad_curvature
                    l1 = Label(self, text=f"Thickness of film is : {thickness}")
                    l1.grid(row=14, column=0)

                b2 = Button(self, text="Compute", command=compute)
                b2.grid(row=13,column=0)
                
            if e1.get() == "2":
                Label(self, text="Enter distance of film from point of contact : ").grid(row=10, column=0)
                e2 = tk.Entry(self)
                e2.grid(row=10, column=1)
                Label(self, text="Enter the thickness of film : ").grid(row=11, column=0)
                e3 = tk.Entry(self)
                e3.grid(row=11, column=1)

                def compute():
                    distance = float(e2.get())
                    thickness = float(e3.get())

                    rad_curvature = (distance*distance)/2*thickness
                    l1 = Label(self, text=f"Radius of Curvature of Lens is : {rad_curvature}")
                    l1.grid(row=14, column=0)

                b2 = Button(self, text="Compute", command=compute)
                b2.grid(row=13,column=0)

            if e1.get() == "3":
                Label(self, text="Enter the thickness of film : ").grid(row=10, column=0)
                e2 = tk.Entry(self)
                e2.grid(row=10, column=1)
                Label(self, text="Enter the Radius of Curvature of the Lens : ").grid(row=11, column=0)
                e3 = tk.Entry(self)
                e3.grid(row=11, column=1)

                def compute():
                    thickness = float(e2.get())
                    rad_curvature = float(e3.get())

                    distance = math.sqrt(2*thickness*rad_curvature)
                    l1 = Label(self, text=f"Distance of film from point of contact is : {distance}")
                    l1.grid(row=14, column=0)

                b2 = Button(self, text="Compute", command=compute)
                b2.grid(row=13,column=0)

            if e1.get() == "4":
                Label(self, text="Enter the diameter of larger ring : ").grid(row=10, column=0)
                e2 = tk.Entry(self)
                e2.grid(row=10, column=1)
                Label(self, text="Enter the diametr of smaller ring : ").grid(row=11, column=0)
                e3 = tk.Entry(self)
                e3.grid(row=11, column=1)
                Label(self, text="Enter the value of n : ").grid(row=12, column=0)
                e4 = tk.Entry(self)
                e4.grid(row=12, column=1)
                Label(self, text="Enter the value of m : ").grid(row=13, column=0)
                e5 = tk.Entry(self)
                e5.grid(row=13, column=1)
                Label(self, text="Enter the wavelength of light used : ").grid(row=14, column=0)
                e6 = tk.Entry(self)
                e6.grid(row=14, column=1)

                def compute():
                    dn = float(e2.get())
                    dm = float(e3.get())
                    n = float(e4.get())
                    m = float(e5.get())
                    wavelength = float(e6.get())

                    rad_cu = ((dn*dn)-(dm*dm))/(4*wavelength*(n-m))
                    l1 = Label(self, text=f"Radius of Curvature of lens is : {rad_cu}")
                    l1.grid(row=16, column=0)

                b2 = Button(self, text="Compute", command=compute)
                b2.grid(row=15,column=0)

            if e1.get() == "4":
                Label(self, text="Enter the diameter of larger ring : ").grid(row=10, column=0)
                e2 = tk.Entry(self)
                e2.grid(row=10, column=1)
                Label(self, text="Enter the diametr of smaller ring : ").grid(row=11, column=0)
                e3 = tk.Entry(self)
                e3.grid(row=11, column=1)
                Label(self, text="Enter the value of n : ").grid(row=12, column=0)
                e4 = tk.Entry(self)
                e4.grid(row=12, column=1)
                Label(self, text="Enter the value of m : ").grid(row=13, column=0)
                e5 = tk.Entry(self)
                e5.grid(row=13, column=1)
                Label(self, text="Enter the Radius of curvature of lens : ").grid(row=14, column=0)
                e6 = tk.Entry(self)
                e6.grid(row=14, column=1)

                def compute():
                    dn = float(e2.get())
                    dm = float(e3.get())
                    n = float(e4.get())
                    m = float(e5.get())
                    rad_cu = float(e6.get())

                    wavelength = ((dn*dn)-(dm*dm))/(4*rad_cu*(n-m))
                    l1 = Label(self, text=f"Wavelength of ligth used is : {wavelength}")
                    l1.grid(row=16, column=0)

                b2 = Button(self, text="Compute", command=compute)
                b2.grid(row=15,column=0)

        b1 = tk.Button(self, text="Enter", command = display, width=10)
        b1.grid(row=9, column=0, pady=5)

        bexit = tk.Button(self, text="Home Page", command = lambda : controller.show_frame(homepage), width=10)
        bexit.grid(row=20, column=0, pady=5)

class Page3(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text ="Optical Fibre", font = LARGEFONT)
        label.grid(row = 0, column = 0)
        
        choice = '''Enter 1 - To find : Accetance Angle
Enter 2 - To find : Refractive Index of core
Enter 3 - To find : Refractive Index of clad
Enter 4 - To find : Numerical Aperature
Enter 5 - To find : Fractional Refractive Index'''
        msg = Message(self, text=choice, width=450)
        msg.config(bg="lightblue", justify="left")
        msg.grid(row=1, column=0)

        tk.Label(self, text="Enter your choice: ").grid(row=7, column=0)
        e1 = tk.Entry(self)
        e1.grid(row=8, column=0)

        def display():
            if e1.get() == "1":
                Label(self, text="Enter the Refractive Index of core : ").grid(row=10, column=0)
                e2 = tk.Entry(self)
                e2.grid(row=10, column=1)
                Label(self, text="Enter the Refractive Index of clad : ").grid(row=11, column=0)
                e3 = tk.Entry(self)
                e3.grid(row=11, column=1)

                def compute():
                    core = float(e2.get())
                    clad = float(e3.get())

                    acceptance_angle = math.asin(math.sqrt((core*core)-(clad*clad)))
                    l1 = Label(self, text=f"Acceptance angle Optical Fibre is : {math.degrees(acceptance_angle)}")
                    l1.grid(row=14, column=0)

                b2 = Button(self, text="Compute", command=compute)
                b2.grid(row=13,column=0)

            if e1.get() == "2":
                Label(self, text="Enter the Refractive Index of clad : ").grid(row=10, column=0)
                e2 = tk.Entry(self)
                e2.grid(row=10, column=1)
                Label(self, text="Enter the Acceptance angle of Optical Fibre : ").grid(row=11, column=0)
                e3 = tk.Entry(self)
                e3.grid(row=11, column=1)

                def compute():
                    clad = float(e2.get())
                    acceptance_angle = float(e3.get())

                    a = (math.sin(acceptance_angle) ** 2) + (clad*clad)
                    core = math.sqrt(a)
                    l1 = Label(self, text=f"The Refractive Index of Core is : {core}")
                    l1.grid(row=14, column=0)

                b2 = Button(self, text="Compute", command=compute)
                b2.grid(row=13,column=0)

            if e1.get() == "3":
                Label(self, text="Enter the Refractive Index of core : ").grid(row=10, column=0)
                e2 = tk.Entry(self)
                e2.grid(row=10, column=1)
                Label(self, text="Enter the Acceptance angle of Optical Fibre : ").grid(row=11, column=0)
                e3 = tk.Entry(self)
                e3.grid(row=11, column=1)

                def compute():
                    core = float(e2.get())
                    acceptance_angle = float(e3.get())

                    clad = math.sqrt((core*core) - (math.sin(acceptance_angle) ** 2))
                    l1 = Label(self, text=f"Refractive Index of Clad is : {clad}")
                    l1.grid(row=14, column=0)

                b2 = Button(self, text="Compute", command=compute)
                b2.grid(row=13,column=0)

            if e1.get() == "4":
                Label(self, text="Enter the Refractive Index of core : ").grid(row=10, column=0)
                e2 = tk.Entry(self)
                e2.grid(row=10, column=1)
                Label(self, text="Enter the Refractive Index of clad : ").grid(row=11, column=0)
                e3 = tk.Entry(self)
                e3.grid(row=11, column=1)

                def compute():
                    core = float(e2.get())
                    clad = float(e3.get())

                    numerical_apperature = math.sqrt((core*core)-(clad*clad))
                    l1 = Label(self, text=f"Numerical Apperature of Optical fibre is : {numerical_apperature}")
                    l1.grid(row=14, column=0)

                b2 = Button(self, text="Compute", command=compute)
                b2.grid(row=13,column=0)

            if e1.get() == "5":
                Label(self, text="Enter the Refractive Index of core : ").grid(row=10, column=0)
                e2 = tk.Entry(self)
                e2.grid(row=10, column=1)
                Label(self, text="Enter the Refractive Index of clad : ").grid(row=11, column=0)
                e3 = tk.Entry(self)
                e3.grid(row=11, column=1)

                def compute():
                    core = float(e2.get())
                    clad = float(e3.get())

                    fri = (core-clad)/clad
                    l1 = Label(self, text=f"Fractional Refractive Index of Optical Fibre is : {fri}")
                    l1.grid(row=14, column=0)

                b2 = Button(self, text="Compute", command=compute)
                b2.grid(row=13,column=0)

        b1 = tk.Button(self, text="Enter", command = display, width=10)
        b1.grid(row=9, column=0, pady=5)

        bexit = tk.Button(self, text="Home Page", command = lambda : controller.show_frame(homepage), width=10)
        bexit.grid(row=20, column=0, pady=5)

master = tkinterApp()
master.title("Python Rejoinder")
master.geometry("650x350")
master.mainloop()