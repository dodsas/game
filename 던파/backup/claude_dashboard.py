import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import json
import threading
import time
from datetime import datetime, timedelta
import re
import os
from claude_monitor_parser import ClaudeMonitorParser
from backup.usage_chart import UsageChartWindow

class ClaudeDashboard:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🤖 Claude Monitor Dashboard")
        self.root.geometry("800x600")
        self.root.configure(bg="#1a1a1a")
        
        # 현재 상태
        self.current_usage = 0
        self.daily_limit = 1000000  # 기본값
        self.current_plan = "custom"
        self.is_monitoring = False
        self.monitor_process = None
        
        # Claude Monitor 파서
        self.parser = ClaudeMonitorParser()
        
        # 스타일 설정
        self.setup_styles()
        
        # UI 구성
        self.setup_ui()
        
        # 모니터링 시작
        self.start_monitoring()
        
    def setup_styles(self):
        """다크 테마 스타일 설정"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # 다크 테마 색상
        style.configure('Dark.TFrame', background='#1a1a1a')
        style.configure('Dark.TLabel', background='#1a1a1a', foreground='#ffffff', font=('SF Pro Display', 12))
        style.configure('Title.TLabel', background='#1a1a1a', foreground='#00d4aa', font=('SF Pro Display', 24, 'bold'))
        style.configure('Metric.TLabel', background='#2d2d2d', foreground='#ffffff', font=('SF Pro Display', 14), relief='solid')
        style.configure('Value.TLabel', background='#2d2d2d', foreground='#00d4aa', font=('SF Pro Display', 18, 'bold'))
        
    def setup_ui(self):
        """UI 구성"""
        # 메인 컨테이너
        main_frame = ttk.Frame(self.root, style='Dark.TFrame')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # 헤더
        header_frame = ttk.Frame(main_frame, style='Dark.TFrame')
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        title_label = ttk.Label(header_frame, text="🤖 Claude Usage Monitor", style='Title.TLabel')
        title_label.pack(side=tk.LEFT)
        
        # 상태 표시
        self.status_label = ttk.Label(header_frame, text="🔴 Disconnected", style='Dark.TLabel')
        self.status_label.pack(side=tk.RIGHT)
        
        # 메트릭 카드들
        metrics_frame = ttk.Frame(main_frame, style='Dark.TFrame')
        metrics_frame.pack(fill=tk.X, pady=(0, 20))
        
        # 토큰 사용량 카드
        self.create_metric_card(metrics_frame, "💭 Current Usage", "0 tokens", "usage_value", 0)
        
        # 일일 한도 카드
        self.create_metric_card(metrics_frame, "📊 Daily Limit", "1,000,000 tokens", "limit_value", 1)
        
        # 사용률 카드
        self.create_metric_card(metrics_frame, "📈 Usage Rate", "0%", "rate_value", 2)
        
        # 남은 토큰 카드
        self.create_metric_card(metrics_frame, "⏳ Remaining", "1,000,000 tokens", "remaining_value", 3)
        
        # 프로그레스 바
        progress_frame = ttk.Frame(main_frame, style='Dark.TFrame')
        progress_frame.pack(fill=tk.X, pady=(0, 20))
        
        progress_label = ttk.Label(progress_frame, text="📊 Usage Progress", style='Dark.TLabel')
        progress_label.pack(anchor=tk.W, pady=(0, 10))
        
        self.progress = ttk.Progressbar(progress_frame, mode='determinate', length=600, style='TProgressbar')
        self.progress.pack(fill=tk.X)
        
        # 세션 정보
        session_frame = ttk.Frame(main_frame, style='Dark.TFrame')
        session_frame.pack(fill=tk.X, pady=(0, 20))
        
        session_label = ttk.Label(session_frame, text="📅 Session Info", style='Dark.TLabel')
        session_label.pack(anchor=tk.W, pady=(0, 10))
        
        info_frame = ttk.Frame(session_frame, style='Dark.TFrame')
        info_frame.pack(fill=tk.X)
        
        self.start_time_label = ttk.Label(info_frame, text="🕐 Started: --", style='Dark.TLabel')
        self.start_time_label.pack(side=tk.LEFT)
        
        self.plan_label = ttk.Label(info_frame, text="💎 Plan: Custom", style='Dark.TLabel')
        self.plan_label.pack(side=tk.RIGHT)
        
        # 컨트롤 버튼들
        control_frame = ttk.Frame(main_frame, style='Dark.TFrame')
        control_frame.pack(fill=tk.X, pady=(20, 0))
        
        self.refresh_btn = tk.Button(control_frame, text="🔄 Refresh", 
                                   command=self.refresh_data,
                                   bg="#00d4aa", fg="white", 
                                   font=("SF Pro Display", 12, "bold"),
                                   relief="flat", padx=20, pady=10)
        self.refresh_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        self.open_monitor_btn = tk.Button(control_frame, text="📊 Open Monitor", 
                                        command=self.open_claude_monitor,
                                        bg="#007acc", fg="white", 
                                        font=("SF Pro Display", 12, "bold"),
                                        relief="flat", padx=20, pady=10)
        self.open_monitor_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        self.settings_btn = tk.Button(control_frame, text="⚙️ Settings", 
                                    command=self.open_settings,
                                    bg="#666666", fg="white", 
                                    font=("SF Pro Display", 12, "bold"),
                                    relief="flat", padx=20, pady=10)
        self.settings_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        self.analytics_btn = tk.Button(control_frame, text="📊 Analytics", 
                                     command=self.open_analytics,
                                     bg="#9b59b6", fg="white", 
                                     font=("SF Pro Display", 12, "bold"),
                                     relief="flat", padx=20, pady=10)
        self.analytics_btn.pack(side=tk.LEFT)
        
        # 실시간 로그
        log_frame = ttk.Frame(main_frame, style='Dark.TFrame')
        log_frame.pack(fill=tk.BOTH, expand=True, pady=(20, 0))
        
        log_label = ttk.Label(log_frame, text="📝 Activity Log", style='Dark.TLabel')
        log_label.pack(anchor=tk.W, pady=(0, 10))
        
        # 스크롤 가능한 텍스트 영역
        log_container = tk.Frame(log_frame, bg="#1a1a1a")
        log_container.pack(fill=tk.BOTH, expand=True)
        
        self.log_text = tk.Text(log_container, bg="#0d1117", fg="#c9d1d9", 
                               font=("Monaco", 11), wrap=tk.WORD,
                               relief="flat", padx=15, pady=15)
        scrollbar = tk.Scrollbar(log_container, command=self.log_text.yview)
        self.log_text.config(yscrollcommand=scrollbar.set)
        
        self.log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # 시작 시간 기록
        self.session_start = datetime.now()
        self.start_time_label.config(text=f"🕐 Started: {self.session_start.strftime('%H:%M:%S')}")
        
        # 로그 초기 메시지
        self.add_log("🚀 Claude Dashboard initialized")
        self.add_log("🔗 Connecting to claude-monitor...")
        
    def create_metric_card(self, parent, title, value, var_name, column):
        """메트릭 카드 생성"""
        card_frame = tk.Frame(parent, bg="#2d2d2d", relief="solid", bd=1)
        card_frame.grid(row=0, column=column, padx=10, pady=10, sticky="ew")
        parent.grid_columnconfigure(column, weight=1)
        
        title_label = tk.Label(card_frame, text=title, bg="#2d2d2d", fg="#888888", 
                              font=("SF Pro Display", 12))
        title_label.pack(pady=(15, 5))
        
        value_label = tk.Label(card_frame, text=value, bg="#2d2d2d", fg="#00d4aa", 
                              font=("SF Pro Display", 18, "bold"))
        value_label.pack(pady=(0, 15))
        
        # 동적 업데이트를 위해 저장
        setattr(self, var_name, value_label)
        
    def start_monitoring(self):
        """모니터링 스레드 시작"""
        if not self.is_monitoring:
            self.is_monitoring = True
            self.monitor_thread = threading.Thread(target=self.monitor_loop, daemon=True)
            self.monitor_thread.start()
            
    def monitor_loop(self):
        """모니터링 루프"""
        while self.is_monitoring:
            try:
                self.get_claude_usage()
                time.sleep(5)  # 5초마다 업데이트
            except Exception as e:
                self.add_log(f"❌ Error: {str(e)}")
                time.sleep(10)
                
    def get_claude_usage(self):
        """Claude 사용량 정보 획득"""
        try:
            # 실제 claude-monitor 데이터 파싱
            data = self.parser.get_current_usage()
            
            if data:
                self.current_usage = data.get('current_usage', 0)
                self.daily_limit = data.get('daily_limit', 1000000)
                self.current_plan = data.get('plan', 'custom')
                
                usage_rate = (self.current_usage / self.daily_limit) * 100 if self.daily_limit > 0 else 0
                remaining = max(0, self.daily_limit - self.current_usage)
                
                # 데이터 저장
                self.parser.save_usage_data(data)
                
                # UI 업데이트
                self.root.after(0, self.update_ui, self.current_usage, usage_rate, remaining)
                
                # 연결 상태 업데이트
                status = data.get('status', 'connected')
                if status == 'connected' or self.current_usage > 0:
                    self.root.after(0, lambda: self.status_label.config(text="🟢 Connected"))
                    self.root.after(0, lambda: self.plan_label.config(text=f"💎 Plan: {self.current_plan.title()}"))
                else:
                    self.root.after(0, lambda: self.status_label.config(text="🟡 Limited Data"))
            else:
                self.root.after(0, lambda: self.status_label.config(text="🔴 No Data"))
            
        except Exception as e:
            self.add_log(f"❌ Error getting usage data: {str(e)}")
            self.root.after(0, lambda: self.status_label.config(text="🔴 Error"))
            
    def update_ui(self, usage, rate, remaining):
        """UI 업데이트"""
        # 메트릭 업데이트
        self.usage_value.config(text=f"{usage:,} tokens")
        self.rate_value.config(text=f"{rate:.1f}%")
        self.remaining_value.config(text=f"{remaining:,} tokens")
        
        # 프로그레스 바 업데이트
        self.progress['value'] = rate
        
        # 색상 변경 (사용률에 따라)
        if rate < 50:
            color = "#00d4aa"  # 초록
        elif rate < 80:
            color = "#f39c12"  # 주황
        else:
            color = "#e74c3c"  # 빨강
            
        self.usage_value.config(fg=color)
        
        # 로그 추가 (사용량이 크게 증가했을 때만)
        if hasattr(self, '_last_logged_usage'):
            if usage - self._last_logged_usage > 500:
                self.add_log(f"📈 Usage increased to {usage:,} tokens ({rate:.1f}%)")
                self._last_logged_usage = usage
        else:
            self._last_logged_usage = usage
            
    def add_log(self, message):
        """로그 메시지 추가"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        
        self.log_text.insert(tk.END, log_entry)
        self.log_text.see(tk.END)
        
        # 로그가 너무 길어지면 오래된 것 삭제
        lines = self.log_text.get("1.0", tk.END).count('\n')
        if lines > 100:
            self.log_text.delete("1.0", "10.0")
            
    def refresh_data(self):
        """데이터 새로고침"""
        self.add_log("🔄 Refreshing data...")
        threading.Thread(target=self.get_claude_usage, daemon=True).start()
        
    def open_claude_monitor(self):
        """Claude Monitor 열기"""
        try:
            self.add_log("📊 Opening Claude Monitor...")
            subprocess.Popen(["claude-monitor", "--theme", "dark"], 
                           stdout=subprocess.DEVNULL, 
                           stderr=subprocess.DEVNULL)
        except Exception as e:
            self.add_log(f"❌ Failed to open claude-monitor: {str(e)}")
            messagebox.showerror("Error", f"Failed to open claude-monitor:\n{str(e)}")
            
    def open_settings(self):
        """설정 창 열기"""
        settings_window = tk.Toplevel(self.root)
        settings_window.title("⚙️ Settings")
        settings_window.geometry("400x300")
        settings_window.configure(bg="#1a1a1a")
        
        # 설정 옵션들
        ttk.Label(settings_window, text="🎛️ Dashboard Settings", style='Title.TLabel').pack(pady=20)
        
        # 플랜 선택
        plan_frame = ttk.Frame(settings_window, style='Dark.TFrame')
        plan_frame.pack(fill=tk.X, padx=20, pady=10)
        
        ttk.Label(plan_frame, text="Plan:", style='Dark.TLabel').pack(side=tk.LEFT)
        
        plan_var = tk.StringVar(value=self.current_plan)
        plan_combo = ttk.Combobox(plan_frame, textvariable=plan_var, 
                                 values=["pro", "max5", "max20", "custom"])
        plan_combo.pack(side=tk.RIGHT)
        
        # 토큰 한도 설정
        limit_frame = ttk.Frame(settings_window, style='Dark.TFrame')
        limit_frame.pack(fill=tk.X, padx=20, pady=10)
        
        ttk.Label(limit_frame, text="Daily Limit:", style='Dark.TLabel').pack(side=tk.LEFT)
        
        limit_var = tk.StringVar(value=str(self.daily_limit))
        limit_entry = tk.Entry(limit_frame, textvariable=limit_var, bg="#2d2d2d", fg="white")
        limit_entry.pack(side=tk.RIGHT)
        
        # 저장 버튼
        def save_settings():
            self.current_plan = plan_var.get()
            try:
                self.daily_limit = int(limit_var.get())
                self.limit_value.config(text=f"{self.daily_limit:,} tokens")
                self.add_log(f"⚙️ Settings updated: {self.current_plan} plan, {self.daily_limit:,} limit")
                self.plan_label.config(text=f"💎 Plan: {self.current_plan.title()}")
                settings_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number for token limit")
                
        save_btn = tk.Button(settings_window, text="💾 Save Settings", 
                           command=save_settings,
                           bg="#00d4aa", fg="white", 
                           font=("SF Pro Display", 12, "bold"),
                           relief="flat", padx=20, pady=10)
        save_btn.pack(pady=20)
        
    def open_analytics(self):
        """분석 창 열기"""
        try:
            self.add_log("📊 Opening usage analytics...")
            UsageChartWindow(self.root, self.parser)
        except Exception as e:
            self.add_log(f"❌ Failed to open analytics: {str(e)}")
            messagebox.showerror("Error", f"Failed to open analytics:\n{str(e)}")
        
    def run(self):
        """앱 실행"""
        try:
            self.root.mainloop()
        finally:
            self.is_monitoring = False
            if self.monitor_process:
                self.monitor_process.terminate()

if __name__ == "__main__":
    app = ClaudeDashboard()
    app.run()