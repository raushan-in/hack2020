import ast
from django.db import models
from hashids import Hashids
import random
from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta

 
current_time = datetime.now() 
hashids = Hashids(salt=str(current_time), min_length=4)

class ListField(models.TextField):
	description = "Stores a python list"

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def from_db_value(self, value, expression, connection):
		if value is None:
			return value
		if isinstance(value, str):
			return value.split(',')

	def to_python(self, value):
		if not value:
			value = []
		if isinstance(value, list):
			return value
		if isinstance(value, str):
			return ast.literal_eval(value)

	def get_prep_value(self, value):
		if value is None:
			return value
		if value is not None and isinstance(value, str):
			return value
		if isinstance(value, list):
			return ','.join(value)

	def value_to_string(self, obj):
		value = self.value_from_object(obj)
		return self.get_prep_value(value)

def get_code(email):
	hash1 = hashids.encode(random.randrange(100, 10000))
	hash2 = hashids.encode(random.randrange(100, 10000))
	return f'IL-{hash1}-{hash2}'

def get_expiry(month):
	dt = date.today() + relativedelta(months=+month)
	return datetime.combine(dt, datetime.min.time())