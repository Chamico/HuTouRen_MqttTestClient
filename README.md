一、准备
使用之前，确保自己的mosquitto服务器能正常连接，并且已经配置了密码授权方式。需要确定如下信息：
1、服务器ip
2、moquitto端口号
3、用户名称
4、用户密码

二、使用方式
1、根据自己的服务器配置，手动修改config.json。此文件中有异常注释，不修改无法编译通过。
2、运行subscriber.py。
3、运行publisher.py。
4、能在两个窗口上看到，publisher发送的数据，在subscriber上面能正常收到并打印。
