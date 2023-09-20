from flask import render_template, request, flash, redirect, url_for
from app import app, db, socketio
from app.models import User,employee, late, leave
#from flask_login import login_user, login_required, logout_user, current_user
import json
from sqlalchemy.sql import func
from .controller import * 
from flask_socketio import emit
from sqlalchemy import desc
# Your route handlers and SocketIO events go here
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/late_form_page')
def late_form_page():
    return render_template('emp_late.html')


@app.route('/leave_form_page')
def leave_form_page():
    return render_template('emp_leave.html')


@socketio.on('connect')
def handle_connect():
    print('Client Connected')


@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')    

@app.route('/late_approve',methods=['POST','GET'])
def late_approve():
    user = json.loads(request.data)
    userID = user['userId']
    user = late.query.filter_by(emp_id=userID).first()
    print(" USER : ",user)
    current_user='hr'
    if current_user=='hr':
        user.hr_approval='Approved'
        user.status='Approved'
        db.session.commit()
        print("Hr Approval ", user.hr_approval)
        print("Status ", user.status)
        emit('late_hr_approval_update', {'userId': userID, 'hr_approval': user.hr_approval}, broadcast=True)

@app.route('/leave_approve',methods=['POST','GET'])
def leave_approve():
    user = json.loads(request.data)
    userID = user['userId']
    user = leave.query.filter_by(emp_id=userID).first()
    print(" USER : ",user)
    current_user='hr'
    if current_user=='hr':
        user.hr_approval='Approved'
        user.status='Approved'
        db.session.commit()
        print("Hr Approval ", user.hr_approval)
        print("Status ", user.status)
        emit('leave_hr_approval_update', {'userId': userID, 'hr_approval': user.hr_approval}, broadcast=True)

@app.route('/late_decline',methods=['POST','GET'])
def late_decline():
    user = json.loads(request.data)
    userID = user['userId']
    user = late.query.filter_by(emp_id=userID).first()
    print(" USER : ",user)
    current_user='hr'
    if current_user=='hr':
        user.hr_approval='Declined'
        user.status='Declined'
        db.session.commit()
        print("Hr Approval ", user.hr_approval)
        print("Status ", user.status)
        emit('late_hr_approval_update', {'userId': userID, 'hr_approval': user.hr_approval}, broadcast=True)

@app.route('/leave_decline',methods=['POST','GET'])
def leave_decline():
    user = json.loads(request.data)
    userID = user['userId']
    user = leave.query.filter_by(emp_id=userID).first()
    print(" USER : ",user)
    current_user='hr'
    if current_user=='hr':
        user.hr_approval='Declined'
        user.status='Declined'
        db.session.commit()
        print("Hr Approval ", user.hr_approval)
        print("Status ", user.status)
        emit('leave_hr_approval_update', {'userId': userID, 'hr_approval': user.hr_approval}, broadcast=True)

@socketio.on('late')
def handle_lateform_callback(lateDet):
    emp_id=lateDet['emp_id']
    emp_name=lateDet['emp_name']
    reason=lateDet['reason']
    from_time=lateDet['from_time']
    to_time=lateDet['to_time']
    status='Pending'
    hod_approval='Pending'
    approved_by='Hod Name'
    hr_approval='Pending'
    try:
        new_request=late(emp_id=emp_id,emp_name=emp_name,reason=reason,from_time=from_time,to_time=to_time,status=status,hod_approval=hod_approval,approved_by=approved_by,hr_approval=hr_approval)
        db.session.add(new_request)
        db.session.commit()
        print("new request : ",new_request.emp_id)
        all_latedata = {'emp_id':emp_id, 'emp_name':emp_name, 'reason':reason, 'from_time':from_time, 'to_time':to_time, 'status':status, 'hod_approval':hod_approval, 'approved_by':approved_by, 'hr_approval':hr_approval}
        print("EMP ID : ",all_latedata['emp_id'])

        emit('late', all_latedata, broadcast=True)


    except Exception as e:
        print(f"An error occurred: {str(e)}")



@app.route('/request_disp')
def request_disp():
    late_permission=late.query.order_by(late.date).all()
    leave_permission=leave.query.order_by(leave.date).all()
    return render_template('request_disp.html',late_permission=late_permission,leave_permission=leave_permission)

@socketio.on('leave')
def handle_leaveform_callback(leaveDet):
    emp_id=leaveDet['emp_id']
    emp_name=leaveDet['emp_name']
    reason=leaveDet['reason']
    from_date=leaveDet['from_date']
    to_date=leaveDet['to_date']
    status='Pending'
    hod_approval='Pending'
    approved_by='Hod Name'
    hr_approval='Pending'
    try:
        new_request=leave(emp_id=emp_id,emp_name=emp_name,reason=reason,from_date=from_date,to_date=to_date,status=status,hod_approval=hod_approval,approved_by=approved_by,hr_approval=hr_approval)
        db.session.add(new_request)
        db.session.commit()
        all_leaveData={'emp_id':emp_id,'emp_name':emp_name,'reason':reason,'from_date':from_date,'to_date':to_date,'status':status,'hod_approval':hod_approval,'approved_by':approved_by,'hr_approval':hr_approval}
        print(all_leaveData)
        emit('leave', all_leaveData, broadcast=True)


    except Exception as e:
        print(f"An error occurred: {str(e)}")



