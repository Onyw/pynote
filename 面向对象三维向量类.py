class swxl(object):
    def __init__(self,x=0,y=0,z=0):
        self.x=x
        self.y=y
        self.z=z
    "+"
    def add(self,n):
        r=swxl()
        r.x=self.x+n.x
        r.y=self.y+n.y
        r.z=self.z+n.z
        print(r.x,r.y,r.z)
    "-"
    def sub(self,n):
        r=swxl()
        r.x=self.x-n.x
        r.y=self.y-n.y
        r.z=self.z-n.z
        print(r.x,r.y,r.z)
    "*"
    def mul(self,n):
        r=swxl()
        r.x=self.x*n
        r.y=self.y*n
        r.z=self.z*n
        print(r.x,r.y,r.z)
    "/"
    def div(self,n):
        r=swxl()
        r.x=self.x/n
        r.y=self.y/n
        r.z=self.z/n
        print(r.x,r.y,r.z)
a=swxl(2,4,6)
b=swxl(3,6,9)
swxl.add(a,b)
swxl.sub(a,b)
swxl.mul(a,5)
swxl.mul(b,4)
swxl.div(a,2)
swxl.div(b,3)
