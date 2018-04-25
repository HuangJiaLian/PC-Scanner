### PC Scanner

#### 简介

这是一个运行在PC端的跨平台条形码，二维码扫描器。另外对于增值税开票二维码(国税，支付宝)，结合官方开票软件可以实现闪电开票。

#### 安装Python库

Linux:
``` bash
sudo apt-get install  python-xlib
sudo pip install pyautogui
sudo pip install clipboard
sudo apt-get install libzbar-dev
sudo pip install zbar
sudo apt-get install python-opencv
```
Window:

1. zbar:从[这里](https://github.com/jacobvalenta/zbar-py27-msi/blob/master/zbar-0.10.win32-py2.7_2.msi)下载
2. 其他：
    ``` bash
    pip install pyautogui
    pip install clipboard
    pip install chardet
    python -m pip install opencv-python
    ```


#### 说明

- 编程语言：`Python`
- 使用技术：
  - `OpenCV`: 获取摄像头采集的图像
  - `PIL`: 图片格式转化
  - `Zbar`: 条形码，二维码解码库
  - `pyautogui`, `clipboard`: 将解码数据粘贴到其他图形界面
  - `signal`: 处理按键操作
- 运行环境: `Window` , `Linux`

使用说明:

使用之前确保摄像头运行正常。

1. 安装对应的Pyhton库
2. 命令行运行：`python pcScanner.py`
3. 打开一个可编译窗口，例如`windows`上的`记事本` 或者`Linux`上的`Leafpad`软件
4. 利用摄像头对准待扫描的条码，扫描结果便会出现在编辑窗口