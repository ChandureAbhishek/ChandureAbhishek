from flask import Flask, url_for, render_template, request, redirect, make_response, jsonify
# from flask_cors import CORS, cross_origin
from application import app
# from application import models




@app.route('/', methods=['GET', 'POST'])  # To render Homepage
def home_page():
    return render_template('index-v4.html')


@app.route('/index.html', methods=['GET', 'POST'])  # To render Homepage
def home_page1():
    return render_template('index-v4.html')

# To render about us page


@app.route('/about-us.html', methods=['GET', 'POST'])
def about():
    return render_template('about-us.html')


# To render technology-as-force-multiperil
@app.route('/technology-as-force-multiperil.html', methods=['GET', 'POST'])
def technology_as_force_multiperil():
    return render_template('technology-as-force-multiperil.html')


# To render end-to-end-fda-implementation.html
@app.route('/end-to-end-fda-implementation.html', methods=['GET', 'POST'])
def end_to_end_fda_implimentation():
    return render_template('end-to-end-fda-implementation.html')


# To render team
@app.route('/team.html', methods=['GET', 'POST'])
def team():
    return render_template('team.html')

# To render in-vitro


@app.route('/in-vitro.html', methods=['GET', 'POST'])
def in_vitro():
    return render_template('in-vitro.html')


# To render in-vivo
@app.route('/in-vivo.html', methods=['GET', 'POST'])
def in_vivo():
    return render_template('in-vivo.html')


# To render meta-stage-of-organ-on-a-chip
@app.route('/meta-stage-of-organ-on-a-chip.html', methods=['GET', 'POST'])
def meta_stage_of_organ_on_a_chip():
    return render_template('meta-stage-of-organ-on-a-chip.html')

# To render phase


@app.route('/phase.html', methods=['GET', 'POST'])
def phase():
    return render_template('phase-i.html')


# To render phase-i
@app.route('/phase-i.html', methods=['GET', 'POST'])
def phase_i():
    return render_template('phase-i.html')


# To render phase-ii
@app.route('/phase-ii.html', methods=['GET', 'POST'])
def phase_ii():
    return render_template('phase-ii.html')


# To render phase-iii
@app.route('/phase-iii.html', methods=['GET', 'POST'])
def phase_iii():
    return render_template('phase-iii.html')


# To render phase-iv
@app.route('/phase-iv.html', methods=['GET', 'POST'])
def phase_iv():
    return render_template('phase-iv.html')

# To render pmcf


@app.route('/pmcf.html', methods=['GET', 'POST'])
def pmcf():
    return render_template('pmcf.html')

# To render pms


@app.route('/pms.html', methods=['GET', 'POST'])
def pms():
    return render_template('pms.html')

# To render pharmacovigilance


@app.route('/pharmacovigilance.html', methods=['GET', 'POST'])
def pharmacovigilance():
    return render_template('pharmacovigilance.html')


# To render clinical-data-management
@app.route('/clinical-data-management.html', methods=['GET', 'POST'])
def clinical_data_management():
    return render_template('clinical-data-management.html')


# To render clinical-study-management
@app.route('/clinical-study-management.html', methods=['GET', 'POST'])
def clinical_study_management():
    return render_template('clinical-study-management.html')


# To render medical-and-scientific-writing
@app.route('/medical-and-scientific-writing.html', methods=['GET', 'POST'])
def medical_and_scientific_writing():
    return render_template('medical-and-scientific-writing.html')


# To render medical-monitoring
@app.route('/medical-monitoring.html', methods=['GET', 'POST'])
def medical_monitoring():
    return render_template('medical-monitoring.html')


# To render patient recruitment
@app.route('/patient-recruitment.html', methods=['GET', 'POST'])
def patient_recruitment():
    return render_template('patient-recruitment.html')


# To render site recruitment
@app.route('/site-recruitment.html', methods=['GET', 'POST'])
def site_recruitment():
    return render_template('site-recruitment.html')


# To render site management
@app.route('/site-management.html', methods=['GET', 'POST'])
def site_management():
    return render_template('site-management.html')


# To render project-management
@app.route('/project-management.html', methods=['GET', 'POST'])
def project_management():
    return render_template('project-management.html')


# To render Biostatistics
@app.route('/biostatistics.html', methods=['GET', 'POST'])
def biostatistics():
    return render_template('biostatistics.html')


# To render sites
@app.route('/sites.html', methods=['GET', 'POST'])
def sites():
    return render_template('sites.html')


# To render kiosk based trial page
@app.route('/kiosk-based-trial-enrollment.html', methods=['GET', 'POST'])
def kiosk_based_trial_enrollment():
    return render_template('kiosk-based-trial-enrollment.html')


# To render ai-for-augmenting-clinical-trials page
@app.route('/ai-for-augmenting-clinical-trials.html', methods=['GET', 'POST'])
def ai_for_augmenting_clinical_trials():
    return render_template('ai-for-augmenting-clinical-trials.html')


# To render career page
@app.route('/careers.html', methods=['GET', 'POST'])
def careers():
    return render_template('careers.html')

# To render contact-us page


@app.route('/contact-us.html', methods=['GET', 'POST'])
def contact_us():
    return render_template('contact-us.html')




# def login():
#     try:
#         phone = request.form.get('phone')
#         password = request.form.get('password')
#         user_loging = models.user.query.filter_by(phone=phone).first()
#         uid = user_loging.uid
#         user_type = user_loging.user_type
#         if (user_loging == None):
#             raise Exception("Unauthorised user.")
#         elif (password == user_loging.password):
#             print("verified login")
#             models.login_user(user_loging)
#         else:
#             raise Exception("Incorrect Password.")


#     except Exception as msg:
#         print("[ERROR] unable to fetch login creds : " + str(msg))
#         data = {'message': "[ERROR] unable to fetch login creds : " + str(msg), 'status': False}
#         resp = jsonify(data)
#         resp.status_code = 200
#         return resp

#     data = {'message': 'Request recieved sucessfully', 'status': True, 'uid': uid, 'user_type': user_type}
#     resp = jsonify(data)
#     resp.status_code = 200
#     return resp



# @app.route('/savesignupdata', methods=['POST'])
# def savesignupdata():
#     email=request.form.get('email')
#     pannumber=request.form.get('pannumber')
#     print(email,pannumber)
#     try:
#         user_det = user.query.filter_by(email =  email).first()
#         if(user_det != None and user_det.password == password):
#             print("verified login")
#             login_user(user_det)
#         else:
#             raise Exception("Invalid Credentials")

#     except Exception as msg:
#         print("[ERROR] in login :" + str(msg))
#         data= {'message' : '[ERROR] in login : Invalid credentials', 'status': False}
#         resp= jsonify(data)
#         resp.status_code= 200
#         return resp
#     data= {'message' : 'Successful login', 'status': True}
#     resp = jsonify(data)
#     resp.status_code = 200
#     return resp