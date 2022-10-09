from marshmallow import fields, Schema


class QuickResponseVCFSerializer(Schema):
    """Quick Response VCF"""

    first_name: fields.String = fields.String(load_only=True, required=True)
    last_name: fields.String = fields.String(load_only=True, required=True)
    organization: fields.String = fields.String(
        allow_none=True, default=None, load_only=True, required=False
    )
    title: fields.String = fields.String(
        allow_none=True, default=None, load_only=True, required=False
    )
    cell: fields.String = fields.String(load_only=True, required=True)
    phone: fields.String = fields.String(
        allow_none=True, default=None, load_only=True, required=False
    )
    fax: fields.String = fields.String(
        allow_none=True, default=None, load_only=True, required=False
    )
    email: fields.String = fields.Email(
        allow_none=True, default=None, load_only=True, required=False
    )
    url: fields.String = fields.String(
        allow_none=True, default=None, load_only=True, required=False
    )
    street: fields.String = fields.String(
        allow_none=True, default=None, load_only=True, required=False
    )
    city: fields.String = fields.String(
        allow_none=True, default=None, load_only=True, required=False
    )
    region: fields.String = fields.String(
        allow_none=True, default=None, load_only=True, required=False
    )
    postcode: fields.String = fields.String(
        allow_none=True, default=None, load_only=True, required=False
    )
    country: fields.String = fields.String(
        allow_none=True, default=None, load_only=True, required=False
    )
