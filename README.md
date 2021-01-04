# 雨粒を集めましょう  
![Screenshot from 2021-01-05 01-48-02](https://user-images.githubusercontent.com/52824423/103558904-b0343700-4ef8-11eb-9f32-1a9fbc725d76.png)  
![Screenshot from 2021-01-05 01-48-23](https://user-images.githubusercontent.com/52824423/103558961-c5a96100-4ef8-11eb-98a8-1bdf18dead22.png)

## 環境
OS: Ubuntu18.04  
Ros  
Python2.7  
## セットアップ方法  
```
git clone https://github.com/sakatanitouga/robosys_l.git  
```  

cloneしたフォルダの中の robosys_l/src のディレクトリに行き  

```
chmod +x key_input.py
chmod +x tkinter_ui.py
```
と入力し、実行許可を行う  

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

