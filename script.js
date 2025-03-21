from flask import Flask, request, jsonify
import cv2
import numpy as np
from PIL import Image
import io
import torch
from torchvision import transforms

app = Flask(__name__)

# 加载模型（假设模型已经训练好并保存为 model.pth）
model = torch.load('class.pth')
model.eval()

# 图像预处理
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # 读取图像
    image = Image.open(io.BytesIO(file.read()))
    image = transform(image).unsqueeze(0)

    # 调用模型进行识别
    with torch.no_grad():
        output = model(image)
        _, predicted = torch.max(output.data, 1)
        result = predicted.item()

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)