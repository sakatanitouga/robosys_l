# 雨粒を集めましょう  
![Screenshot from 2021-01-05 01-48-02](https://user-images.githubusercontent.com/52824423/103558904-b0343700-4ef8-11eb-9f32-1a9fbc725d76.png)  
## リポジトリの概要  
落ちてくる雨粒を集めるゲームです。  

## 動作環境
OS: Ubuntu18.04  
Ros  
Python 2.7  
pygame 1.9.6
## 使用したもの  
Ubuntu18.04 OSのPC  

## デモ動画  
https://www.youtube.com/watch?v=57TtqhpEYpI  

## インストール方法  
Rosのインストール方法は以下のリンクを参考に入れてください。  
http://wiki.ros.org/ja/kinetic/Installation/Ubuntu  

インストールが完了したら/catkin_ws/srcのディレクトリに移動し以下を入力してください。  
```
git clone https://github.com/sakatanitouga/robosys_l.git  
```  

cloneしたフォルダの中へ移動し  

```
./ setup.sh
```
と入力するとインストールが始まります。  

## 遊び方  
ターミナル上で
```
roscore
```

別のターミナルでcloneしたフォルダの中の robosys_l/src のディレクトリに行き以下を入力  
```
rosrun robosys_l tkinter_ui.py
```  
!!注意!!  
tkinter_ui.pyの実行はrobosys_l/src のディレクトリで実行を行わないと音声ファイルが再生されないので　　
robosys_l/srcのディレクトリで実行するようにしてください。

別のターミナルで以下を入力
```
rosrun robosys_l key_input.py
```

## ライセンス  
こちらのリポジトリのライセンスはBSD-2-Clause Licenseです。詳しくは[こちら](https://github.com/sakatanitouga/robosys_l/blob/master/LICENSE)。