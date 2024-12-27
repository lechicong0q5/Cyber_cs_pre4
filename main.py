def  add_two_number(number_1, number_2):
    return number_1 + number_2

if __name__ == "__main__":
    print(add_two_number(3,5))
    
    
    


#tạo biến, biến có thể đặt tiếng việt ht hoặc tiếng anh hết
#đặt tên theo kiểu snake case


#in biến/ lệnh xuất
# print(2)
# print("abc")
# print(ho_ten)

#cách tạo ghi chú banh crtl + /

#lệnh nhập



#kiểu dữ liệu: 
# str string
# int interger
# float: số thập phân
# bool : boolean true/false




    
# print("bạn này có trên 18 không: ", is_order_than_18)


#hàm

def in_hoten ():
   ho_ten = "duy" 

def kiem_tra_tuoi (num): 
    is_order_than_18 = True
    if num > 18: 
        is_order_than_18 = True
    else: is_order_than_18 = False
    return is_order_than_18

# in_hoten()

tuoi = int(input("nhập vào tuổi của bạn "))
print("bạn có trên 18 tuổi không: ", kiem_tra_tuoi(tuoi))

#phạm vi của biến, scope

x=10

def change_x(x): 
    x = 20
    print("x: ", x)
    
change_x(x)
    
#vòng lặp

#for/while

#đặt 1 biến để xác định dừng vòng lặp

#range(a,b) a là giá trị bắt đầu, b-1 là giá trị kết thúc, 1 -> 9
#range(a, b, c) a và b như trên, c là step giữa các giá trị, a+ c
for i in range(1, 10):
    print(i)
    
#while tạo giá trị boolean, phải có dòng lệnh thay đổi giá trị kết thúc vòng lặp

while i < 10:
    print(i)
    i += 1


# cấu trúc dữ liệu: set, turples, list, dictionary

# set
''' 
Đặc điểm của Set: 
1. Không được sắp xếp -> mình không thể lấy giá trị của phần tử theo index
2. Không chứa dữ liệu trùng lặp

'''

my_set = {1, 1, 1, 2, 3, 4, 5, 6}
print(my_set)
print("Chiều dài set:", len(my_set))




''' 
Đặc điểm của Tuples: 
1. Khai báo: {}
2. Không được sắp xếp -> mình có thể lấy giá trị của phần tử theo index
3. Không thay đổi (tương tác) được với phần tử trong tuples
4. Chứa được dữ liệu trùng lặp
'''


my_tuples = (100,200,300,400)
print(my_tuples)


'''
Đặc điểm của list:
1. Khai báo: []
2. Có thể được sắp xếp -> lấy giá trị của phần tử theo index
3. Tương tác được với phần tử trong list: thêm, xoá, sửa = CRUD
4. Chứa được dữ liệu trùng lặp
'''



# my_list = [1, 1, 1, 2, 3, 4, 5, 6]
# print(my_list)
# print("Chiều dài list:", len(my_list))



# my_list.pop() # Xoá giá trị cuối cùng (k có tham số), có tham số -> xoá theo index
# my_list.remove(2) # Remove: xoá hết giá trị truyền vào hàm remove mặt định nếu không có giá trị truyền vào

# my_list.sort() # Sắp xếp các giá trị tăng dần (mặc định) -> [2, 4, 5, 6, 6, 9]

# print("List được xoá: ", my_list)

# # my_list.remove()

# print("Chiều dài list:", len(my_list))

# for item in my_list:
#     print(item)


'''
Đặc điểm của dictionary = object / JSON:
1. Khai báo: {}, chứa các phần tử là 1 cặp key (bắt buộc là chuỗi) - value (kiểu dữ liệu nào cũng được)
2. Lấy gía trị (my_dict.values()), lấy key (my_dict.keys()), lấy cả 2 (my_dict.items())
3. Tương tác được với phần tử trong list: thêm, xoá, sửa = CRUD
4. Không được chứa key trùng lặp, giá trị của từng key thì không ảnh hướng
5. Không sắp xếp được
'''
my_dict = {
    "name": "Nguyen Duy", 
    "age": 18,
    "phone": 123456
}

my_keys = my_dict.keys().sort() # ["name", "age", ...]
print("Keys: ", my_keys)

my_values = my_dict.values().sort() # ["Nguyen Duy", 18, ...]
print("Values: ", my_values)

# for key, value in my_dict.items():
#     print(key, value)
    
# my_dict["job"] = "Giang Vien"

# print("Dictionary được thêm: ", my_dict)

# my_dict["age"] = 20

# print("Dictionary được cập nhật: ", my_dict)

a = [1, 2, 3, 4, 5, 6] 
b = a # b = [1, 2, 3, 4, 5, 6]

a.append(7) # a = [1, 2, 3, 4, 5, 6, 7]

print("a:", a)
print("b:", b)




