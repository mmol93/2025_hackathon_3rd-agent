from dotenv import load_dotenv
import os
import subprocess
import vertexai
from vertexai import agent_engines

load_dotenv()

project_from_env = os.getenv("GOOGLE_CLOUD_PROJECT")

print(f"환경 변수 기반 프로젝트: {project_from_env}")

# gcloud CLI로 현재 설정 확인
try:
    project_from_gcloud = subprocess.check_output(["gcloud", "config", "get-value", "project"]).decode().strip()
    print(f"gcloud 기반 프로젝트: {project_from_gcloud}")
    print("✅ gcloud에서 현재 선택되어있는 프로젝트 확인 완료")
except Exception as e:
    print(f"❌ gcloud 확인 에러: {e}")

# Vertex AI 초기화 (필요 시 재설정)
vertexai.init(
    project="endless-fire-468401-f8",  # 이전 대화의 프로젝트 ID
    location="us-west1"  # 이전 대화의 위치
)
print("✅ Vertex AI 초기화 완료 (설정 값은 위에서 확인하세요)")

try:
    agents = list(agent_engines.list())  # list()로 변환
    print(f"\n현재 배포되어 있는 전체 에이전트 수: {len(agents)}")
    if len(agents) == 0:
        print("❌ 여전히 빈 목록입니다. 아래 원인을 확인하세요.")
    else:
        for agent in agents:
            print(f"- 이름: {agent.display_name}")
            print(f"  리소스: {agent.resource_name}")
            print("---")
except Exception as e:
    print(f"❌ 조회 에러: {e}")

agent = agent_engines.get("5580980285102620672")

# 응답 출력
response = agent.query(
    input={"messages": [
        ("user", "8ヶ月の男の子、体重8.5kgですが、健康状態とおすすめ活動を教えてください")
    ]}
)


# 응답에서 최종 답변(content)과 사용된 툴 추출
def extract_final_content_and_tools(response):
    final_content = "답변 없음"
    used_tools = []  # 사용된 툴 목록 (이름, ID, 결과)

    # 응답이 dict 형식이라고 가정 (이전 데이터처럼 {'messages': [...]})
    if isinstance(response, dict) and 'messages' in response:
        messages = response['messages']

        # 툴 메시지 추출 (ToolMessage 타입)
        for msg in messages:
            if msg.get('type') == 'constructor' and msg['kwargs'].get('type') == 'tool':
                tool_info = {
                    'name': msg['kwargs'].get('name'),
                    'tool_call_id': msg['kwargs'].get('tool_call_id'),
                    'result': msg['kwargs'].get('content')
                }
                used_tools.append(tool_info)

        # 마지막 AI 메시지에서 최종 content 추출
        for msg in reversed(messages):  # 마지막부터 검색
            if msg.get('type') == 'constructor' and msg['kwargs'].get('type') == 'ai':
                final_content = msg['kwargs'].get('content', "답변 없음")
                break

    # 또는 응답 객체에 직접 접근 (SDK에 따라 다름)
    elif hasattr(response, 'output'):
        final_content = response.output
        # 툴 정보는 SDK 객체에서 별도로 추출 (필요 시 response.tool_calls 등 확인)

    return final_content, used_tools


# 추출 및 출력
final_answer, tools_used = extract_final_content_and_tools(response)

print("추출된 최종 답변:")
print(final_answer)

print("\n사용된 툴 정보:")
if not tools_used:
    print("사용된 툴 없음")
else:
    for tool in tools_used:
        print(f"- 툴 이름: {tool['name']}")
        print(f"  호출 ID: {tool['tool_call_id']}")
        print(f"  결과: {tool['result']}")
        print("---")
