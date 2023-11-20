import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    pattern = r'^\+7 \d{3} \d{3} \d{2} \d{2}$'
    return re.match(pattern, phone) is not None

def validate_date(date):
    pattern = r'^(?:\d{2}\.\d{2}\.\d{4}|\d{4}-\d{2}-\d{2})$'
    return re.match(pattern, date) is not None


form_template = {
    "name": "MyForm",
    "field_name_1": "email",
    "field_name_2": "phone",
    "field_name_3": "date",
    "field_name_4": "text",
}