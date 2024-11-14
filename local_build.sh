source C:\\Users\\rodry\\Desktop\\IndexRx\\.venv\\Scripts\\activate
C:\Users\rodry\Desktop\IndexRx\.venv\Scripts\python.exe -m pip install --upgrade pip
pip install -r requirements.txt
rm -rf public
reflex init
reflex export --frontend-only
unzip frontend.zip -d public
rm -f frontend.zip
desactivate