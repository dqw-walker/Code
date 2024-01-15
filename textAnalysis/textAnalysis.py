import jieba
import os
# 读取关键词
with open('wordKey.txt', 'r', encoding='utf-8') as f:
    keywords = f.read().splitlines()
    # 将关键词添加到jieba的词库中
for keyword in keywords:
    jieba.add_word(keyword)
    # 创建一个字典来存储关键词的频率
    keyword_frequency = {keyword: 0 for keyword in keywords}

    # 遍历annualReport目录下的所有txt文件
for filename in os.listdir('年报txt'):
    if filename.endswith('.txt'):
        # 读取文件
        with open(os.path.join('年报txt', filename), 'r', encoding='utf-8') as f:
            text = f.read()
        # 对文本进行分词
        words = jieba.cut(text)

        # 遍历分词结果，如果词在关键词列表中，就在字典中增加这个词的计数
        for word in words:
            if word in keyword_frequency:
                keyword_frequency[word] += 1

# 打印出关键词及其在文本中出现的频率
for keyword, frequency in keyword_frequency.items():
    print(f'{keyword}: {frequency}')

    #得到以下结果
    # 社会责任: 39
    # 可持续发展: 14
    # 环境友好: 0
    # 经济利益: 226
    # 长效发展: 0
    # 企业治理: 0
    # 利益共享: 0
    # 动态管理: 0
    # 商业模式: 74
    # 混合组织: 0



