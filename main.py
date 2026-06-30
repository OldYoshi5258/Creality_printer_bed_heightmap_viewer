import tkinter
import tkinter.ttk as ttk
import matplotlib.pyplot as plt

class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title = "Printer bed heightmap viewer"

        # This is the model
        self.heightmap = [[0.0 for i in range(5)] for j in range(5)]

        # This is the view

        ## Making the entry boxes
        self.entries = []
        for x in range(5):
            row = []
            for y in range(5):
                row.append(ttk.Entry(self))
                row[-1].insert(0,"0")
                row[-1].bind('<Return>', lambda event, i=x, j=y: [self.setbox(i,j)])
                row[-1].grid(column=y, row=x)
            self.entries.append(row)

        ## Making the plot button
        self.confirm = ttk.Button(self, text="Plot", command=self.plotgraph)

        self.confirm.grid(column=0, row=6, columnspan=5)

    def setbox(self, i, j):
        try:
            self.heightmap[i][j] = float(self.entries[i][j].get())
        except ValueError:
            self.entries[i][j].delete(0, tkinter.END)
            self.entries[i][j].insert(0,"Error")
            self.heightmap[i][j] = 0.0

        print(self.heightmap)

    def plotgraph(self):
        for i in range(5):
            for j in range(5):
                try:
                    self.heightmap[i][j] = float(self.entries[i][j].get())
                except ValueError:
                    self.entries[i][j].delete(0, tkinter.END)
                    self.entries[i][j].insert(0,"Error")
                    self.heightmap[i][j] = 0.0
        self.make_plot(self.heightmap)

    def make_plot(self, data: list[list[float]]):
        front = [i for i in range(5)]
        side = [i for i in range(5)]

        # Creating a 3D plot
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Plotting 3D bars
        for i in range(len(front)):
            for j in range(len(side)):
                ax.bar3d(i, j, 0, 0.8, 0.8, data[i][j])

        ax.set_xlabel('Side')
        ax.set_ylabel('Front')
        ax.set_zlabel('Height')
        ax.set_title('Printer Bed Heightmap')

        # Displaying the plot
        plt.show()

if __name__ == "__main__":
    root = App()
    root.mainloop()