"""베이비시터 AI 에이전트 설정"""

import os
from pathlib import Path
from dotenv import load_dotenv

# .env 파일 로드 (패키지 내부에서)
env_path = Path(__file__).parent / '.env'
load_dotenv(env_path)


class Config:
    """에이전트 설정 클래스"""

    PROJECT_ID: str = os.getenv("GOOGLE_CLOUD_PROJECT")
    LOCATION: str = os.getenv("VERTEX_AI_LOCATION")
    STAGING_BUCKET: str = os.getenv("STAGING_BUCKET")
    MODEL_NAME: str = "gemini-2.0-flash"

    def __init__(self):
        """설정 검증"""
        if not self.PROJECT_ID or self.PROJECT_ID == "your-project-id":
            raise ValueError("GOOGLE_CLOUD_PROJECT 환경변수를 설정해주세요")
        if not self.STAGING_BUCKET or "your-bucket" in self.STAGING_BUCKET:
            raise ValueError("STAGING_BUCKET 환경변수를 설정해주세요")

    def display_config(self):
        """현재 설정 출력"""
        print(f"✅ 프로젝트: {self.PROJECT_ID}")
        print(f"✅ 리전: {self.LOCATION}")
        print(f"✅ 스테이징 버킷: {self.STAGING_BUCKET}")
        print(f"✅ 모델: {self.MODEL_NAME}")
