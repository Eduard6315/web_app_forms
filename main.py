from flask import Flask, request, jsonify
from app_forms.form_templates import form_template,validate_email, validate_phone, validate_date
from tinydb import TinyDB

app = Flask(__name__)
db = TinyDB('db.json')


db.insert(form_template)

def get_field_type(value):
    if validate_email(value):
        return 'email'
    elif validate_phone(value):
        return 'phone'
    elif validate_date(value):
        return 'date'
    else:
        return 'text'

@app.route('/get_form', methods=['POST'])
def get_form():
    if request.method =="POST":
        data = request.form
        data_types = {field: get_field_type(value) for field, value in data.items()}

        for template in db.all():
            template_fields = {field: field_type for field, field_type in template.items() if field != 'name'}
            if all(field in data_types and data_types[field] == field_type for field, field_type in template_fields.items()):
                return template['name']

        return jsonify(data_types)

if __name__ == '__main__':
    app.run(debug=True)