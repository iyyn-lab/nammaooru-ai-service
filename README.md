# 1. Clone the repository
git clone <YOUR_REPOSITORY_URL>

# 2. Navigate to the project
cd nammaooru-ai-service

# 3. Create virtual environment
python3 -m venv venv

# 4. Activate virtual environment
source venv/bin/activate

# 5. Install required packages
pip install -r requirements.txt

# 6. Start FastAPI server
uvicorn main:app --reload


Open Swagger UI:

http://localhost:8000/docs