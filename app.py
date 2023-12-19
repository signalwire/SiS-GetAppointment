from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json
from dateutil import parser


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clients.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    user_phone = db.Column(db.String(20), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    appointment_time = db.Column(db.DateTime, nullable=True)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
@app.route('/get_appointment', methods=['GET','POST'])
def get_appointment():

    data = request.json  
    
    # accessing the 'argument' and then 'parsed', which is a list
    user_data = data.get('argument', {}).get('parsed', [{}])
    first_name = user_data[0].get('first_name')
    last_name = user_data[0].get('last_name')
    dob_input = user_data[0].get('dob')
    
    if not first_name or not last_name or not dob_input:
        return Response(json.dumps({'error': 'First name, last name, and date of birth are required'}), status=400, mimetype='application/json')

    try:
        dob = parser.parse(dob_input).date()
    except ValueError:
        return Response(json.dumps({'error': 'Invalid date of birth format. Please use MM-DD-YYYY'}), status=400, mimetype='application/json')

    existing_user = User.query.filter_by(first_name=first_name, last_name=last_name, dob=dob).first()

    # If the user exists and has an appointment, provide information
    if existing_user:
        if existing_user.appointment_time:
            # Return information about the appointment
            appointment_info = f"Thank you for calling, {first_name}. Your appointment is scheduled for {existing_user.appointment_time.strftime('%Y-%m-%d %H:%M:%S')}."
            return Response(json.dumps({'response': appointment_info}), mimetype='application/json')
        else:
            # Inform the user no appointment is found
            return Response(json.dumps({'error': f"No appointment found for {first_name}."}), status=404, mimetype='application/json')
    else:
        # No user found with an appointment, inform the caller
        return Response(json.dumps({'error': "No user or appointment found."}), status=404, mimetype='application/json')


if __name__ == '__main__':
    app.run(port=8080, debug=True)