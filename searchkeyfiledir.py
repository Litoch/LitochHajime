# 输入关键字，列出指定文件夹中的所有文件名中含有此关键字的文件/目录，
# 以及文件内容中含有此关键字的文件。
# 建议使用 os 模块的 listdir 方法获取指定目录下的所有文件
# 主要涉及内容：文件路径、输入输出、字符串匹配

import os

# # walk使用方法
# import os
# for root, dirs, files in os.walk(".", topdown=False):
#     for name in files:
#         print(os.path.join(root, name))
#     for name in dirs:
#         print(os.path.join(root, name))

def findfile(key, inputdir='.'):
    found_list = []
    all_files = os.listdir(inputdir)
    for name in all_files:
        file_path = inputdir + '/' + name
        if key in name:
            found_list.append(file_path)
        else:   # 排除非文本文件
            try:
                with open(file_path) as f:
                    for l in f:     # 相当于for l in f.readlines()
                        if key in l:
                            found_list.append(file_path + ':' + l.strip())
                            break
            except:
                pass
    return  found_list

keyword = input('Please enter the keyword: ')
path = input('Please enter the directory: ')
if not path.strip():    # 如果没有有效字符
    path = '.'

result = findfile(keyword, path)

print('---------------- result ----------------')
for r in result:
    print(r)
