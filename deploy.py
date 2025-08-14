from babysitter_agent.agent import BabysitterAgent


def main():
    print("=" * 60)
    print("🍼 베이비시터 AI 에이전트 배포 (ADK 공식 패턴)")
    print("=" * 60)

    try:
        # ADK 패턴 에이전트 초기화
        babysitter = BabysitterAgent()

        # 배포 실행
        remote_agent = babysitter.deploy_agent()

        print("\n" + "=" * 60)
        print("🎉 ADK 패턴 배포 성공!")
        print("=" * 60)
        print(f"📋 리소스 이름: {remote_agent.resource_name}")

        # 배포 후 테스트
        print("\n🧪 배포 후 테스트 실행...")
        test_response = remote_agent.query(
            input={"messages": [
                ("user", "8ヶ月の男の子、体重8.5kgですが、健康状態とおすすめ活動を教えてください")
            ]}
        )
        print(f"✅ テスト応答: {test_response}")

        print("\n📖 次のステップ:")
        print("   1. Flutter アプリでこのリソース名を使ってAPI呼び出し")
        print("   2. python test.py で詳細テスト実行")
        print("   3. GCP コンソールで Vertex AI > Agent Engine 확인")

    except Exception as e:
        print(f"\n❌ 배포 실패: {e}")
        print("\n🔍 해결 방법:")
        print("   1. babysitter_agent/.env 파일의 환경변수 확인")
        print("   2. gcloud auth application-default login 실행")
        print("   3. Cloud Storage 버킷 존재 확인")
        print("   4. Vertex AI API 활성화 확인")
        exit(1)


if __name__ == "__main__":
    main()
