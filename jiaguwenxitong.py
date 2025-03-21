import cv2
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import os
import json
from PIL import Image, ImageDraw
import torch
from torch.utils.data import Dataset, DataLoader
import torch.optim as optim
import torch.nn as nn
from torchvision import transforms

# 设置支持中文的字体
font = FontProperties(fname=r'C:\Windows\Fonts\simhei.ttf', size=14)

# 加载图像，以灰度模式读取
original_image = cv2.imread(r"C:\Data\1_Pre_test\w01637.jpg", cv2.IMREAD_GRAYSCALE)

# 应用双边滤波进行降噪
bilateral_filtered = cv2.bilateralFilter(original_image, 9, 75, 75)

# 创建CLAHE对象（对比度限制的自适应直方图均衡化）
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

# 在双边滤波后应用CLAHE
clahe_on_bilateral = clahe.apply(bilateral_filtered)

# 绘制和显示处理后的图像
plt.figure(figsize=(12, 6))

# 原始图像
plt.subplot(1, 2, 1)
plt.imshow(original_image, cmap='gray')
plt.title('原始图像', fontproperties=font)
plt.axis('off')

# 双边滤波后应用CLAHE的图像
plt.subplot(1, 2, 2)
plt.imshow(clahe_on_bilateral, cmap='gray')
plt.title('双边滤波后应用CLAHE', fontproperties=font)
plt.axis('off')

plt.tight_layout()
plt.show()

# 设置设备
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class CustomDataset(Dataset):
    def __init__(self, folder_path, transform=None):
        self.folder_path = folder_path
        self.transform = transform
        self.items = [file.replace('.json', '') for file in os.listdir(folder_path) if file.endswith('.json')]

    def __len__(self):
        return len(self.items)

    def __getitem__(self, idx):
        base_name = self.items[idx]
        img_path = os.path.join(self.folder_path, f"{base_name}.jpg")
        label_path = os.path.join(self.folder_path, f"{base_name}.json")

        # 加载图像
        image = Image.open(img_path).convert('L')

        # 加载并处理标签
        with open(label_path, 'r') as f:
            label_data = json.load(f)

        # 创建一个空白的掩膜，大小与图像相同
        mask = Image.new('L', image.size, 0)
        draw = ImageDraw.Draw(mask)

        # 读取每个注释并绘制矩形
        for ann in label_data['ann']:
            x1, y1, x2, y2, cls = ann
            if cls == 1.0:  # 只处理我们关心的类别
                draw.rectangle([x1, y1, x2, y2], outline=1, fill=1)

        # 应用图像转换
        if self.transform:
            image = self.transform(image)
            mask = self.transform(mask)

        return image, mask

def pixel_accuracy(output, mask):
    with torch.no_grad():
        output = torch.sigmoid(output) >= 0.5  # 将 logits 转换为二值图像
        correct = (output == mask).float()  # 正确预测的像素
    return correct.sum() / correct.numel()  # 总正确率

def iou(output, mask, smooth=1e-6):
    with torch.no_grad():
        output = torch.sigmoid(output) >= 0.5  # 将 logits 转换为二值图像
        intersection = (output & mask).float().sum((1, 2))  # 交集
        union = (output | mask).float().sum((1, 2))  # 并集
        return (intersection + smooth) / (union + smooth)

class Detect(nn.Module):
    def __init__(self):
        super(Detect, self).__init__()
        # Detect 类的初始化代码
        pass

class Segment(Detect):
    def __init__(self):
        super(Segment, self).__init__()
        # Segment 类的初始化代码
        pass

class BaseModel(nn.Module):
    def __init__(self):
        super(BaseModel, self).__init__()
        # BaseModel 类的初始化代码
        pass

class DetectionModel(BaseModel):
    def __init__(self):
        super(DetectionModel, self).__init__()
        # DetectionModel 类的初始化代码
        pass

class SegmentationModel(DetectionModel):
    def __init__(self):
        super(SegmentationModel, self).__init__()
        # SegmentationModel 类的初始化代码
        pass

class ClassificationModel(BaseModel):
    def __init__(self):
        super(ClassificationModel, self).__init__()
        # ClassificationModel 类的初始化代码
        pass

def parse_model(d, ch):
    # parse_model 函数的实现
    pass

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--cfg", type=str, default="yolov5s.yaml", help="model.yaml")
    parser.add_argument("--batch-size", type=int, default=1, help="total batch size for all GPUs")
    parser.add_argument("--device", default="", help="cuda device, i.e. 0 or 0,1,2,3 or cpu")
    parser.add_argument("--profile", action="store_true", help="profile model speed")
    parser.add_argument("--line-profile", action="store_true", help="profile model speed layer by layer")
    parser.add_argument("--test", action="store_true", help="test all yolo*.yaml")
    opt = parser.parse_args()
    opt.cfg = check_yaml(opt.cfg)  # check YAML
    print_args(vars(opt))
    device = select_device(opt.device)

    # 创建模型
    im = torch.rand(opt.batch_size, 3, 640, 640).to(device)
    model = DetectionModel(opt.cfg).to(device)

    # 选项
    if opt.line_profile:  # 逐层分析
        model(im, profile=True)
    elif opt.profile:  # 前后向分析
        results = profile(input=im, ops=[model], n=3)
    elif opt.test:  # 测试所有模型
        for cfg in Path(ROOT / "models").rglob("yolo*.yaml"):
            try:
                _ = DetectionModel(cfg)
            except Exception as e:
                print(f"Error in {cfg}: {e}")
    else:  # 报告融合模型摘要
        model.fuse()