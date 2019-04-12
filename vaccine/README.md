# 这是新华网 关于疫苗的爬虫
## 环境
- python 3.5.2
- scrapy 1.5.2
- conda 4.6.11
> 如果碰到 兼容性问题
最好的方式，是通过 conda 安装所需要的环境变量，记得安装之后重启下系统
```
conda install -c conda-forge scrapy
```
## 运行
```
scrapy crawl spiderNews  
```

## 文件目录说明

通过 tree 命令查看目录结构
```
.
├── scrapy.cfg
└── vaccine
    ├── __init__.py
    ├── items.py
    ├── middlewares.py
    ├── pipelines.py
    ├── __pycache__
    │   ├── __init__.cpython-37.pyc
    │   ├── items.cpython-37.pyc
    │   ├── MySQLPipLine.cpython-37.pyc
    │   ├── pipelines.cpython-37.pyc
    │   └── settings.cpython-37.pyc
    ├── README.md
    ├── settings.py
    ├── spiders
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-37.pyc
    │   │   └── VaccineNewsSpider.cpython-37.pyc
    │   └── VaccineNewsSpider.py
    └── vaccine_name.txt
```
- **vaccine_name.txt** ---需要查询的关键字文件

- **VaccineNewsSpider.py** --- 爬虫执行文件

- pipelines.py --- 配置 通道的位置
   ```python
   # 链接数据的配置
   self.connect = pymysql.connect(
            host="127.0.0.1",
            # 数据库地址
            port=3306,
            db="dbcontent",
            user='yusuzi',
            passwd='yusuzi',
            charset='utf8',
            use_unicode=True
        )
   ```