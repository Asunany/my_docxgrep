#!/usr/bin/env python
# coding=utf-8
from setuptools import setup, find_packages

setup(
    name="wordgrep",
    version="0.1.1",
    keywords=("test report", "python unit testing"),
    description="The HTML Report for Python unit testing Base on HTMLTestRunner",
    long_description="The HTML Report for Python unit testing Base on HTMLTestRunner",
    license="MIT",
    author="xxx",
    author_email="xxx@163.com",
    package_dir={'myGrep':'myGrep'},         # 指定哪些包的文件被映射到哪个源码包
    packages=['myGrep'],       # 需要打包的目录。如果多个的话，可以使用find_packages()自动发现
  
    # https://zhuanlan.zhihu.com/p/276461821
    # 用来支持自动生成脚本，安装后会自动生成 /usr/bin/my_wordgrep 的可执行文件
    # 该文件入口指向 myGrep/my_wordgrep.py的main 函数
    entry_points={
        'console_scripts': [
            'my_wordgrep = myGrep.my_wordgrep:main'
        ]
    },
    include_package_data=True,
    py_modules=[],          # 需要打包的python文件列表
    platforms="any",
    # scripts=['/usr/bin/my_wordGrep.sh', 'my_wordGrep.py'],             # 安装时复制到PATH路径的脚本文件
    classifiers=[           # 程序的所属分类列表
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False
)
