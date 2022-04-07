runs on resolution 1920 * 1080
## Install requirment using command:
sudo pip3 install -r requirements.txt

To enable DB

Change the path 
app.config['SQLALCHEMY_DATABASE_URI'] in __init__.py line 11

Comment line -- from login import routes inside --init--.py
database setuped on rds aws.
with the static table of  test_details with data-
# test_data1 = test_details(test_uid='BRACA001',test_name='Breast Cancer test',test_cover='12 parameters Covered',test_desc ='Online report and consulting', test_avail='Daily available',test_repo='Confidential Reports',test_price='899.00')
# test_data2 = test_details(test_uid='BRACA002',test_name='Breast Cancer test',test_cover='9 parameters Covered',test_desc ='Online report and consulting', test_avail='Daily available',test_repo='Confidential Reports',test_price='599.00')
  
And run the project
python3 run.py

to add Static path for image

add uploaded(name) folder in static(name) folder
