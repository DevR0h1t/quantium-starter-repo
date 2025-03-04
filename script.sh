source .venv/Scripts/activate
python -m pytest test_app.py
test_status=$?

if [ $test_status -eq 0 ]
then
    exit 0
else 
    exit 1
fi
