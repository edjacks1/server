from Config.config     import db
import math

from Models.accident import Accident, Hour
from Models.affected import Affected

def get_xy(gender = 'todos'):
	points = []
	accidents = Accident.query.all()
	for accident in accidents:
		if gender == 'todos':
			if not math.isnan(accident.x) and not math.isnan(accident.y):
				points.append((accident.x, accident.y))
		else:
			affected = Affected.query.filter_by(id=accident.affected_id).first()
			if gender == 'hombres':
				if affected.gender == True:
					if not math.isnan(accident.x) and not math.isnan(accident.y):
						points.append((accident.x, accident.y))
			else:
				if affected.gender == False:
					if not math.isnan(accident.x) and not math.isnan(accident.y):
						points.append((accident.x, accident.y))
	return points