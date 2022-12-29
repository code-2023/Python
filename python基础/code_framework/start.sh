#!/bin/bash

#这是一段shell启动脚本

function init() {
  export PYTHON_SCRIPT_DIR=/local/learn_python/
  echo 创建了一个环境变量:
  echo --------------------------------------
  PYTHON_SCRIPT=$PYTHON_SCRIPT_DIR/main.py
}
function fun() {
    python $PYTHON_SCRIPT
}
function start(){
  init
  fun
}
start