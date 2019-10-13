基于flask的web后台简易框架\
使用了sqlalchemy、redis、restful等模块或功能\
使用方法：\
pip install -r requirements.txt\
python index.py [dev|sit|uat|prod]

20190922\
1、重写了restful的Resouce类和sqlalchemy的Model类，对rest接口和数据库的基本操作方法以及错误处理\
2、提供了入参校验、request参数获取处理等方法

20191006\
抱歉国庆出去旅游了\
1、完成应用相关接口的调试\
2、修复了字符串长度检测的布尔值替换bug


20191007\
1、角色id转换为角色名称

20191007\
1、新增了环境、平台的文件及接口

20191013\
1、完成环境、平台、接口的调试\
2、为接口查询增加redis缓存以及初始化方案\

待办：\
1、输出接口swagger文档\
2、增加api调用统计功能\
3、提供api信息查询接口，只读取redis数据\


正在完善过程中，后续会继续补充

