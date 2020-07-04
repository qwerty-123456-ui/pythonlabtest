class InvalidException(Exception):
    def __init__(self,value):
        self.value=value
    def __str__(self):
      return(repr(self.value))
    
r=input("Enter radius : ")
try:
    if(not r.isnumeric()):
        raise (InvalidException(r))
    rad=int(r)
    print("Area = ",3.14*rad*rad)
    
except  InvalidException as ex:
    print("Invalid radius ", ex.value)