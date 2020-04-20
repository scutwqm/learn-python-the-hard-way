# _*_ coding:utf-8- _*_
import os

for i in range(1,53):
    file_name = "exercise-%s"%i
    f_py_name = "ex%s.py"%i
    print("Try: make a folder named " + file_name)
    try:
        os.mkdir(file_name)
        print("Success: " + file_name)
        
    except:
        print("Fail: " + file_name)
for i in range(1,53):
    file_name = "exercise-%s"%i
    f_py_name = "ex%s.py"%i   
    try:
            file_path = os.path.join(file_name, f_py_name)
            print("making " + file_path)
            with open(file_path, 'a') as f:
                f.write("# _*_ coding:utf-8- _*_" + '\n')
                
            #os.mknod(file_path)
            print("Success: " + f_py_name)
    except:
            print("Fail: " + f_py_name)
a = input("Please input anything to exit...")