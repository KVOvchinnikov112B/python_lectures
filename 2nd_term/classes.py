import random

class matrix:
 
    def __init__(self, h, w):
        self.w = w    # ширина
        self.h = h    # высота
 
    def create(self):
        self.A = []
        for i in range(self.h*self.w):
            self.A.append( [round((random.random()),1),round((random.random()),1),round((random.random()),1)] )

    def write(self):
        for i in range(1,self.h*self.w+1):
            print (self.A[i-1], end=' ')
            if ((i) % self.w == 0):
                print('')

    def grayscale(self):
        self.B = []
        for i in range(self.h*self.w):
            self.B.append( round(sum(self.A[i])/len(self.A[i]),1) )

    def grayscale_print(self):
        for i in range(1,self.h*self.w+1):
            print (self.B[i-1], end=' ')
            if ((i) % self.w == 0):
                print('')

    def negative(self):
         self.C = []
         for i in range(self.h*self.w):
             self.C.append( (round(1-self.A[i][0],1),round(1-self.A[i][1],1),round(1-self.A[i][2],1))  )

    def negative_print(self):
         for i in range(1,self.h*self.w+1):
            print (self.C[i-1], end=' ')
            if ((i) % self.w == 0):
                print('') 
 
tom = matrix(12, 4)
tom.create()
tom.write()
print(' ')
tom.grayscale()
tom.negative()
print(' ')
tom.grayscale_print()
tom.negative_print()
