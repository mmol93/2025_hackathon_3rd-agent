"""베이비시터 AI 에이전트 - ADK 공식 패턴"""

import vertexai
from vertexai import agent_engines

from babysitter_agent.config import Config
from babysitter_agent.tools.babysitter_tools import BABY_TOOLS

class BabysitterAgent:
    """베이비시터 AI 에이전트"""

    def __init__(self):
        """에이전트 초기화"""
        self.config = Config()
        self.tools = BABY_TOOLS
        self.agent = None
        self._initialize_vertexai()

    def _initialize_vertexai(self):
        """Vertex AI 초기화"""
        try:
            vertexai.init(
                project=self.config.PROJECT_ID,
                location=self.config.LOCATION,
                staging_bucket=self.config.STAGING_BUCKET
            )
            print("✅ Vertex AI 초기화 완료")
        except Exception as e:
            print(f"❌ Vertex AI 초기화 실패: {e}")
            raise

    def create_agent(self):
        """LangGraph 에이전트 생성 - 원래 방식대로"""
        try:
            self.agent = agent_engines.LanggraphAgent(
                model=self.config.MODEL_NAME,
                tools=self.tools,
            )

            print(f"✅ LangGraph 에이전트 생성 완료 (모델: {self.config.MODEL_NAME})")
            print(f"   등록된 툴 수: {len(self.tools)}")

            return self.agent

        except Exception as e:
            print(f"❌ 에이전트 생성 실패: {e}")
            raise

    def deploy_agent(self):
        """Vertex AI에 에이전트 배포"""
        print("🚀 에이전트 배포 시작...")

        if not self.agent:
            self.agent = self.create_agent()

        try:
            requirements = [
                "google-cloud-aiplatform[agent_engines,adk,langchain,ag2,llama_index]>=1.108.0",
                "python-dotenv"
            ]
            extra_packages = ["babysitter_agent"]

            remote_agent = agent_engines.create(
                self.agent,  # LanggraphAgent 객체
                requirements=requirements,
                display_name="BabySitterAgent",
                extra_packages=extra_packages,
                description="베이비시터 AI 에이전트 - 육아 상담 및 조언 제공"
            )

            print("✅ 배포 완료!")
            print(f"📋 리소스 이름: {remote_agent.resource_name}")

            return remote_agent

        except Exception as e:
            print(f"❌ 배포 실패: {e}")
            raise

if __name__ == "__main__":
    print(BabysitterAgent().create_agent().query(input={"messages": [
                ("user", "What is the exchange rate from US dollars to Swedish currency?"),
            ]}))