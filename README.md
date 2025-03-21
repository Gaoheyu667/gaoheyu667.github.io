README

项目简介 本项目围绕甲骨文展开，结合网页展示与 AI 技术（如模型识别），实现甲骨文相关内容的展示、分类、识别等功能。 以下是项目文件结构及说明：

文件结构与说明

文件夹

.idea：IntelliJ IDEA生成的项目配置文件夹，存储编译、模块等配置。

images：项目图片资源文件夹，存放网页所需的图片素材。 网页文件（HTML）

index1.html：项目主页，承载核心展示内容。

detail.html - detail8.html：详情页，用于展示甲骨文具体信息（如定义、分类、历史意义等）。

ai识别.html：AI 识别功能页面，实现甲骨文图片识别交互。

图片资源

各类 .png/.jpg 文件（如 dingyi.png、jiaguwen1.jpg 等）：甲骨文相关配图、图标，用于网页可视化展示。

代码与模型文件

jiaguwenxitong.py：Python 核心逻辑脚本，可能处理数据、调用模型。

script.js/script1.js：JavaScript 脚本，负责网页前端交互逻辑。

.pth 文件（如 class.pth、oracle_model_epoch_50(1).pth）：PyTorch 训练的模型文件，用于甲骨文分类、识别等 AI 功能。

style1.css/styles.css：CSS 样式文件，控制网页页面布局与样式。

技术栈

前端：HTML + CSS + JavaScript

后端 / AI：Python、PyTorch（模型训练与推理）

开发工具： PyCharm、IntelliJ IDEA 。

运行指南

网页部分：直接使用浏览器打开 index1.html 及各详情页 HTML 文件，查看网页内容。

环境配置与依赖安装说明

前端环境（网页展示）

运行方式：直接使用现代浏览器（如 Chrome、Edge）打开 HTML 文件，无需额外安装依赖。

后端 / AI 功能（Python 脚本）
环境要求： Python 3.7+ 依赖安装： bash pip install torch torchvision torchaudio
运行脚本： 确保模型文件（.pth）与 jiaguwenxitong.py 在同一目录，执行： bash python jiaguwenxitong.py
