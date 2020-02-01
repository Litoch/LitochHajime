# 读取屏蔽词文件
def load_blocked():
    with open('words.txt') as f:
        global blocked_words  # 使用全局变量记录屏蔽词
        blocked_words = [l.strip() for l in f.readlines() if l]
        # 这里是为了去掉读进来的内容中带有的空格、换行符、空字符等，等同于以下代码
        # blocked_words = []
        # lines = f.readlines()
        # for l in lines:
        #     if l:  # 如果 l 不为空，即去掉空行
        #         l = l.strip()  # 去除字符前后的空格和回车
        #         blocked_words.append(l)

def words_filter(text, symbol='*'):
    for w in blocked_words:
        # 将每个屏蔽词与待检测文字匹配并替换，默认使用‘*’
        # * 的数量等同于屏蔽词的字符数，即 len(w)
        text = text.replace(w, symbol * len(w))
    return text

# 读取屏蔽词
load_blocked()
while True:
    t = input('输入文字(直接回车退出)：\n')
    if not t:  # 如果 t 为空则跳出
        break
    print(words_filter(t))  # 输出替换结果
