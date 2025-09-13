python -m venv venv
venv\Scripts\activate
pip install -e .
python .\pipeline\build_pipeline.py
streamlit run .\app\app.py