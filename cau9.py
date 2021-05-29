def cong(x,y):
    return x+y
def tru(x,y):
    return x-y
def nhan(x,y):
    return x*y
def chia(x,y):
    return x/y
print("Lựa chọn các phép tính")
print("1.Cộng")
print("2.Trừ")
print("3.Nhân")
print("4.Chia")

choice = input("Nhập phép tính(1/2/3/4):")
num1 = int(input("Số thứ nhất: "))
num2 = int(input("Số thứ 2: "))
if choice == '1':
    print(num1,"+",num2,"=",cong(num1,num2))
elif choice == '2':
    print(num1,"-",num2,"=",tru(num1,num2))
elif choice == '3':
    print(num1,"*",num2,"=",nhan(num1,num2))
elif choice == '4':
    print(num1,"/",num2,"=",chia(num1,num2))
else:
    print("đầu vào không hợp lệ")
