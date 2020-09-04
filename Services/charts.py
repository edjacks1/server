from Config.config        import db
from sqlalchemy           import extract  

from Models.accident      import Accident, Hour
from Models.accident_type import Accident_type
from Models.affected      import Affected, Age_range
from Models.brand         import Brand
from Models.car           import Car
from Models.car_type      import Car_type
from Models.cause         import Cause
from Models.detail        import Detail
from Models.municipality  import Municipality
from Models.neighborhood  import Neighborhood
from Models.place         import Place
from Models.route         import Route
from Models.street        import Street
from Models.subbrand      import Subbrand

def injured(gender='todos'):
    inj = {
        'label':[],
        'value':[]
    }
    types = Detail.query.with_entities(Detail.injured).distinct()
    
    if gender == 'todos':
        for i in types:
            if i[0]:
                inj['value'].append(Detail.query.filter_by(injured=i[0]).count())
                inj['label'].append(i[0])
    
    else:

        if gender == 'hombres':
            flag = True
        else:
            flag = False
        
        gen = Affected.query.filter(Affected.gender==flag).all()
        for i in types:
            if i[0]:
                inj['value'].append(0)
                inj['label'].append(i[0])
        for i in gen:
            accident = Accident.query.filter(Accident.affected_id==i.id).first()
            if accident:
                detail = Detail.query.filter(Detail.id==accident.detail_id).first()
                if detail.injured:
                    index = inj['label'].index(detail.injured)
                    inj['value'][index] += 1

    return inj

def car_type():
    car = {
        'label':[],
        'value':[]
    }
    types = db.session.query(Car_type.name.distinct().label("name"))

    for i in types:
        car_query = Car_type.query.filter_by(name=i[0]).first()
        car['label'].append(car_query.name)
        car['value'].append(db.session.query(Car).filter_by(car_type_id=car_query.id).count())
    return car

def cause(gender='todos'):
    cause_dict = {
        'label':[],
        'count':[]
    }
    
    causes = Cause.query.with_entities(Cause.name).distinct()

    if gender == 'todos':
        for i in causes:
            if i[0] != 'SIN ELEMENTOS':
                cause = Cause.query.filter_by(name=i[0]).first()
                cause_dict['count'].append(db.session.query(Accident).filter_by(cause_id=cause.id).count())
                cause_dict['label'].append(cause.name)
    else:

        if gender == 'hombres':
            flag = True
        else:
            flag = False
        
        gen = Affected.query.filter(Affected.gender==flag).all()
        for i in causes:
            if i[0] != 'SIN ELEMENTOS':
                cause_dict['count'].append(0)
                cause_dict['label'].append(i.name)
        for i in gen:
            accident = Accident.query.filter(Accident.affected_id==i.id).first()
            if accident:
                cause = Cause.query.filter(Cause.id==accident.cause_id).first()
                if cause.name:
                    if cause.name != 'SIN ELEMENTOS':
                        index = cause_dict['label'].index(cause.name)
                        cause_dict['count'][index] += 1

    return cause_dict

def gender():
    man = db.session.query(Affected).filter_by(gender=True).count()
    woman = db.session.query(Affected).filter_by(gender=False).count()
    return man, woman

def hour(gender='todos'):
    hours = []
    for i, hour in enumerate(Hour):
        hour_query = db.session.query(Accident).filter_by(hour=hour)
        hours.append(hour_query.count())
        
        if gender != 'todos':
            for j in hour_query:
                affected = Affected.query.filter_by(id=j.affected_id).first()

                if gender == 'hombres':
                    if affected.gender == False:
                        hours[i] -= 1
                else:
                    if affected.gender == True:
                        hours[i] -= 1

    return hours

def age(gender='todos'):
    ages = []

    for age in Age_range:
        ages.append(db.session.query(Affected).filter_by(age_range=age).count())

    if gender == 'hombres' or gender == 'mujeres':

        if gender == 'hombres':
            flag = False
        else:
            flag = True

        gen = Affected.query.filter(Affected.gender==flag).all()

        for i in gen:
            if i.age_range == Age_range.ten:
                ages[0] -= 1
            elif i.age_range == Age_range.twenty:
                ages[1] -= 1
            elif i.age_range == Age_range.thirty:
                ages[2] -= 1
            elif i.age_range == Age_range.forty:
                ages[3] -= 1
            elif i.age_range == Age_range.fifty:
                ages[4] -= 1
            elif i.age_range == Age_range.sixty:
                ages[5] -= 1
            elif i.age_range == Age_range.seventy:
                ages[6] -= 1
            else:
                ages[7] -= 1

    return ages

def month(gender='todos',limit=6):
    month = []
    for i in range(1,limit+1):
        month_query = db.session.query(Accident).filter(extract('month', Accident.date)==i).all()
        month.append(len(month_query))

        if gender != 'todos':

            for j in month_query:
                affected = Affected.query.filter_by(id=j.affected_id).first()
                
                if gender == 'hombres':
                    if affected.gender == False:
                        month[i-1] -= 1
                else:
                    if affected.gender == True:
                        month[i-1] -= 1

    return month