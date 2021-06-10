#输入一条字符串，输出首字母
# 用户数入字符串
str = input("Convert to A CRONYM :")
#所有字符串分离
str = str.upper()
#将字符串放入一个列表
listOfWards = str.split()
#一个一个单词的访问
for word in listOfWards:
#索引
    print(word[0],end = "")


orig_message = input("Enter a string in uppercase:")

secret_message = ''#初始值为空
for char in orig_message:
    secret_message += str(ord(char))
print("Scert message: ", secret_message)
norm_string = ""
for i in range(0,len(secret_message)-1,2):
    char_code = secret_message[i] + secret_message[i+1]
    norm_string +=chr(int(char_code))





