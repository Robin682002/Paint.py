from tkinter import *
from tkinter import filedialog, messagebox, colorchooser
from PIL import Image, ImageDraw
import PIL


WIDTH , HEIGHT = 500, 500
CENTER = WIDTH//2
WHITE = (255,255,255)

class PaintGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Paint")

        self.brush_width = 5
        self.color = "#000000"

        self.can = Canvas(self.root, width=WIDTH, height=HEIGHT, bg="white")
        self.can.pack()

        self.can.bind("<B1-Motion>", self.paint)

        self.image = PIL.Image.new("RGB", (WIDTH, HEIGHT), "white")
        self.draw = ImageDraw.Draw(self.image)

        #button frame

        self.btn_frame = Frame(self.root)
        self.btn_frame.pack(fill=X)

        self.btn_frame.columnconfigure(0, weight=1)
        self.btn_frame.columnconfigure(1, weight=1)
        self.btn_frame.columnconfigure(2, weight=1)

        self.clear_btn = Button(self.btn_frame, text="Clear", command=self.clear)
        self.clear_btn.grid(row=0, column=1, sticky=W+E)

        self.save_btn = Button(self.btn_frame, text="Save", command=self.save)
        self.save_btn.grid(row=1, column=2, sticky=W+E)

        self.bplus_btn = Button(self.btn_frame, text="B+", command=self.brush_plus)
        self.bplus_btn.grid(row=0, column=0, sticky=W+E)

        self.bminus_btn = Button(self.btn_frame, text="B-", command=self.brush_minus)
        self.bminus_btn.grid(row=1, column=0, sticky=W+E)

        self.color_btn = Button(self.btn_frame, text="Change Color", command=self.color_change)
        self.color_btn.grid(row=1, column=1, sticky=W+E)



        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.attributes("-fullscreen", True)
        self.root.mainloop()

    def paint(self, event ):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        self.can.create_rectangle(x1, y1, x2, y2, fill=self.color, outline=self.color, width=self.brush_width)
        self.draw.rectangle([x1, y1, x2 + self.brush_width, y2 + self.brush_width], fill=self.color)

        

    def clear(self):
        self.can.delete("all")
        self.draw.rectangle([0,0,1000,1000], fill="white")
    def save(self):
        
        file_name = filedialog.asksaveasfilename(initialfile = "untiled.png", defaultextension= ".png" , filetypes=[("PNG", ".png"), ("JPG", ".jpg")])
        if file_name:
            self.image.save(file_name)
        else:
            messagebox.showerror("Error", "Invalid file name")
        
        
    def brush_plus(self):
        self.brush_width += 1

    def brush_minus(self):
        if self.brush_width > 1:
            self.brush_width -= 1
    def color_change(self):
        self.color = colorchooser.askcolor(title="Choose color")[1]
        self.color = "#%02x%02x%02x" % (self.color[0], self.color[1], self.color[2])
        self.color_btn.config(bg=self.color)
        self.color_btn.config(fg=self.color)
        self.color_btn.config(activebackground=self.color)
        
        


    def on_closing(self):
        answer = messagebox.askyesno("Quit", "Do you want to save?", parent = self.root)
        if answer is not None:
            if answer:
                self.save()
            self.root.destroy()
            exit(0)
        else:
            self.root.destroy()
            exit(0)
        
    
        


PaintGUI()