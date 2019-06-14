
# ------------------------------------------------------------------
# adb  +  appium  基 础 参 数
# Automatic Server 运行程序提示是否run ,可以点击下边的这个选项来启动
# Custom Server
# ------------------------------------------------------------------

# 查 看 当 前手  机 运 行 的 app 名 称 及 进 程 名 字

# 命令：adb shell dumpsys window | findstr mCurrentFocus

# 结果：  mCurrentFocus=Window{2b2e12bd u0 com.ss.android.ugc.aweme/com.ss.android.ugc.aweme.main.MainActivity}

# 包名 ： com.ss.android.ugc.aweme  进程入口名：com.ss.android.ugc.aweme.main.MainActivity  注意这是个完整进口，一定要完整的才行


#查 看 手 机 的 设 备 编 号

# 命令： adb devices

# 结果：List of devices attached
#       88AKDMH22BEC    device   手机设备型号
#       如果出现 offlin 就执行 adb kill-server 再adb start-server



# 命令： adb shell getprop ro.build.version.release
#
# 结果： 5.1     安卓版本
#
#
#     1.platformName：这里是android的apk
#
#     2.deviceName：手机设备名称，通过adb devices查看
#
#     3.platformVersion：android系统的版本号
#
#     4.appPackage：apk包名
#
#     5.appActivity：apk的launcherActivity




