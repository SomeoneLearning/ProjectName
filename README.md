# ProjectName

这是一个示例项目，主要是为了设计个人编码的风格与规范。

This is a sample project，which is mainly designed for personal coding style and standard.

## 项目结构

```
ProjectName
├── README.md
├── requirements.txt
├── data
│   ├── raw_data
│   ├── processed_data
│   └── ...
├── results
│   ├── figures
│   └── ...
├── settings
│   ├── config.json
│   ├── config.ini
│   ├── config.yaml
│   └── ...
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── module1.py
│   ├── module2.py
│   └── ...
└── tests
    ├── __init__.py
    ├── test_module1.py
    ├── test_module2.py
    └── ...
```

- `README.md`：项目说明文档，一般包括项目背景、项目结构、项目功能、项目使用方法等。
- `requirements.txt`：项目依赖的第三方库列表，一般包括项目运行所需的第三方库。
- `data`：项目数据目录，一般包括原始数据、经过处理的数据等。
- `settings`：项目配置目录，一般包括项目运行所需的配置文件。
- `results`：项目结果目录，一般包括项目运行结果的图表等。
- `src`：项目源码目录，一般包括项目主要功能的实现代码。
- `tests`：项目测试目录，一般包括项目主要功能的测试代码。

## 编码规范

- 代码风格：遵循 PEP8 规范，使用 4 个空格缩进，每行不超过 79 个字符。
- 命名规范：见下文。
- 注释规范：见下文。
- 文档规范：见下文。

### 命名规范

- 变量名：小写，单词之间用下划线连接。
- 类名：驼峰命名法，首字母大写。
- 函数名：驼峰命名法，首字母小写。
- 常量名：全部大写，单词之间用下划线连接。

### 注释规范

- 注释内容：使用英文，简明扼要，尽量避免使用过多注释。
- 注释位置：代码上方，与代码同一行；代码下方，与代码同一行；代码中间，单独一行。
- 注释格式：单行注释以 `#` 开头，多行注释以 `"""` 开头和 `"""` 结尾。

### 文档规范

- 文档内容：使用英文，简明扼要，尽量避免使用过多文档。
- 文档位置：代码上方，与代码同一行；代码下方，与代码同一行；代码中间，单独一行。
- 文档格式：单行文档以 `#` 开头，多行文档以 `"""` 开头和 `"""` 结尾。

## 虚拟环境

推荐使用 `virtualenv` 或 `venv` 来创建虚拟环境。
https://blog.csdn.net/m0_73550224/article/details/135662877

```
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
venv\Scripts\activate

# Python中pip的升级命令时单独的，更新pip版本
python -m pip install --upgrade pip==24.0
python -m pip install --upgrade pip==23.3.2

# 退出虚拟环境
deactivate
```

## 运行方式

```
# 安装依赖
pip install -r requirements.txt

单个包示例
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ --upgrade Django==4.2.13
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ --upgrade xgboost==1.7.6

多个包示例
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ -r requirements.txt

# 运行项目
python src/main.py
```

## 其他说明

- 项目中使用到的第三方库，请在 `requirements.txt` 中添加。
- 项目中使用的数据，请在 `data` 目录下添加。
- 项目中使用到的结果，请在 `results` 目录下添加。
- 项目中使用到的配置文件，请在 `settings` 目录下添加。
- 项目中使用到的测试代码，请在 `tests` 目录下添加。
