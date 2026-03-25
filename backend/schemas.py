from marshmallow import Schema, fields, validate
from constants import TITLE_MAX_LENGTH, DESCRIPTION_MAX_LENGTH, PRIORITY_MIN, PRIORITY_MAX

class TaskSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True, validate=validate.Length(min=1, max=TITLE_MAX_LENGTH))
    description = fields.Str(load_default=None, validate=validate.Length(max=DESCRIPTION_MAX_LENGTH))
    deadline = fields.Str(load_default=None)
    priority = fields.Int(required=True, validate=validate.Range(min=PRIORITY_MIN, max=PRIORITY_MAX))
    created_at = fields.DateTime(dump_only=True)