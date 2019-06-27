# The modol of the GUI
# That class control the logic of the GUI and is association with the system
# The function in this class are the "on action" function of any button of the gui
import model
from tkinter import filedialog, messagebox
from tkinter.messagebox import showinfo, showwarning


train_model = ""
res = []

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


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top


def upload_model():
    global w

    model_path = filedialog.askopenfilename(title="Choose model file")
    w.Entry_1.delete(0, 'end')
    w.Entry_1.insert(0, model_path)


def load_flower_dir():
    global w

    flower_dir = filedialog.askdirectory(title="Choose flower image directory")
    w.Entry_2.delete(0, 'end')
    w.Entry_2.insert(0, flower_dir)


def dest_path():
    global w

    dest_dir = filedialog.askdirectory(title="Choose directory for save csv")
    w.Entry_3.delete(0, 'end')
    w.Entry_3.insert(0, dest_dir)


def predict():
    global w
    global train_model

    path = w.Entry_1.get()
    if path != "":
        train_model = model.load_model(path)
        showinfo("Info", "Model uploaded successfully")
    else:
        showwarning("Warning", "No path has been inserted to load the model")


def prediction():
    global w
    global train_model
    global res

    if train_model != "":
        path = w.Entry_2.get()
        if path != "":
            res = model.predict_image(train_model, path)
            showinfo("Info", "The prediction process has ended")
        else:
            showwarning("Warning", "No path insert")
    else:
        showwarning("Warning", "No model load")


def show_res():
    global w
    global res

    if len(res) != 0:
        toplevel = tk.Toplevel()
        toplevel.title("Flower Prediction")
        toplevel.geometry('600x210')
        toplevel.resizable(False, False)
        scrollbar = tk.Scrollbar(toplevel)
        scrollbar.pack(side='right', fill='y')
        treeview = ttk.Treeview(toplevel, yscrollcommand=scrollbar.set, show="tree")
        treeview.place(height=600, width=200)
        treeview['show'] = 'headings'
        treeview['columns'] = ('Image Name', 'Prediction')
        treeview.column('Image Name', anchor=tk.CENTER)
        treeview.column('Prediction', anchor=tk.CENTER)
        treeview.tag_configure('oddrow', background='orange')
        treeview.tag_configure('evenrow', background='purple')
        treeview.heading('Image Name', text='Image Name')
        treeview.heading('Prediction', text='Prediction')
        treeview.pack(fill='x')

        scrollbar.config(command=treeview.yview())
        index = 1
        for x in res:
            if index == 1:
                treeview.insert('', 'end', text='Term', tags=('oddrow',), values=(str(x[0]), str(x[1])))
                index = 0
            else:
                treeview.insert('', 'end', text='Term', tags=('evenrow',), values=(str(x[0]), str(x[1])))
                index = 1
    else:
        showwarning("Warning", "No result")


def save_res():
    global w
    global res

    if len(res) != 0:
        path = w.Entry_3.get()
        if path != "":
            model.save_to_csv(res, path)
            showinfo("Info", "The file flower predictions.csv is saved")
        else:
            showwarning("Warning", "No path insert")
    else:
        showwarning("Warning", "No result")


def rest():
    global w
    global train_model
    global res

    if messagebox.askyesno("Question", "Are you sure you want to delete the selected fields and model?"):
        train_model = ""
        res = []
        w.Entry_1.delete(0, 'end')
        w.Entry_2.delete(0, 'end')
        w.Entry_3.delete(0, 'end')

def destroy_window():
    # Function which closes the window.
    global top_level
    global in_process

    if not in_process:
        top_level.destroy()
        top_level = None


if __name__ == '__main__':
    import gui
    gui.vp_start_gui()
