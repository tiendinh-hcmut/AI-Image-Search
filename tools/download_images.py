import requests
import os

keywords = ["forest", "cat", "city", "food", "ocean"]
num_images = 5

os.makedirs('data', exist_ok=True)

for word in keywords:
    print(f"Đang tải ảnh cho từ khóa: {word}")
    for i in range(num_images):
        url = f"https://loremflickr.com/500/500/{word}?lock={i}"
        response = requests.get(url)
        
        if response.status_code == 200:
            file_path = f"data/{word}_{i}.jpg"
            with open(file_path, "wb") as f:
                f.write(response.content)
            print(f"  -> Đã lưu thành công: {word}_{i}.jpg")
        else:
            print(f"  -> Lỗi không tải được ảnh {word}_{i} (Mã lỗi: {response.status_code})")

print("Hoàn tất việc tải ảnh!")