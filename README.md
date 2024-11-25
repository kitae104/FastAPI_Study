# FastAPI Study
### 시작하기 
1. 가상 환경 만들기
python -m venv fastapi

2. 가상환경 활성화하기
fastapi\Scripts\activate.bat

3. 패키지 설치 
pip install fastapi
pip install "uvicorn[standard]"

4. 프로젝트 실행(main.py 일 경우)
uvicorn main:app --port 8080 --reload