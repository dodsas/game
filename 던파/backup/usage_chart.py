import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
from datetime import datetime, timedelta

class UsageChart:
    def __init__(self, parent, parser):
        self.parent = parent
        self.parser = parser
        
        # Figure 설정 (다크 테마)
        plt.style.use('dark_background')
        self.fig = Figure(figsize=(8, 4), dpi=100, facecolor='#1a1a1a')
        self.ax = self.fig.add_subplot(111, facecolor='#1a1a1a')
        
        # 차트 스타일
        self.ax.spines['bottom'].set_color('#444444')
        self.ax.spines['top'].set_color('#444444')
        self.ax.spines['right'].set_color('#444444')
        self.ax.spines['left'].set_color('#444444')
        self.ax.tick_params(colors='white')
        self.ax.xaxis.label.set_color('white')
        self.ax.yaxis.label.set_color('white')
        
        # 캔버스 생성
        self.canvas = FigureCanvasTkAgg(self.fig, parent)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # 초기 차트 그리기
        self.update_chart()
        
    def update_chart(self):
        """차트 업데이트"""
        try:
            # 사용량 히스토리 가져오기
            history = self.parser.get_usage_history(7)  # 최근 7일
            
            if not history:
                self.draw_no_data_chart()
                return
            
            # 데이터 준비
            dates = [item['date'] for item in history]
            usages = [item['usage'] for item in history]
            percentages = [item['percentage'] for item in history]
            
            # 차트 지우기
            self.ax.clear()
            
            # 라인 차트 그리기
            self.ax.plot(dates, usages, color='#00d4aa', linewidth=3, marker='o', markersize=6)
            
            # 영역 채우기 (그라데이션 효과)
            self.ax.fill_between(dates, usages, alpha=0.3, color='#00d4aa')
            
            # 차트 꾸미기
            self.ax.set_title('📊 Token Usage - Last 7 Days', color='white', fontsize=14, pad=20)
            self.ax.set_xlabel('Date', color='white')
            self.ax.set_ylabel('Tokens Used', color='white')
            
            # Y축 포맷팅 (천 단위 구분)
            self.ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{int(x/1000)}K'))
            
            # X축 날짜 포맷팅
            self.ax.tick_params(axis='x', rotation=45)
            
            # 그리드 추가
            self.ax.grid(True, alpha=0.3, color='#444444')
            
            # 최고/최저 지점 표시
            if len(usages) > 1:
                max_idx = np.argmax(usages)
                min_idx = np.argmin(usages)
                
                self.ax.annotate(f'Peak: {usages[max_idx]:,}', 
                               xy=(max_idx, usages[max_idx]), 
                               xytext=(10, 10), textcoords='offset points',
                               bbox=dict(boxstyle='round,pad=0.5', fc='#00d4aa', alpha=0.8),
                               arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))
            
            # 레이아웃 조정
            self.fig.tight_layout()
            
            # 캔버스 업데이트
            self.canvas.draw()
            
        except Exception as e:
            print(f"Error updating chart: {e}")
            self.draw_error_chart(str(e))
    
    def draw_no_data_chart(self):
        """데이터가 없을 때 차트"""
        self.ax.clear()
        self.ax.text(0.5, 0.5, '📊 No Usage Data Available\n\nStart using Claude to see your usage patterns!', 
                    horizontalalignment='center', verticalalignment='center',
                    transform=self.ax.transAxes, fontsize=12, color='#888888')
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 1)
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.canvas.draw()
    
    def draw_error_chart(self, error_msg):
        """에러 발생시 차트"""
        self.ax.clear()
        self.ax.text(0.5, 0.5, f'❌ Error Loading Chart\n\n{error_msg}', 
                    horizontalalignment='center', verticalalignment='center',
                    transform=self.ax.transAxes, fontsize=12, color='#e74c3c')
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 1)
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.canvas.draw()

class UsageChartWindow:
    def __init__(self, parent, parser):
        self.window = tk.Toplevel(parent)
        self.window.title("📊 Usage Analytics")
        self.window.geometry("900x600")
        self.window.configure(bg="#1a1a1a")
        
        # 헤더
        header_frame = tk.Frame(self.window, bg="#1a1a1a")
        header_frame.pack(fill=tk.X, padx=20, pady=20)
        
        title_label = tk.Label(header_frame, text="📊 Claude Usage Analytics", 
                              bg="#1a1a1a", fg="#00d4aa", 
                              font=("SF Pro Display", 20, "bold"))
        title_label.pack(side=tk.LEFT)
        
        # 새로고침 버튼
        refresh_btn = tk.Button(header_frame, text="🔄 Refresh", 
                               command=self.refresh_chart,
                               bg="#00d4aa", fg="white", 
                               font=("SF Pro Display", 10, "bold"),
                               relief="flat", padx=15, pady=5)
        refresh_btn.pack(side=tk.RIGHT)
        
        # 차트 프레임
        chart_frame = tk.Frame(self.window, bg="#1a1a1a")
        chart_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))
        
        # 차트 생성
        self.chart = UsageChart(chart_frame, parser)
        
        # 통계 정보
        stats_frame = tk.Frame(self.window, bg="#2d2d2d", relief="solid", bd=1)
        stats_frame.pack(fill=tk.X, padx=20, pady=(0, 20))
        
        self.create_stats_display(stats_frame, parser)
    
    def create_stats_display(self, parent, parser):
        """통계 정보 표시"""
        stats_title = tk.Label(parent, text="📈 Weekly Statistics", 
                              bg="#2d2d2d", fg="white", 
                              font=("SF Pro Display", 14, "bold"))
        stats_title.pack(pady=10)
        
        stats_container = tk.Frame(parent, bg="#2d2d2d")
        stats_container.pack(fill=tk.X, padx=20, pady=(0, 15))
        
        try:
            history = parser.get_usage_history(7)
            if history:
                total_usage = sum(item['usage'] for item in history)
                avg_usage = total_usage / len(history)
                max_usage = max(item['usage'] for item in history)
                min_usage = min(item['usage'] for item in history)
                
                stats = [
                    ("Total", f"{total_usage:,} tokens"),
                    ("Average", f"{avg_usage:,.0f} tokens/day"),
                    ("Peak", f"{max_usage:,} tokens"),
                    ("Minimum", f"{min_usage:,} tokens")
                ]
                
                for i, (label, value) in enumerate(stats):
                    stat_frame = tk.Frame(stats_container, bg="#2d2d2d")
                    stat_frame.grid(row=0, column=i, padx=10, sticky="ew")
                    stats_container.grid_columnconfigure(i, weight=1)
                    
                    tk.Label(stat_frame, text=label, bg="#2d2d2d", fg="#888888", 
                            font=("SF Pro Display", 10)).pack()
                    tk.Label(stat_frame, text=value, bg="#2d2d2d", fg="#00d4aa", 
                            font=("SF Pro Display", 12, "bold")).pack()
            
        except Exception as e:
            tk.Label(stats_container, text=f"Error loading statistics: {e}", 
                    bg="#2d2d2d", fg="#e74c3c", 
                    font=("SF Pro Display", 10)).pack()
    
    def refresh_chart(self):
        """차트 새로고침"""
        self.chart.update_chart()

if __name__ == "__main__":
    # 테스트용
    root = tk.Tk()
    root.withdraw()
    
    from claude_monitor_parser import ClaudeMonitorParser
    parser = ClaudeMonitorParser()
    
    chart_window = UsageChartWindow(root, parser)
    root.mainloop()