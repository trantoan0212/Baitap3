def get_sum(*num): 
    tmp = 0
    for i in num:
        tmp+=i
    return tmp
result = get_sum(1,2,3,4,5)
print(result)

'''Ta gọi hàm get_sum với nhiều tham số là *num(tham số tùy biến),
*num trở thành một tuple trước khi truyền vào hàm get_sum. Bên trong
hàm, sử dụng vong lặp for để lấy tất cả các tham số trong tuple'''

