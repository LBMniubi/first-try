import matplotlib.pyplot as plt
import numpy as np

import tkinter as tk  


def draw_sin():
    x = np.linspace(0,2*np.pi,30)
    #y1 = x**2
    #y2 = x**2 + 1000

    #y3 = np.exp(x)

    #y4 = 20000* np.sin(x)

    y5 = np.sin(x)

    plt.figure(2)
    plt.plot(y5,".")
    plt.title("y[n] = sin(pi*n/15)")
    #plt.title('$f(x) = -e^{4x}$')
    #plt.title(u"正弦波", fontproperties='SimHei')

    #plt.figure(30)
    #plt.plot(x,y4)
    plt.show()

def draw_n():
    x = np.linspace(0,30,30)
    y1 = x
    plt.figure(2)
    plt.plot(y1,".")
    plt.title("y[n] = n")
    plt.show()


def step_function(x):
    return np.array(x > 0, dtype=np.int)




def draw_u_n():
    X = np.arange(-15, 15, 1)
    Y = step_function(X)
    plt.plot(X, Y,".")
    plt.title("y[n] = u[n]")
    plt.ylim(-0.1, 1.1)  
    plt.show()

def draw_e():
    X = np.arange(-5, 25, 1)
    Y = np.exp(X/10)
    plt.plot(X, Y,".")
    plt.title("y[n] = e^[n/10]")
    plt.show()



if __name__ == "__main__":
    #draw_u_n()
    #draw_e()
    window = tk.Tk()
    
   
    window.title('My Window')
    
    
    window.geometry('500x300') 
    
    
    l = tk.Label(window, text='信号与系统 实验三', bg='white', font=('Arial', 12), width=30, height=2)
   
    
    
    l.pack()    
    

    b1 = tk.Button(window, text='y[n] = n', font=('Arial', 12), width=10, height=1, command=draw_n)
    b2 = tk.Button(window, text='y[n] = sin()', font=('Arial', 12), width=10, height=1, command=draw_sin)
    b3 = tk.Button(window, text='y[n] = u[n]', font=('Arial', 12), width=10, height=1, command=draw_u_n)
    b4 = tk.Button(window, text='y[n] = e^[n/10]', font=('Arial', 12), width=10, height=1, command=draw_e)

    num = 12
    b1.pack(padx=0, pady=num)
    b2.pack(padx=0, pady=num)
    b3.pack(padx=0, pady=num)
    b4.pack(padx=0, pady=num)



   
    window.mainloop()