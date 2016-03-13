from flask_wtf import Form
from wtforms import StringField, IntegerField 
from wtforms.validators import ValidationError

def unit_id_format(form, field):
    parts = field.data.split(':')
    if parts != 3:
        raise ValidationError('unit id format is <start>:<end>:<unit id>')

class AvailableForm(Form):
    unit_id = StringField(u'<start>:<end>:<unit id>', [unit_id_format])
    resort_id = StringField(u'resort id')
    from_date = IntegerField(u'start timestamp')
    start_date = IntegerField(u'end timestamp')
    calendar_id = StringField(u'gcal id')
    room_type = StringField(u'room type')
    capacity = IntegerField(u'capacity')
    status = StringField(u'status')
