# 服务器信息统计工具

依赖：python3 ssh sshpass

在Windows Subsystem for Linux (WSL)中测试

将要操作的服务器地址写入ip.txt，一行一个

## 生成known_hosts

```
./generate_known_hosts.sh >> /path/to/known_hosts
```
该方法不具有去除重复的功能，已有的还会再添加

## 拷贝公钥

为支持ssh无密码登录，首先拷贝公钥到所有目标服务器

首先将登录密码写入password文件（如果需要密码的话）

```
./copy_id.sh
```

## 统计版本

```
python3 gather_version.py > out/version.txt
```

## 统计用户

```
python3 gather_users.py > out/users.txt
```
结果可直接复制入Excel进行进一步的处理
