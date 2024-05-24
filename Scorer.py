import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def analyze_scores(scores):
    try:
        scores = list(map(int, scores.split()))
        if not scores:
            raise ValueError("請輸入有效的成績")
        
        passed_scores = [score for score in scores if score >= 60]
        failed_scores = [score for score in scores if score < 60]

        if not passed_scores:
            messagebox.showinfo("結果", "全班均未及格")
        else:
            min_passed_score = min(passed_scores)
            messagebox.showinfo("結果", f"最低及格分數為: {min_passed_score}")

        if not failed_scores:
            messagebox.showinfo("結果", "全班均及格")
        else:
            max_failed_score = max(failed_scores)
            messagebox.showinfo("結果", f"最高未及格分數為: {max_failed_score}")

        # 清空之前的圖表
        for widget in canvas_frame.winfo_children():
            widget.destroy()

        # 成績分佈直方圖
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.hist(scores, bins=10, color='skyblue', edgecolor='black')
        ax.set_title('成績分佈直方圖')
        ax.set_xlabel('分數')
        ax.set_ylabel('人數')
        ax.grid(True)

        # 將圖表嵌入到 tkinter GUI 中
        canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
    except ValueError as e:
        messagebox.showerror("錯誤", str(e))

def process_scores():
    analyze_scores(score_entry.get())

# 創建主窗口
root = tk.Tk()
root.title("成績分析器")

# 添加用戶界面元素
score_label = tk.Label(root, text="輸入全班成績（以空格分隔）：")
score_label.pack(pady=5)

score_entry = tk.Entry(root)
score_entry.pack(pady=5)

analyze_button = tk.Button(root, text="分析成績", command=process_scores)
analyze_button.pack(pady=5)

# 添加一個框架來顯示圖表
canvas_frame = tk.Frame(root)
canvas_frame.pack(fill=tk.BOTH, expand=1)

# 啟動主循環
root.mainloop()
