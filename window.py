import tkinter as tk
from tkinter import filedialog
import requests
import json

# 視窗設定
window = tk.Tk()
window.title("metadata分析")
window.geometry("600x400+250+150")

# 上傳函數
def upload_file():
    file_path = filedialog.askopenfilename() 
    if file_path:
        url = "https://www.virustotal.com/api/v3/files"
        headers = {
            "x-apikey": "873bfdcc900cf2e151f9346f6fd847a22ea215fc6f0ab0fcaa9a38f76f9115d5"
        }
        with open(file_path, "rb") as file:
            files = {"file": (file.name, file)}
            response = requests.post(url, headers=headers, files=files)
            result_label.config(text="上传结果：\n" + response.text)

            jf = json.loads(response.text)
            id_content = jf['data']['id']
            print(id_content)

            url = "https://www.virustotal.com/api/v3/analyses/"+id_content

            headers = {
                "accept": "application/json",
                "x-apikey": "873bfdcc900cf2e151f9346f6fd847a22ea215fc6f0ab0fcaa9a38f76f9115d5"
            }

            response = requests.get(url, headers=headers)

            print(response.text)

# 上傳按鈕
upload_button = tk.Button(window, text="上传文件", command=upload_file)
upload_button.pack(pady=20)

# 顯示結果
result_label = tk.Label(window, text="", wraplength=400)
print
result_label.pack()

# 啟動視窗
window.mainloop()



