class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


#THIS IS THE CLASS INHERITANCE
class Fish(Animal):
    def __init__(self):
        super().__init__()
        #BY DEFINING THIS SUPER CLASS, YOU WILL INHERIT ALL THE METHODS IN THE PARENT CLASS

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")



nemo = Fish()
nemo.breathe()

#OUTPUT:
'''
Inhale, exhale.
doing this underwater.
'''