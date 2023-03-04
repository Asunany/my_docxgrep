# Text extraction from Word(docx) files
import pdb
import argparse
from docx import Document
import sys
import argparse
import os
import re



def wordgrep(path, search_word):
    lis = []
    document = Document(path)
    # 1パラグラフごとに配列に入れる
    for i, p in enumerate(document.paragraphs):
        i_text = str(i) + ' : ' + p.text
        lis.append(i_text)
    # 検索条件
    pattern =  search_word 
    # pattern = ".*" + search_word + ".*"

    # Match the above pattern using list comprehension
    # filtered_lis = [x for x in lis if re.match(pattern, x)]

    color_begin = '\033[1;31;40m'
    color_end = '\033[0m'
    # print(lis)
  
    filtered_lis = []
    for x in lis:
        if re.search(pattern, x, re.IGNORECASE):
            find_res = re.search(pattern, x, re.IGNORECASE)
            # print(find_res.span())
            start_ = find_res.span()[0]
            end_ = find_res.span()[1]
            # print('find_target: ',x[start_:end_])
            # pdb.set_trace()
            # 对于找到的关键词添加颜色，print()的时候就可以再bash终端展示
            x = x[0:start_] + color_begin + x[start_:end_] + color_end + x[end_:] 
            # print("x：:",x)
            filtered_lis.append(path +":" + x)
    # filtered_lis = [path +" line: " + red + x + end for x in lis if re.fullmatch(pattern, x, re.IGNORECASE)]

    # 結果
    # print(filtered_lis)
    # pdb.set_trace() 
    print('\n'.join(filtered_lis))


# コマンドライン引数を処理する
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Text extraction from Word(docx) files")
    parser.add_argument('-f','--files',nargs='+',help='docx files')
    parser.add_argument('-w','--word',type=str,help='search word(Regular expression enabled)',required=True)

    args = parser.parse_args()
    file_paths = args.files
    # pdb.set_trace()
    # 字符串判定，去除~开头的缓存文件
    file_paths = [x for x in file_paths if not x.startswith("~")]

    # print("file_paths:",file_paths)
    if not file_paths:
        sys.exit('Arguments are too short')
    else:
        for file_path in file_paths:
            # 絶対パスへ変換
            path = os.path.abspath(file_path)
            # print("path:",path)
            # ファイルの存在有無
            if not os.path.isfile(path):
                sys.exit("I don't have that file.")
            # .docxを想定している場合
            if path.split(".")[-1] != "docx":
                sys.exit("That's not the right extension!!!")
            search_word = args.word
            wordgrep(path, search_word)
