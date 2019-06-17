
# -----------------------------------------------------------------------------------------------------------
# adb  +  appium  基 础 参 数
# Automatic Server 如果出现 Could not connect to server; are you sure it's running? 就点击下面的选项再启动
# Custom Server
# 除了设置java se 和 android sdk 及 appium 添加path ,还要将 appium 里
# 的 aapt 添加到 path 系统环境里边 地址： C:\Program Files (x86)\Android\android-sdk\build-tools\29.0.0
# 安卓5.1系统 启动：
# No route found. Setting content type to 'text/plain'   切换旧版本appium即可  地址：在我的百度网盘
# desired_caps['udid'] = '88MFDMG3AVLH' 如果要同时开启两台手机上的app  需要添加这个选项，参数就是设备码
# -----------------------------------------------------------------------------------------------------------

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

#     6.automationName: UiAutomator2  避免重复安装appiumsetting 包
# 
#     7.udid = '88MFDMG3AVLH' 如果要同时开启两台手机上的app  需要添加这个选项，参数就是手机设备码




