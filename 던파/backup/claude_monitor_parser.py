import os
import json
import subprocess
import re
from datetime import datetime
from pathlib import Path

class ClaudeMonitorParser:
    def __init__(self):
        self.config_dir = Path.home() / ".config" / "claude-monitor"
        self.data_file = self.config_dir / "usage_data.json"
        self.log_file = self.config_dir / "monitor.log"
        
    def get_current_usage(self):
        """현재 토큰 사용량을 가져옵니다"""
        try:
            # claude-monitor의 상태를 JSON으로 가져오기
            result = subprocess.run([
                "claude-monitor", "--format", "json"
            ], capture_output=True, text=True, timeout=5)
            
            if result.returncode == 0:
                data = json.loads(result.stdout)
                return data
            else:
                # JSON 형식이 지원되지 않는 경우 텍스트 파싱
                return self.parse_text_output()
                
        except (subprocess.TimeoutExpired, json.JSONDecodeError, FileNotFoundError):
            return self.parse_from_logs()
    
    def parse_text_output(self):
        """텍스트 출력에서 정보 파싱"""
        try:
            result = subprocess.run([
                "claude-monitor", "--no-clear"
            ], capture_output=True, text=True, timeout=3)
            
            if result.returncode != 0:
                return self.get_default_data()
                
            output = result.stdout
            
            # 토큰 사용량 정보 추출
            usage_data = {
                "current_usage": 0,
                "daily_limit": 1000000,
                "plan": "custom",
                "reset_time": None,
                "last_updated": datetime.now().isoformat()
            }
            
            # 패턴 매칭으로 정보 추출
            patterns = {
                "usage": r"Usage[:\s]+([0-9,]+)\s*tokens",
                "limit": r"Limit[:\s]+([0-9,]+)\s*tokens",
                "plan": r"Plan[:\s]+(\w+)",
                "percentage": r"([0-9.]+)%"
            }
            
            for key, pattern in patterns.items():
                match = re.search(pattern, output, re.IGNORECASE)
                if match:
                    value = match.group(1)
                    if key in ["usage", "limit"]:
                        usage_data[f"current_{key}" if key == "usage" else f"daily_{key}"] = int(value.replace(",", ""))
                    elif key == "plan":
                        usage_data[key] = value.lower()
                        
            return usage_data
            
        except Exception as e:
            print(f"Error parsing text output: {e}")
            return self.get_default_data()
    
    def parse_from_logs(self):
        """로그 파일에서 정보 파싱"""
        try:
            if self.log_file.exists():
                with open(self.log_file, 'r') as f:
                    lines = f.readlines()
                    
                # 최근 로그에서 사용량 정보 찾기
                for line in reversed(lines[-50:]):  # 최근 50줄만 확인
                    if "tokens" in line.lower():
                        # 로그에서 토큰 정보 추출
                        numbers = re.findall(r'[0-9,]+', line)
                        if numbers:
                            usage = int(numbers[0].replace(',', ''))
                            return {
                                "current_usage": usage,
                                "daily_limit": 1000000,
                                "plan": "custom",
                                "last_updated": datetime.now().isoformat()
                            }
        except Exception as e:
            print(f"Error reading log file: {e}")
            
        return self.get_default_data()
    
    def get_default_data(self):
        """기본 데이터 반환"""
        return {
            "current_usage": 0,
            "daily_limit": 1000000,
            "plan": "custom",
            "usage_rate": 0.0,
            "remaining": 1000000,
            "last_updated": datetime.now().isoformat(),
            "status": "disconnected"
        }
    
    def get_usage_history(self, days=7):
        """최근 N일간의 사용량 히스토리"""
        history = []
        
        # 실제 구현에서는 저장된 히스토리 데이터를 읽어옵니다
        # 여기서는 샘플 데이터를 생성합니다
        import random
        from datetime import timedelta
        
        for i in range(days):
            date = datetime.now() - timedelta(days=i)
            usage = random.randint(50000, 800000)
            history.append({
                "date": date.strftime("%Y-%m-%d"),
                "usage": usage,
                "percentage": (usage / 1000000) * 100
            })
            
        return list(reversed(history))
    
    def save_usage_data(self, data):
        """사용량 데이터 저장"""
        try:
            self.config_dir.mkdir(parents=True, exist_ok=True)
            
            # 기존 데이터 로드
            existing_data = []
            if self.data_file.exists():
                with open(self.data_file, 'r') as f:
                    existing_data = json.load(f)
            
            # 새 데이터 추가
            data['timestamp'] = datetime.now().isoformat()
            existing_data.append(data)
            
            # 최근 1000개 항목만 유지
            if len(existing_data) > 1000:
                existing_data = existing_data[-1000:]
            
            # 저장
            with open(self.data_file, 'w') as f:
                json.dump(existing_data, f, indent=2)
                
        except Exception as e:
            print(f"Error saving usage data: {e}")

if __name__ == "__main__":
    # 테스트
    parser = ClaudeMonitorParser()
    data = parser.get_current_usage()
    print(json.dumps(data, indent=2))