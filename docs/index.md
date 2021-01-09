このドキュメントは制作のメモ的な位置付けです。詳細な手順までは記載されていません。

# ハードウェア
## 構成

||コメント|
|---|---|
|メカナムホイールカーキット|OSOYOO メカナムホイールカー キット|
|Jetson Nano|古いA02モデル。メモリ4G|
|Jetson Nano用電源|INIU モバイルバッテリ 容量10000mAh。最大出力3A|
|Wi-Fiドングル|TP-Link TL-WN725N|
|ゲームパッド|ロジクール ワイヤレスゲームパッド F710|
|PCA9685|VKLSVAN PCA9685 16チャンネル 12ビット PWM ドライバー|
|LiDAR|LDS-01|
|カメラ|Intel RealSense Tracking Camera T265|

Jetson Nanoの電源はとりあえず車体とは別にしました。

## 組み立て方法
まずは、[公式のレッスン1](https://osoyoo.com/2019/11/08/metal-chassis-mecanum-wheel-robotic-for-arduino-mega2560-lesson1-robot-car-assembly/)まで組み立てる。  
  
車体から Arduino Mega 2560互換ボードを取り外す。  

[ブログの内容](https://www.sato-susumu.com/entry/mecanum-jetson)を参考に、メカナムホイールカート、Jetson Nano、PCA9685を接続する。  
  
LiDAR LDS-01、Intel RealSense Tracking Camera T265をUSBケーブルで接続する。  

# ソフトウェア
[ブログの内容](https://www.sato-susumu.com/entry/mecanum-jetson)を参考にUbuntuからコントロールできるようにする。    

Jetson NanoにROS Melodicをインストール。  

```
$ mkdir -p ~/catkin_ws/src
$ cd ~/catkin_ws/src
$ git clone https://github.com/sato-susumu/ss_mecanum
$ cd ~/catkin_ws
$ catkin_make
$ source devel/setup.bash
```

# 参考
[PCA9685の動作確認方法］(https://www.sato-susumu.com/entry/pwm_pca9685)  
[LiDAR LDS-01の動作確認方法](https://www.sato-susumu.com/entry/LDS-01)  

