import os
import cv2

# 所有需要处理的图片的路径
traversal_file="F:\Photo\Chose"
# 添加水印后的图片的路径
watermask_file="F:\Photo\Added"
# 水印图片路径
mark_path="F:\Signature.png"

def add_water(img_path,mark_path,save_path):
    # 读取原图片
    print(f"Image path: {img_path}")  # Print the image path
    if not os.path.exists(img_path):  # Check if the file exists
        print(f"File does not exist: {img_path}")
        return
    img = cv2.imread(img_path)
    h, w = img.shape[0], img.shape[1]
    print("Original h : " + str(h) + "px Original w : " + str(w)+"px")
    # 读取水印图片
    mark = cv2.imread(mark_path)
    mark_h, mark_w = mark.shape[0], mark.shape[1]
    print("watermark h : " + str(mark_h) + "px watermark w : " + str(mark_w)+"px")
    # 根据小图像的大小，在大图像上创建感兴趣区域roi（放置位置任意取）
    rows, cols = mark.shape[:2]  # 获取水印的高度、宽度
    # 水印应该在图片的右下角
    roi = img[h - mark_h:h, w - mark_w:w]  # 获取原图roi
    print(roi.shape[:2]) # 打印roi大小
    dst = cv2.addWeighted(mark, 1, roi, 1, 0)  # 图像融合
    add_img = img.copy()  # 对原图像进行拷贝
    add_img[h - mark_h:h, w - mark_w:w] = dst  # 将融合后的区域放进原图
    # 保存添加水印后的图片
    cv2.imwrite(save_path+".jpg", add_img)

# 首先检测两个路径是否都可访问，如果水印路径没有则创建
if os.path.isdir(traversal_file):
    print("Check traversal file ok")
else:
    print("Traversal file error")
if os.path.isdir(watermask_file):
    print("Check water mask file ok")
else:
    print("Water mask file warning,auto create it")
    os.mkdir(watermask_file)

# 遍历传入的文件夹，挨个给文件添加水印

dirs=os.listdir(traversal_file)
print("Traversing file...")
for file in dirs:
    
    print(file[:-4])
    file_name=file[:-4] # 这里裁剪文件后缀.jpg .png
    # if file_name[-1]=="+" : # 这里判断除去后缀后，文件名最后一个是不是"+"这个字符
    print(file+" add water marking...")
    add_water(traversal_file+"/"+file,mark_path,watermask_file+"/"+file_name)
