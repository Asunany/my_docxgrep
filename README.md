# 名称
项目名称：my_wordgrep  

1.基于他人的代码，做了一点改进。  
2.实现对docx格式的批量文档内容的搜索，并标红

# 用法
python my_wordgrep.py  -f *.docx -w 'hello'

# 编译

项目目录结构和setup.py文件都就绪之后，就可以开始编译并打包了；首先最好升级下打包相关的基础库。  

python -m pip install --upgrade pip  
pip install --upgrade setuptools wheel  

接着，从命令行进入项目的根目录，通过如下命令即可进行编译打包操作：  

python setup.py sdist       # 打源码包  
python setup.py bdist       # 打二进制包  
python setup.py bdist_egg       # 打egg包  
python setup.py bdist_wheel     # 打wheel包  

# 本地测试
在打包后，可以本地进行安装和使用测试，也可以通过如下命令直接安装：  

python setup.py build  
python setup.py install  

# 参考
https://blog.51cto.com/u_15918230/5954850  
https://zhuanlan.zhihu.com/p/276461821  
https://blog.csdn.net/weixin_44343319/article/details/126208516  
https://www.jianshu.com/p/9fb0d69134d2  
https://blog.csdn.net/u014163312/article/details/117934339  
