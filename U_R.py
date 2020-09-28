I=0
EW = 0
EM = 0
QIYI = []
import copy
def OR(A,B):
    

    QIYI = []
    if len(A)!=0:
        for i in range(len(A)):
            QIYI.append(A[i])
    if len(B)!=0:
        for i in range(len(B)):
            QIYI.append(B[i])
                   
    
    return QIYI
def COMPL(F,J):
    PI = []
    QI = []
    flag = 0
    global I
    global EW,EM
    PS = []
    PS_H1 = []
    PS_H2 = []
    PS_H3 = []
    PS_2=[]
    PS_3=[]
    for i in range(J): # create a list with nested lists
        PI.insert(i,"11")
    if F!=[]:
        for a in range(J):
            if F[0][a]=="11":
                PS_2.append("11")
            elif F[0][a]!="11":
                PS_2.append(0)
    
    PS_2[:]=[item for item in PS_2 if item !="11"]
  
    if len(PS_2)==0:
        return PS
    if len(F)==1:
        
            
        
        if all(elem == "11" for elem in F):
            return QI
        else:
            
            for i in range(J):
                if F[0][i]=="10":
                    flag = flag+1
                    PS_H1.insert(i,i)
                    PS_H2.insert(i,0)
                if F[0][i]=="01":
                    flag = flag+1
                    PS_H2.insert(i,i)
                    PS_H1.insert(i,0)
                if F[0][i]=="11":
                    
                    PS_H3.insert(i,i)
          
            
           
        
            for i in range(flag):
                PS.append([])
                for a in range(J):
                    PS[i].append("11")
            
            if len(PS_H1)>0:
                for i in range(len(PS_H1)):
                    if PS_H1[i]!=0:
                        PS[i][PS_H1[i]]="01"
            
                    
            if len(PS_H2)>0:
                
                for i in range(len(PS_H2)):
                    if PS_H2[i]!=0:
                        PS[i][PS_H2[i]]="10"
                    
            
            
            
     
            return PS
                

            
            

                

                
    else:

        E =SEL(F,J)
        
        P_1_i = copy.deepcopy(F)
        Q_1_i = copy.deepcopy(F)
    
        
        P_2 = COMPL(PCOF(P_1_i,E,J),J)
      
        P_3 = COMPL(NCOF(Q_1_i,E,J),J)
        
        P_2 = AND(P_2,E,J,1)
        P_3 = AND(P_3,E,J,2)        
        return OR(P_2,P_3)
    

        
        
        
def NCOF(Fx_1,X_1,ji_1):
    
   
    li_1 = len(Fx_1)

    del_c=[]
    del_d=[]
    
    for i in range (li_1):
        
        if ((Fx_1[i][X_1])== "11" or (Fx_1[i][X_1])=="10"):
            
            
            

            del_c.insert(i,i)
        else:
            del_c.insert(i,"X")

    
   
   
    for i in range(len(Fx_1)): # create a list with nested lists
        del_d.append([])
        
        for n in range(ji_1):
            del_d[i].append("11")
   
        
    for a in range (len(del_c)):
        if del_c[a]!= "X":
            

            del_d[a]=Fx_1[a]
        elif del_c[a]=="X":
            del_d[a]= "X"
            

   
    for a in range (len(del_c)):
        if del_c[a]!= "X":
            

            del_d[a]=Fx_1[a]
            del_d[a][X_1]="11"
        elif del_c[a]=="X":

            del_d[a]= "X"

           
    del_d[:]=[item for item in del_d if item !="X"]

  
    return(del_d)        
        
def PCOF(Fx,X,ji):
    
    
    li = len(Fx)

    del_a=[]
    del_b=[]
    
    for i in range (li):
        
        if ((Fx[i][X])== "11" or (Fx[i][X])=="01"):         
            
            del_a.insert(i,i)
        else:
            del_a.insert(i,"X")

   
    for i in range(len(Fx)): # create a list with nested lists
        del_b.append([])
        for n in range(ji):
            del_b[i].append("11")
   
       
    for a in range (len(del_a)):
        if del_a[a]!= "X":
            

            del_b[a]=Fx[a]
        elif del_a[a]=="X":
            del_b[a]= "X"
    
    for a in range (len(del_a)):
        if del_a[a]!= "X":
            

            del_b[a]=Fx[a]
            del_b[a][X]="11"
            
        elif del_a[a]=="X":
            del_b[a]= "X"

            
    del_b[:]=[item for item in del_b if item !="X"]
    return(del_b)
def AND(P,x,J,IMP):
    PQ_1 = P.copy()
    
    if IMP == 1:
        
        for i in range(len(PQ_1)):
            PQ_1[i][x]= "01"
    elif IMP==2:
        for i in range(len(PQ_1)):
            PQ_1[i][x]="10"
    return PQ_1
def  SEL(S,JP):
    de = 0
    tc=[]
    un =[]
    bn=[]
    dn=0
    t=0
    P_F = 0
    P_F_1 = 0
    c=0
    dc=0
    dc_1 = 0
    dc_2 = []
    mo = 0
    no = 0
    mo_bn = []
    P_F_2 = []
    for i in range (JP) :  #JP is the number of variables in the cubelist 
    # here we are iterating through each variable in cube list     
        for a in range (len(S)): #this is the for loop so that we iterate the same variable through all the cube list  
            if S[a][i]=="01":
                t=t+1              # this is to find out number of true 
            if S[a][i]=="10":
                
                c=c+1            # this is to find out number of complement
            if S[a][i]=="11":
                dc=dc+1           # this is to find out number of don't care

       
        
            
        if (dc==len(S)):
            P_F_2.insert(i,i)
            mo_bn.insert(i,0)
            un.insert(i,0)
            tc.insert(i,1000000)
        if ((t!=0 and c==0) or (t==0 and c!=0)) :  # check if its unate
            
            if t>c:
                tc.insert(i,100000)
                un.insert(i,t)
                mo_bn.insert(i,0)
                P_F_2.insert(i,10000000)
            elif t<c:
                tc.insert(i,100000)
                un.insert(i,c)
                mo_bn.insert(i,0)
                P_F_2.insert(i,10000000)
            
                    
        
        if t!=0 and c!=0:             # check if its binate
           
            mo_bn.insert(i,t+c)      
            un.insert(i,0)
            P_F_2.insert(i,1000000)
            if t>c:
                
                s = t - c
                tc.insert(i,s)
                
            elif c>t:
                s = c - t
                tc.insert(i,s)
            elif t == c:
                tc.insert(i,t)
          
        t=0
        c=0
        dc=0

    
    
        
    if mo_bn.count(max(mo_bn))>=1 and max(mo_bn)!=0:   # choosing the maximum binate variable 
        
        for i in range(len(tc)):
            if (tc[i]==min(tc) and P_F_2.count(i)==0):  # to findout the variable with minimum t-c
                dn = i                                  # variable which is chosen
                break 
               
        
        urc_v = dn
        
        
        return urc_v          # variable returned
    elif mo_bn.count(0)==JP:  #so if no binate exists check for unate
        for i in range(len(un)):
            if (un[i] == max(un) and P_F_2.count(i)==0):   # checking for the most unate variable and returning it
                P_F_1 = i
                break
 
        
        return(P_F_1)
    
            

with open('part5.pcn','r')as f:
    var= []
    
    z = 0
    
    
    
    ut = 0
    t = 0
    board = []
  
    for i in f:
        
        var.append(i)
        if t == 1:
            break
        t = t+1
        
   
    dt = f.read(1)
    var.insert(2,dt)
    while dt:
        
        
        dt = f.read(1)
        var.append(dt)
        ut =ut+1
    
    
    
    e = len(var)
    
    for i in range(e):
        z = str(var[i])
        y = z.replace("\n","")
        var[i] = y
    while(" " in var ) :
        var.remove(" ")
    while("" in var ) :
        var.remove("")

    
    h = len(var)
    for i in range (h-1):
        if str(var[i])== "0":
            var[i-1]= var[i-1]+"0"
    while("0" in var ) :
        var.remove("0")
    g = len(var)
    
    for i in range (g-1):
        if str(var[i])== "-":
            var[i+1]= "-"+var[i+1]
    while("-" in var ) :
        var.remove("-")
  
    
    j = int(var[0])
    k = int(var[1])
    for i in range(k): # create a list with nested lists
        board.append([])
        for n in range(j):
            board[i].append("11")#this is my dummy pcn which i will then edit according to the function  
   
        
    #this is where we have the whole question deduced from the file now we will create the pcn accordingly
   
    l = 0  
    m = 3  
    o = 2
    c = 0
    d = 0 
    for a in range(k):
        for b in range(int(var[o])):
            p = int (var[m])
           
            if p>0:
                board[c][p-1]="01"
            if p<0:
                p = -1*p
                board[c][p-1]="10"
            m = m+1
        l = int(var[o])+1
        o = o+l  
        m = m+1
        
        d = 0 
        c = c+1
    
    
    PIS = COMPL(board,j)
    PIS_1 = 0
    PIS_2 =[]
    PIS_3 =[]
    QI=open("part5answers_mkc.cubes","w")
    QI.write(str(j))
    QI.write("\n")
    QI.write(str(len(PIS)))
    QI.write("\n")
    for i in range(len(PIS)):
        for a in range(j):
            if PIS[i][a]!="11":
                PIS_1 = PIS_1+1
        QI.write(str(PIS_1)+" ")
        for a in range(j):
            if PIS[i][a]=="10":
                    QI.write("-"+str(a+1)+" ")
                    
            if PIS[i][a]=="01":
                    QI.write(str(a+1)+" ")
        QI.write("\n")
        
        PIS_1 = 0
        
        
        
    QI.close()
    #OR([["11","10"],["11","01"]],[["11","11"],["11","01"]],2)
    
    
    

   
        
    
    
    # now this our pcn from the question which needs to be complemented

    #here i will write the code for the 3 basic direct forms



    #here will be the logic for selection of variable fot URC
