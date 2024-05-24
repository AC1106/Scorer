import os

def ensure_utf8_encoding(file_path):
    if not os.path.isfile(file_path):
        print(f"��� {file_path} ���s�b")
        return
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file.read()
        print(f"��� {file_path} �w�g�O UTF-8 �s�X")
    except UnicodeDecodeError:
        try:
            with open(file_path, 'r', encoding='latin1') as file:
                content = file.read()
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"�w�N {file_path} �s�X�ഫ�� UTF-8")
        except Exception as e:
            print(f"�ഫ {file_path} �ɵo�Ϳ��~: {e}")

file_path = 'Scorer.py'
ensure_utf8_encoding(file_path)