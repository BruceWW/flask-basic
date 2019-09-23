基于flask的web后台简易框架
使用了sqlalchemy、redis、restful等模块或功能
使用方法：
pip install -r requirements.txt
python index.py dev|sit|uat|prod

20190922
1、重写了restful的Resouce类和sqlalchemy的Model类，对rest接口和数据库的基本操作方法以及错误处理
2、提供了入参校验、request参数获取处理等方法

正在完善过程中，后续会继续补充