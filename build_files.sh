# build_files.sh
echo " BUILD START"
python3.11 pip install -r requirements.txt
python3.11 manage.py collectstatic --noinput --clear
echo " BUILD END"