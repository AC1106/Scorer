import os

def ensure_utf8_encoding(file_path):
    if not os.path.isfile(file_path):
        print(f"文件 {file_path} 不存在")
        return
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file.read()
        print(f"文件 {file_path} 已經是 UTF-8 編碼")
    except UnicodeDecodeError:
        try:
            with open(file_path, 'r', encoding='latin1') as file:
                content = file.read()
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"已將 {file_path} 編碼轉換為 UTF-8")
        except Exception as e:
            print(f"轉換 {file_path} 時發生錯誤: {e}")

file_path = 'Scorer.py'
ensure_utf8_encoding(file_path)