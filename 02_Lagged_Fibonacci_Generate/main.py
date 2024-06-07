import pandas as pd

#读取question1中生成的随机数文件
file_path = r"C:\Users\86130\Desktop\Computational Physics\hw1\question1\output.csv"
df = pd.read_csv(file_path ,usecols=[1])

#将随机数储存到一个列表中
data_list = df.iloc[:, 0].tolist()

#如果有满足要求的，num加1
num = 0
print("16807产生器:")
for i in range(1,9999999):
    if (data_list[i-1]>data_list[i+1]) & (data_list[i+1]>data_list[i]):
        num+=1
    if i==999:
        print(f"在N=10^3+1时，满足此关系的n有{num}个，比重为{num / 1000}")
    if i==9999:
        print(f"在N=10^4+1时，满足此关系的n有{num}个，比重为{num / 10000}")
    if i==99999:
        print(f"在N=10^5+1时，满足此关系的n有{num}个，比重为{num / 100000}")
    if i==999999:
        print(f"在N=10^6+1时，满足此关系的n有{num}个，比重为{num / 1000000}")
print(f"在N=10^7+1时，满足此关系的n有{num}个，比重为{num/10000000}")

#讨论Fibonacci延迟产生器
#利用question1中得到前43个I
file_path2 = r"C:\Users\86130\Desktop\Computational Physics\hw1\question1\I.csv"
df2 = pd.read_csv(file_path2 ,usecols=[1])

m = 2147483647
I = df2.iloc[:, 0].tolist()
X = []     #储存随机数

for n in range(43,10000044):
    I.append(I[n-22] - I[n-43])
    if I[n]<0:
        I[n] = I[n] + (4294967296 - 5) -1
    X.append(I[n-42]/m)

num = 0
print("Fibonacci产生器")
for i in range(0,10000000):
    if (X[i-1]>X[i+1]) & (X[i+1]>X[i]):
        num+=1
    if i==1000:
        print(f"在N=10^3+1时，满足此关系的n有{num}个，比重为{num / 1000}")
    if i==10000:
        print(f"在N=10^4+1时，满足此关系的n有{num}个，比重为{num / 10000}")
    if i==100000:
        print(f"在N=10^5+1时，满足此关系的n有{num}个，比重为{num / 100000}")
    if i==1000000:
        print(f"在N=10^6+1时，满足此关系的n有{num}个，比重为{num / 1000000}")
print(f"在N=10^7+1时，满足此关系的n有{num}个，比重为{num/10000000}")