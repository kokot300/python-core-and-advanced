import pickle
import filespicklestudent

f=open("student.dat","ab")
st=filespicklestudent.Student(12,"john",7.5)
pickle.dump(st,f)
f.close()

f=open("student.txt","a")
st=filespicklestudent.Student(12,"john",7.5)
#pickle.dump(st,f) #not possible
#f.write(st) #not possible
f.close()

f=open("student.dat","rb")
ff=pickle.load(f)
ff.disp()

f=open("student.txt","r")
#ff=pickle.load(f) #pickle is only for binaries :(
ff.disp()