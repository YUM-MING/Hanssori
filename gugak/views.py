import os
import json
import requests
from dotenv import load_dotenv
from datetime import datetime
from collections import Counter

from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_time

from openai import OpenAI
from .models import EmotionRecord, ChatLog, DailySummary


from django.shortcuts import render
from .recommend_engine import recommend_from_text
import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 현재 위치: gugak/
METADATA_PATH = os.path.join(BASE_DIR, 'static', 'gugak_metadata.csv')
df = pd.read_csv(METADATA_PATH)

def index(request):
    return render(request, 'index.html')

def recommend_view(request):
    user_input = request.GET.get('query', '')
    results = recommend_from_text(user_input) if user_input else []
    return render(request, 'gugak/recommend.html', {'query': user_input, 'results': results})

# views.py
from django.shortcuts import render
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
import json
import os


# 🎯 feature columns (실제 csv 컬럼에 맞게 수정됨)
feature_cols = ['템포', '곡길이', '시김새 개수']

# 🎵 플레이리스트 추천 뷰
def playlist_view(request):
    recent_json = request.GET.get('recent')  # localStorage에서 가져온 recentTracks JSON
    if not recent_json:
        return render(request, 'gugak/playlist.html', {'playlist': [], 'error': '최근 들은 곡이 없습니다.'})

    try:
        recent_tracks = json.loads(recent_json)
    except:
        return render(request, 'gugak/playlist.html', {'playlist': [], 'error': 'recent 파라미터 오류'})

    # 🔍 최근 곡들의 feature 평균 벡터 계산
    filenames = [track['filename'] for track in recent_tracks]
    recent_df = df[df['파일명'].isin(filenames)]

    if recent_df.empty:
        return render(request, 'gugak/playlist.html', {'playlist': [], 'error': '메타데이터에 곡 정보가 없습니다.'})

    # 💡 수치형 데이터 결측치 처리 (예방 차원)
    recent_df = recent_df[feature_cols].dropna()
    recent_vec = recent_df.mean().values.reshape(1, -1)

    # 🎯 전체 곡들과의 코사인 유사도 계산
    all_data = df.dropna(subset=feature_cols)  # 전체 데이터에서 feature 결측 제거
    all_vectors = all_data[feature_cols].values
    similarities = cosine_similarity(recent_vec, all_vectors)[0]

    all_data = all_data.copy()
    all_data['similarity'] = similarities
    top_songs = all_data.sort_values(by='similarity', ascending=False).head(10)

    results = []
    for _, row in top_songs.iterrows():
        results.append({
            'title': row['곡명'],
            'filename': row['파일명'],
            'tempo': row['템포'],
            'instrument': row['악기'],
            'sigimsae': row.get('시김새 목록', '정보 없음'),
        })

    return render(request, 'gugak/playlist.html', {'playlist': results})

# ✅ 환경 변수 로딩
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ✅ KoBERT 감정 분석 API 설정
KOBERT_API_URL = "https://dat-feet-valley-notified.trycloudflare.com"
valid_labels = {'기쁨', '당황', '분노', '불안', '상처', '슬픔'}
emotion_aliases = {
    '화남': '분노', '짜증': '분노', '우울': '슬픔', '놀람': '당황',
    '공포': '불안', '행복': '기쁨', '분노 ': '분노',
    '불안감': '불안', 'unknown': '알 수 없음'
}

# ✅ 감정 라벨 매핑 함수
def map_emotion(label):
    cleaned = label.strip()
    mapped = emotion_aliases.get(cleaned, cleaned)
    return mapped if mapped in valid_labels else '알 수 없음'

# ✅ KoBERT 감정 분석 함수
def analyze_sentiment_kobert(text):
    try:
        res = requests.post(KOBERT_API_URL, json={"text": text})
        if res.status_code == 200:
            label = res.json().get("label", "unknown")
            emotion = map_emotion(label)
            print("🧪 KoBERT 응답:", emotion)
            return emotion
        else:
            print("❌ KoBERT 오류 응답:", res.status_code)
            return "알 수 없음"
    except Exception as e:
        print("❌ KoBERT 요청 실패:", e)
        return "알 수 없음"

# ✅ 상태 변수 (비회원용 히스토리 저장용)
chat_history = []
emotion_history = []
current_summary = ""

# ✅ 메인 페이지
def index(request):
    return render(request, "gugak/index.html")

def register(request):
    return render(request, 'gugak/register.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.http import JsonResponse

# 회원가입
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('/')  # 이미 로그인된 사용자는 홈으로

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "회원가입 완료! 로그인해주세요.")
            return redirect('/')
        else:
            messages.error(request, "회원가입 실패.")
    else:
        print(form.errors)
        form = UserCreationForm()

    return render(request, 'gugak/register.html', {'form': form})

# 로그인
def login_view(request):
    if request.user.is_authenticated:
        # 로그인된 상태에서 다시 로그인 요청시 JSON 또는 redirect
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'status': 'already_logged_in'})
        return redirect('/')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # ✅ Ajax 요청일 경우 JSON 응답
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'status': 'success'})
            return redirect('/')
        else:
            print("❌ 로그인 실패")
            print("입력값 username:", request.POST.get('username'))
            print("입력값 password:", request.POST.get('password'))
            print("form.errors:", form.errors)
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'status': 'fail', 'errors': form.errors})
    
            messages.error(request, "로그인 실패. 아이디와 비밀번호를 확인해주세요.")
    else:
        form = AuthenticationForm()

    return JsonResponse({'status': 'error', 'message': 'GET 요청은 허용되지 않음'}, status=405)

# 로그아웃
def logout_view(request):
    logout(request)
    messages.info(request, "로그아웃.")
    return redirect('/')
