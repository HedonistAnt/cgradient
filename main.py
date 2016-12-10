from sympy import *
def newtons_method(x0, tk, dtk, eps):
    #f1 - производная
    while True:
        x = x0 - (tk.subs(t,x0) / dtk.subs(t,x0))
        print(x)
        if abs(x - x0) < eps:
            return x
        x0 = x

def absdf(df):
    return sqrt((df[0]**2)+df[1]**2)
x1=symbols('x1')
x2=symbols('x2')
print("Function:")
f=eval(input())
print("X01:")
x01=input()
print("X02:")
x02=input()
X1=Matrix([[x01],[x02]])
print("eps:")
eps=float(input())
df=Matrix([[diff(f,x1)],[diff(f,x2)]])
dk=-df.subs([(x1,X1[0]),(x2,X1[1])])
k=0
Xk=X1
dfsubs=df.subs([(x1,X1[0]),(x2,X1[1])])
t=symbols('t')

while absdf(dfsubs)>eps :

    if k%2==0:

        tk=f.subs([(x1,Xk[0]+dk[0]*t),(x2,Xk[1]+dk[1]*t)])

        dtk=diff(tk,t)

        Xk=Xk+newtons_method(0,tk,dtk,0.1)*dk
        Xk[0] = float(Xk[0])
        Xk[1] = float(Xk[1])
        dk = - df.subs([(x1,Xk[0]),(x2,Xk[1])])
    else:

        tk = f.subs([(x1, Xk[0] + dk[0] * t), (x2, Xk[1] + dk[1] * t)])

        dtk = diff(tk, t)
        Xkprev=Xk


        Xk = Xk + newtons_method(0,tk,dtk,0.1)* dk

        Bk=(absdf(Xk)**2)/(absdf(Xkprev)**2)
        dk=-df.subs([(x1,Xk[0]),(x2,Xk[1])])+Bk*dk
    dfsubs = df.subs([(x1, Xk[0]), (x2, Xk[1])])
    print(dfsubs)
    k+=1
print("xmin=",round(float(Xk[0]),2),round(float(Xk[1]),2))









