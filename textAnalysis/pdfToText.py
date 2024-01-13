# 提取/年报目录里的PDF信息，并保存为文本
# 提现PDF为文本信息
import sys
import importlib

importlib.reload(sys)
import re

from pdfminer.pdfparser import PDFParser  # 文档分析器
from pdfminer.pdfdocument import PDFDocument  # PDF文档对象存储文档结构
from pdfminer.pdfpage import PDFPage  # 页面
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter  # PDF资源管理器，解释器
from pdfminer.converter import PDFPageAggregator  # PDF设备对象
from pdfminer.layout import LTTextBoxHorizontal, LAParams  # 分析参数
from pdfminer.pdfpage import PDFTextExtractionNotAllowed  # 判断文件是否允许文本提取


# 定义解析函数，提取pdf信息并保存为文本
# 定义解析函数,提取pdf信息并保存为文本
def pdftotxt(pdf_path, txt_path):
    fp = open(pdf_path, 'rb')
    parser = PDFParser(fp)  # 创建一个文档分析器
    document = PDFDocument(parser)  # 创建一个PDF文档对象存储文档结构
    # 判断文件是否允许文本提取
    if not document.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        resmag = PDFResourceManager()  # 创建一个PDF资源管理器对象来存储资源
        laparams = LAParams()  # 设定参数进行分析
        device = PDFPageAggregator(resmag, laparams=laparams)  # 创建一个PDF设备对象
        interpreter = PDFPageInterpreter(resmag, device)  # 创建一个PDF解释器对象
        # 处理每一页
        for page in PDFPage.create_pages(document):
            interpreter.process_page(page)
            # 接受该页面的LTPage对象
            layout = device.get_result()
            text = ''
            for y in layout:
                if (isinstance(y, LTTextBoxHorizontal)):
                    text = text + y.get_text()

            text = text.replace("\n", "")
            for ch in '!"#$%&（）*+,\、-./：；<=>?@[\\]^_‘{|}~':
                text = text.replace(ch, "")  # 将文本中特殊字符替换为空格
            text = re.sub(r'[0-9]+', '', text)
            text = text.replace(" ", "")
            with open(txt_path, 'a', encoding='UTF-8', errors='ignore') as f:
                f.write(text)

    # 主函数


if __name__ == '__main__':
    # 解析./年报  目录里的PDF信息，并保存为文本
    import os

    os.listdir('./年报')

    import time

    for i in os.listdir('./年报'):
        start = time.time()
        pdf_path = './年报' + '/' + i
        txt_path = './年报txt' + '/' + i.split('.')[0] + ".txt"
        pdftotxt(pdf_path, txt_path)
        end = time.time()
        print('pdf_path转换完毕,运行时间:%s 秒' % (end - start))
