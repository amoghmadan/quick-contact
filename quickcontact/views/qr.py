from http import HTTPStatus

from flask import request, views, Response
from marshmallow.exceptions import ValidationError
from marshmallow.schema import SchemaMeta

from quickcontact.serializers.qr import QuickResponseVCFSerializer
from quickcontact.utils.qr import generate_qr
from quickcontact.utils.vcf import generate_vcf


class QuickResponseVCFView(views.MethodView):
    """Generate VCF QR"""

    serializer_class: SchemaMeta = QuickResponseVCFSerializer

    def post(self: "QuickResponseVCFView", *args: str, **kwargs: str) -> Response:
        """
        Serialize data generate QR content and return as image/png mimetype
        :param args: str
        :param kwargs: str
        :return: Response
        """
        serializer: QuickResponseVCFSerializer = self.serializer_class()
        try:
            validated_data: dict = serializer.load(request.json)
        except ValidationError as e:
            return Response(
                e.messages, HTTPStatus.BAD_REQUEST, mimetype="application/json"
            )
        content: bytes = generate_qr(generate_vcf(validated_data))
        return Response(content, HTTPStatus.CREATED, mimetype="image/png")
