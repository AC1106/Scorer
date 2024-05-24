import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def analyze_scores(scores):
    try:
        scores = list(map(int, scores.split()))
        if not scores:
            raise ValueError("�п�J���Ī����Z")
        
        passed_scores = [score for score in scores if score >= 60]
        failed_scores = [score for score in scores if score < 60]

        if not passed_scores:
            messagebox.showinfo("���G", "���Z�����ή�")
        else:
            min_passed_score = min(passed_scores)
            messagebox.showinfo("���G", f"�̧C�ή���Ƭ�: {min_passed_score}")

        if not failed_scores:
            messagebox.showinfo("���G", "���Z���ή�")
        else:
            max_failed_score = max(failed_scores)
            messagebox.showinfo("���G", f"�̰����ή���Ƭ�: {max_failed_score}")

        # �M�Ť��e���Ϫ�
        for widget in canvas_frame.winfo_children():
            widget.destroy()

        # ���Z���G�����
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.hist(scores, bins=10, color='skyblue', edgecolor='black')
        ax.set_title('���Z���G�����')
        ax.set_xlabel('����')
        ax.set_ylabel('�H��')
        ax.grid(True)

        # �N�Ϫ�O�J�� tkinter GUI ��
        canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
    except ValueError as e:
        messagebox.showerror("���~", str(e))

def process_scores():
    analyze_scores(score_entry.get())

# �ЫإD���f
root = tk.Tk()
root.title("���Z���R��")

# �K�[�Τ�ɭ�����
score_label = tk.Label(root, text="��J���Z���Z�]�H�Ů���j�^�G")
score_label.pack(pady=5)

score_entry = tk.Entry(root)
score_entry.pack(pady=5)

analyze_button = tk.Button(root, text="���R���Z", command=process_scores)
analyze_button.pack(pady=5)

# �K�[�@�Ӯج[����ܹϪ�
canvas_frame = tk.Frame(root)
canvas_frame.pack(fill=tk.BOTH, expand=1)

# �ҰʥD�`��
root.mainloop()
