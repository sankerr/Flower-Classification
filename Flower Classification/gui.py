# gui class
# That class create the gui for this app
import os
import sys


try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import gui_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    gui_support.init(root, top)
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    root.iconbitmap(os.path.join(base_path, "Resources/icon.ico"))
    root.resizable(False,False)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    gui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None
    sys.exit(0)


# create the main window of the app
class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Segoe UI} -size 20 -weight bold -slant "  \
            "italic -underline 0 -overstrike 0"
        font12 = "-family {Segoe UI} -size 10 -weight bold -slant " \
                 "italic -underline 0 -overstrike 0"

        top.geometry("600x270")
        top.title("Flower Species Recognition")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        self.Label_0 = tk.Label(top)
        self.Label_0.place(relx=0.18, rely=0.037, height=51, width=400)
        self.Label_0.configure(activebackground="#f9f9f9")
        self.Label_0.configure(activeforeground="black")
        self.Label_0.configure(background="#d9d9d9")
        self.Label_0.configure(disabledforeground="#a3a3a3")
        self.Label_0.configure(font=font10)
        self.Label_0.configure(foreground="#000000")
        self.Label_0.configure(highlightbackground="#501fef")
        self.Label_0.configure(highlightcolor="#1f1863")
        self.Label_0.configure(text='''Flower Species Recognition''')


        self.Label_1 = tk.Label(top)
        self.Label_1.place(relx=0.04, rely=0.3, height=21, width=150)
        self.Label_1.configure(activebackground="#f9f9f9")
        self.Label_1.configure(activeforeground="black")
        self.Label_1.configure(background="#d9d9d9")
        self.Label_1.configure(disabledforeground="#a3a3a3")
        self.Label_1.configure(foreground="#000000")
        self.Label_1.configure(highlightbackground="#d9d9d9")
        self.Label_1.configure(highlightcolor="black")
        self.Label_1.configure(text='''Train model path''')
        self.Label_1.configure(font=font12)


        self.Label_2 = tk.Label(top)
        self.Label_2.place(relx=0.04, rely=0.4, height=21, width=150)
        self.Label_2.configure(activebackground="#f9f9f9")
        self.Label_2.configure(activeforeground="black")
        self.Label_2.configure(background="#d9d9d9")
        self.Label_2.configure(disabledforeground="#a3a3a3")
        self.Label_2.configure(foreground="#000000")
        self.Label_2.configure(highlightbackground="#d9d9d9")
        self.Label_2.configure(highlightcolor="black")
        self.Label_2.configure(text='''Image flowers directory''')
        self.Label_2.configure(font=font12)

        self.Label_3 = tk.Label(top)
        self.Label_3.place(relx=0.05, rely=0.5, height=21, width=135)
        self.Label_3.configure(activebackground="#f9f9f9")
        self.Label_3.configure(activeforeground="black")
        self.Label_3.configure(background="#d9d9d9")
        self.Label_3.configure(disabledforeground="#a3a3a3")
        self.Label_3.configure(foreground="#000000")
        self.Label_3.configure(highlightbackground="#d9d9d9")
        self.Label_3.configure(highlightcolor="black")
        self.Label_3.configure(text='''Save destination''')
        self.Label_3.configure(font=font12)


        self.model_btn = tk.Button(top)
        self.model_btn.place(relx=0.87, rely=0.3, height=20, width=49)
        self.model_btn.configure(activebackground="#ececec")
        self.model_btn.configure(activeforeground="#000000")
        self.model_btn.configure(background="#d9d9d9")
        self.model_btn.configure(disabledforeground="#a3a3a3")
        self.model_btn.configure(foreground="#000000")
        self.model_btn.configure(highlightbackground="#d9d9d9")
        self.model_btn.configure(highlightcolor="black")
        self.model_btn.configure(pady="0")
        self.model_btn.configure(text='''Browse''')
        self.model_btn.bind('<Button-1>',lambda e:gui_support.upload_model())

        self.flower_dir = tk.Button(top)
        self.flower_dir.place(relx=0.87, rely=0.4, height=20, width=49)
        self.flower_dir.configure(activebackground="#ececec")
        self.flower_dir.configure(activeforeground="#000000")
        self.flower_dir.configure(background="#d9d9d9")
        self.flower_dir.configure(disabledforeground="#a3a3a3")
        self.flower_dir.configure(foreground="#000000")
        self.flower_dir.configure(highlightbackground="#d9d9d9")
        self.flower_dir.configure(highlightcolor="black")
        self.flower_dir.configure(pady="0")
        self.flower_dir.configure(text='''Browse''')
        self.flower_dir.bind('<Button-1>',lambda e:gui_support.load_flower_dir())

        self.destination_path_btn = tk.Button(top)
        self.destination_path_btn.place(relx=0.87, rely=0.5, height=20, width=49)
        self.destination_path_btn.configure(activebackground="#ececec")
        self.destination_path_btn.configure(activeforeground="#000000")
        self.destination_path_btn.configure(background="#d9d9d9")
        self.destination_path_btn.configure(disabledforeground="#a3a3a3")
        self.destination_path_btn.configure(foreground="#000000")
        self.destination_path_btn.configure(highlightbackground="#d9d9d9")
        self.destination_path_btn.configure(highlightcolor="black")
        self.destination_path_btn.configure(pady="0")
        self.destination_path_btn.configure(state="normal")
        self.destination_path_btn.configure(text='''Browse''')
        self.destination_path_btn.bind('<Button-1>', lambda e: gui_support.dest_path())


        self.Entry_1 = tk.Entry(top)
        self.Entry_1.place(relx=0.31, rely=0.3, height=20, relwidth=0.55)
        self.Entry_1.configure(background="white")
        self.Entry_1.configure(disabledforeground="#a3a3a3")
        self.Entry_1.configure(font="TkFixedFont")
        self.Entry_1.configure(foreground="#000000")
        self.Entry_1.configure(insertbackground="black")
        self.Entry_1.configure(width=184)
        self.Entry_1.configure(x=tk.StringVar())

        self.Entry_2 = tk.Entry(top)
        self.Entry_2.place(relx=0.31, rely=0.4, height=20, relwidth=0.55)
        self.Entry_2.configure(background="white")
        self.Entry_2.configure(disabledforeground="#a3a3a3")
        self.Entry_2.configure(font="TkFixedFont")
        self.Entry_2.configure(foreground="#000000")
        self.Entry_2.configure(insertbackground="black")
        self.Entry_2.configure(width=184)

        self.Entry_3 = tk.Entry(top)
        self.Entry_3.place(relx=0.31, rely=0.5, height=20, relwidth=0.55)
        self.Entry_3.configure(background="white")
        self.Entry_3.configure(disabledforeground="#a3a3a3")
        self.Entry_3.configure(font="TkFixedFont")
        self.Entry_3.configure(foreground="#000000")
        self.Entry_3.configure(insertbackground="black")
        self.Entry_3.configure(width=184)

        self.predict_btn = tk.Button(top)
        self.predict_btn.place(relx=0.09, rely=0.7, height=24, width=80)
        self.predict_btn.configure(activebackground="#ececec")
        self.predict_btn.configure(activeforeground="#000000")
        self.predict_btn.configure(background="#d9d9d9")
        self.predict_btn.configure(disabledforeground="#a3a3a3")
        self.predict_btn.configure(foreground="#000000")
        self.predict_btn.configure(highlightbackground="#d9d9d9")
        self.predict_btn.configure(highlightcolor="black")
        self.predict_btn.configure(pady="0")
        self.predict_btn.configure(text='''Predict''')
        self.predict_btn.bind('<Button-1>', lambda e: gui_support.predict())

        self.prediction_btn = tk.Button(top)
        self.prediction_btn.place(relx=0.25, rely=0.7, height=24, width=80)
        self.prediction_btn.configure(activebackground="#ececec")
        self.prediction_btn.configure(activeforeground="#000000")
        self.prediction_btn.configure(background="#d9d9d9")
        self.prediction_btn.configure(disabledforeground="#a3a3a3")
        self.prediction_btn.configure(foreground="#000000")
        self.prediction_btn.configure(highlightbackground="#d9d9d9")
        self.prediction_btn.configure(highlightcolor="black")
        self.prediction_btn.configure(pady="0")
        self.prediction_btn.configure(text='''Prediction''')
        self.prediction_btn.bind('<Button-1>', lambda e: gui_support.prediction())

        self.prediction_res_btn = tk.Button(top)
        self.prediction_res_btn.place(relx=0.41, rely=0.7, height=22, width=80)
        self.prediction_res_btn.configure(activebackground="#ececec")
        self.prediction_res_btn.configure(activeforeground="#000000")
        self.prediction_res_btn.configure(background="#d9d9d9")
        self.prediction_res_btn.configure(disabledforeground="#a3a3a3")
        self.prediction_res_btn.configure(foreground="#000000")
        self.prediction_res_btn.configure(highlightbackground="#d9d9d9")
        self.prediction_res_btn.configure(highlightcolor="black")
        self.prediction_res_btn.configure(pady="0")
        self.prediction_res_btn.configure(text='''Show Result''')
        self.prediction_res_btn.bind('<Button-1>', lambda e: gui_support.show_res())

        self.save_btn = tk.Button(top)
        self.save_btn.place(relx=0.57, rely=0.7, height=22, width=80)
        self.save_btn.configure(activebackground="#ececec")
        self.save_btn.configure(activeforeground="#000000")
        self.save_btn.configure(background="#d9d9d9")
        self.save_btn.configure(disabledforeground="#a3a3a3")
        self.save_btn.configure(foreground="#000000")
        self.save_btn.configure(highlightbackground="#d9d9d9")
        self.save_btn.configure(highlightcolor="black")
        self.save_btn.configure(pady="0")
        self.save_btn.configure(text='''Save''')
        self.save_btn.bind('<Button-1>', lambda e: gui_support.save_res())

        self.resert_btn = tk.Button(top)
        self.resert_btn.place(relx=0.8, rely=0.7, height=22, width=80)
        self.resert_btn.configure(activebackground="#ececec")
        self.resert_btn.configure(activeforeground="#000000")
        self.resert_btn.configure(background="#d9d9d9")
        self.resert_btn.configure(disabledforeground="#a3a3a3")
        self.resert_btn.configure(foreground="#000000")
        self.resert_btn.configure(highlightbackground="#d9d9d9")
        self.resert_btn.configure(highlightcolor="black")
        self.resert_btn.configure(pady="0")
        self.resert_btn.configure(text='''Reset''')
        self.resert_btn.bind('<Button-1>', lambda e: gui_support.rest())


if __name__ == '__main__':
    vp_start_gui()





