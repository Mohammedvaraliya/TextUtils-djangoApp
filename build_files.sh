# build_files.sh
echo " BUILD START"
python pip install django
python manage.py collectstatic
echo " BUILD END"