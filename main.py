
#1worker 上线，登记到server，分配接收内存资源
#2系统初始化，server确定参与训练的worker，分配通信资源，打开上传链路监听，分配接收内存资源
#3sever 确定model，将model分发给各个选中的worker
#4worker接收model，根据自身数据进行训练
#5worker根据自身的端口上传数据进入channel
#6server在channel的出口接收到数据
#7server根据数据更新模型
#8server 更新模型，重新进入3（不满足退出循环条件）或结束训练（满足退出循环条件）
#9分发模型

#channel的接收数据可以存在文件中或者内存中，然后再等待读取（Pymalloc，用法(wchar_t **)PyMem_RawMalloc(sizeof(wchar_t*) * (argc+1)),https://github.com/IzunaDevs/TinyURL/blob/a0f69ce6db0e89def99e0abbc74d1ef851eafae4/app/make_tinyurl_c.py,argv_copy[i] ） 