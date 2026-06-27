import matplotlib.pyplot as plt 

class charts:
    def __init__(self,x , y ):
        self.x = x
        self.y = y
        
    def showchartviaCategory(self):
        plt.plot(self.x , self.y,marker=".",markersize=20,makerfacecolor= "red")
        plt.show()
    