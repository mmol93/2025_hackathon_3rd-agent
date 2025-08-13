"""베이비시터 AI 툴 모음"""

def baby_recommendation(age: int) -> str:
    """아기 나이별 맞춤 활동과 놀이를 추천하는 툴입니다.

    사용 시기:
    - 사용자가 "무엇을 하면 좋을지" 질문할 때
    - "놀이 추천", "활동 추천" 요청할 때
    - "우리 아기 나이에 맞는 것" 물어볼 때
    - "발달에 도움되는 것" 궁금해할 때

    예시 질문: "6개월 아기 놀이 추천해줘", "10개월 아기가 하면 좋은 활동은?"

    Args:
        age: 아기 나이 (개월 수, 0-36개월 범위)

    Returns:
        해당 나이에 적합한 발달 활동과 놀이 추천
    """
    if age < 0:
        return "正しい年齢を入力してください。"
    elif age <= 3:
        return "0-3ヶ月: 毎日のスキンシップと授乳ルーティンをお勧めします。優しい音楽を聞かせ、赤ちゃんとアイコンタクトを頻繁に取ってください。"
    elif age <= 6:
        return "4-6ヶ月: 首座りと寝返りの練習を手伝ってください。ガラガラやカラフルなおもちゃで視覚・聴覚刺激を与えてください。"
    elif age <= 9:
        return "7-9ヶ月: 離乳食導入と座る練習を始めてください。安全な空間でハイハイを促してください。"
    elif age <= 12:
        return "10-12ヶ月: つかまり立ちと歩行の準備をしてください。簡単な言葉（ママ、パパ）を教えてみてください。"
    elif age <= 18:
        return "13-18ヶ月: 言語発達のために本をたくさん読み聞かせ、ブロック遊びで細かい筋肉の発達を手伝ってください。"
    elif age <= 24:
        return "19-24ヶ月: トイレトレーニングを開始し、お絵描きや塗り絵で創造性を育ててください。"
    else:
        return f"{age}ヶ月: 年齢に適した社会性発達と言語能力向上に集中してください。同年代の友達との遊び時間を増やしてみてください。"

def baby_weight_check(weight: float, age: int, gender: str = "男の子") -> str:
    """아기 몸무게와 나이를 분석해 건강 팁을 반환하는 툴입니다.

    사용 시기:
    - 사용자가 "몸무게가 정상인지" 궁금해할 때
    - "건강 상태 체크" 요청할 때
    - "영양 상태" 또는 "성장 발달" 질문할 때
    - "우리 아기 키/몸무게" 관련 상담할 때

    예시 질문: "8개월 아기 몸무게 8kg 정상인가요?", "몸무게 체크해주세요"

    Args:
        weight: 아기 현재 몸무게 (kg)
        age: 아기 나이 (개월 수)
        gender: 성별 ("男の子" 또는 "女の子")

    Returns:
        몸무게 분석 결과와 맞춤 영양/건강 조언
    """
    if weight <= 0 or age < 0:
        return "正しい体重と年齢を入力してください。"

    # 간단한 평균 몸무게 계산 (실제로는 더 정교한 성장차트 사용)
    if age <= 6:
        average_weight = 3.5 + (age * 0.7)  # 신생아 기준
    else:
        average_weight = 7.5 + ((age - 6) * 0.3)  # 6개월 이후

    # 성별에 따른 조정
    if gender == "男の子":
        average_weight *= 1.05
    else:
        average_weight *= 0.98

    weight_ratio = weight / average_weight

    if weight_ratio < 0.85:
        return f"体重が平均より低いです（現在: {weight}kg、平均: {average_weight:.1f}kg）。栄養バランスの取れた食事を増やし、小児科医に相談してみてください。母乳育児や粉ミルクの量を確認し、必要に応じて栄養補助食品を検討してください。"
    elif weight_ratio > 1.2:
        return f"体重が平均より高いです（現在: {weight}kg、平均: {average_weight:.1f}kg）。適切な活動量を増やし、定期検診を受けてください。過度な粉ミルクや間食の摂取を調整し、発達に合った運動をさせてください。"
    else:
        return f"体重が正常範囲です（現在: {weight}kg、平均: {average_weight:.1f}kg）。現在の栄養管理を継続し、継続的な成長観察を維持してください。定期的な小児科検診もお忘れなく。"

def baby_sleep_advice(age: int, sleep_hours: float) -> str:
    """아기 나이별 수면 패턴 조언을 제공하는 툴입니다.

    사용 시기:
    - 사용자가 "수면 문제" 또는 "잠" 관련 질문할 때
    - "밤에 안 잔다", "낮잠이 짧다" 등 수면 고민 상담할 때
    - "수면 시간이 적절한지" 궁금해할 때
    - "수면 루틴" 또는 "잠자리 습관" 조언 요청할 때

    예시 질문: "아기가 밤에 안 자요", "6개월 아기 수면 시간 적절한가요?"

    Args:
        age: 아기 나이 (개월 수)
        sleep_hours: 하루 평균 수면 시간

    Returns:
        나이별 권장 수면 시간과 수면 패턴 개선 조언
    """
    if age < 0 or sleep_hours < 0:
        return "正しい年齢と睡眠時間を入力してください。"

    # 나이별 권장 수면 시간
    if age <= 3:
        recommended_sleep = 16  # 16-17시간
        advice = "新生児はよく目を覚まして授乳するのが正常です。"
    elif age <= 6:
        recommended_sleep = 14  # 14-15시간
        advice = "睡眠パターンが少しずつ規則的に変わる時期です。"
    elif age <= 12:
        recommended_sleep = 13  # 13-14시간
        advice = "夜泣きと昼寝の区別が明確になる時期です。"
    elif age <= 18:
        recommended_sleep = 12.5  # 12-13시간
        advice = "昼寝の回数が減り、夜泣きが長くなります。"
    else:
        recommended_sleep = 12  # 11-12시간
        advice = "規則的な睡眠スケジュールの確立が重要です。"

    if sleep_hours < recommended_sleep - 2:
        return f"睡眠時間が不足している可能性があります（現在: {sleep_hours}時間、推奨: {recommended_sleep}時間）。{advice} 睡眠環境をチェックし、ルーティンを作ってみてください。"
    elif sleep_hours > recommended_sleep + 2:
        return f"睡眠時間が多い可能性があります（現在: {sleep_hours}時間、推奨: {recommended_sleep}時間）。{advice} 起きている時間の活動量を増やしてみてください。"
    else:
        return f"適切な睡眠を取っています（現在: {sleep_hours}時間、推奨: {recommended_sleep}時間）。{advice} 現在のパターンを維持してください。"

# Vertex AI Agent Engine에서 사용할 툴 목록
BABY_TOOLS = [
    baby_recommendation,
    baby_weight_check,
    baby_sleep_advice
]
