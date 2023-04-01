import os
import shutil

# 定义数据路径
data_path = "D:/granduationpro/python/plant_identification/data"

# 定义标签
labels = ["Strawberry", "calamus", "lotus", "rosy", "Willd", "grape"]

# 遍历每个文件夹，将其中所有图片移到以标签命名的文件夹
for i, label in enumerate(labels):
    # 创建以标签命名的文件夹
    os.makedirs(os.path.join(data_path, str(i)), exist_ok=True)
    # 获取该类别的所有图片路径
    images_path = os.path.join(data_path, label)
    image_names = os.listdir(images_path)
    # 将图片移动到以标签命名的文件夹中
    for image_name in image_names:
        shutil.move(os.path.join(images_path, image_name), os.path.join(data_path, str(i), image_name))
