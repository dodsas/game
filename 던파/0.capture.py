import tkinter as tk
from tkinter import simpledialog, messagebox
import subprocess
import os
import time
import pyautogui

class ImageCaptureToolApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Image Capture Tool with Mouse Tracker")
        self.root.geometry("400x350")
        
        # images 폴더 경로 확인 및 생성
        self.images_folder = os.path.join(os.path.dirname(__file__), 'images')
        if not os.path.exists(self.images_folder):
            os.makedirs(self.images_folder)
        
        # 마우스 위치 추적을 위한 변수
        self.mouse_tracking = False
        
        self.setup_ui()
        self.start_mouse_tracking()
        
    def setup_ui(self):
        title_label = tk.Label(self.root, text="이미지 캡처 도구", font=("Arial", 14, "bold"))
        title_label.pack(pady=10)
        
        info_label = tk.Label(self.root, text="macOS 내장 스크린샷 도구를 사용하여\n영역을 선택하고 이미지를 저장합니다", font=("Arial", 10))
        info_label.pack(pady=5)
        
        # 마우스 좌표 표시 프레임
        mouse_frame = tk.Frame(self.root, relief="sunken", borderwidth=2, bg="lightgray")
        mouse_frame.pack(pady=10, padx=20, fill="x")
        
        mouse_title = tk.Label(mouse_frame, text="실시간 마우스 좌표", font=("Arial", 11, "bold"), bg="lightgray")
        mouse_title.pack(pady=2)
        
        self.mouse_label = tk.Label(mouse_frame, text="X: 0, Y: 0", font=("Arial", 12, "bold"), fg="red", bg="lightgray")
        self.mouse_label.pack(pady=5)
        
        # 파일명 입력 필드 추가
        filename_label = tk.Label(self.root, text="저장할 파일명을 입력하세요:", font=("Arial", 11, "bold"))
        filename_label.pack(pady=(10, 5))
        
        self.filename_entry = tk.Entry(self.root, 
                                      font=("Arial", 14), 
                                      width=25, 
                                      relief="solid", 
                                      borderwidth=2,
                                      bg="white",
                                      fg="black",
                                      insertbackground="black",
                                      highlightthickness=2,
                                      highlightcolor="blue")
        self.filename_entry.pack(pady=10, padx=20)
        self.filename_entry.focus()  # 처음 실행시 입력 필드에 포커스
        
        capture_button = tk.Button(self.root, text="영역 선택 및 캡처", 
                                 command=self.start_capture, 
                                 font=("Arial", 12),
                                 bg="#4CAF50",
                                 fg="white",
                                 width=20,
                                 height=2)
        capture_button.pack(pady=15)
        
        instruction_label = tk.Label(self.root, text="1. 파일명 입력\n2. 버튼 클릭\n3. 영역 드래그 선택\n(마우스 좌표가 실시간으로 표시됩니다)", 
                                   font=("Arial", 9), 
                                   fg="gray")
        instruction_label.pack(pady=5)
        
    def start_capture(self):
        # 입력 필드에서 파일명 가져오기
        filename = self.filename_entry.get().strip()
        
        print(f"DEBUG: 입력된 파일명: '{filename}'")  # 디버깅용
        
        if not filename:
            messagebox.showwarning("알림", "파일명을 입력해주세요.")
            return
        
        temp_path = os.path.join(self.images_folder, f"{filename}_temp.png")
        final_path = os.path.join(self.images_folder, f"{filename}.jpg")
        print(f"DEBUG: 저장 경로: {final_path}")  # 디버깅용
        
        try:
            # macOS 스크린샷 도구로 임시 PNG 파일 생성
            result = subprocess.run([
                "screencapture", 
                "-i",  # 인터랙티브 모드 (영역 선택)
                "-r",  # 소리 끄기
                temp_path
            ], timeout=30)
            
            print(f"DEBUG: screencapture 결과: {result.returncode}")  # 디버깅용
            print(f"DEBUG: 임시 파일 존재 여부: {os.path.exists(temp_path)}")  # 디버깅용
            
            if result.returncode == 0 and os.path.exists(temp_path):
                # PNG를 JPG로 변환
                try:
                    from PIL import Image
                    img = Image.open(temp_path)
                    img = img.convert('RGB')  # PNG의 투명도 제거
                    img.save(final_path, "JPEG", quality=95)
                    
                    # 임시 PNG 파일 삭제
                    os.remove(temp_path)
                    
                    print(f"DEBUG: JPG 변환 완료: {final_path}")
                    messagebox.showinfo("완료", f"이미지가 JPG로 저장되었습니다:\n{final_path}")
                except ImportError:
                    # PIL이 없으면 PNG 그대로 저장하되 확장자는 jpg로
                    import shutil
                    shutil.move(temp_path, final_path.replace('.jpg', '.png'))
                    messagebox.showinfo("완료", f"이미지가 PNG로 저장되었습니다:\n{final_path.replace('.jpg', '.png')}")
            else:
                messagebox.showinfo("취소", "스크린샷이 취소되었습니다.")
                
        except subprocess.TimeoutExpired:
            messagebox.showwarning("시간 초과", "스크린샷 시간이 초과되었습니다.")
        except Exception as e:
            messagebox.showerror("오류", f"스크린샷 중 오류가 발생했습니다:\n{str(e)}")
    
    def start_mouse_tracking(self):
        """마우스 위치 추적 시작"""
        self.mouse_tracking = True
        self.update_mouse_position()
    
    def update_mouse_position(self):
        """마우스 위치를 실시간으로 업데이트"""
        if self.mouse_tracking:
            try:
                x, y = pyautogui.position()
                self.mouse_label.config(text=f"X: {x}, Y: {y}")
            except Exception:
                self.mouse_label.config(text="X: -, Y: -")
            
            # 100ms마다 업데이트
            self.root.after(100, self.update_mouse_position)
    
    def run(self):
        try:
            self.root.mainloop()
        finally:
            self.mouse_tracking = False

if __name__ == "__main__":
    app = ImageCaptureToolApp()
    app.run()