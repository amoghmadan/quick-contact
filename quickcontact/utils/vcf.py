from typing import Union


def generate_vcf(data: dict) -> str:
    """
    Convert dict to VCF text
    :param data: dict
    :return: str
    """
    address_list: list[str] = [
        "",
        "",
        data.get("street"),
        data.get("city"),
        data.get("region"),
        data.get("postcode"),
        data.get("country"),
    ]
    if any([bool(i) for i in address_list]):
        address: Union[str, None] = ";".join([i if i else "" for i in address_list])
    else:
        address: Union[str, None] = None
    name_list: list[str] = [data.get("last_name"), data.get("first_name")]
    name: str = ";".join([i if i else "" for i in name_list])
    vcard_data: dict[str, Union[str, None]] = {
        "N": name,
        "ORG": data.get("organization"),
        "TITLE": data.get("title"),
        "EMAIL;TYPE=INTERNET": data.get("email"),
        "URL": data.get("url"),
        "TEL;TYPE=CELL": data.get("cell"),
        "TEL": data.get("phone"),
        "TEL;TYPE=FAX": data.get("fax"),
        "ADR": address,
    }
    fmt: str = "\n".join([":".join((k, v)) for k, v in vcard_data.items() if v])
    raw: str = "BEGIN:VCARD\nVERSION:3.0\n{}\nEND:VCARD".format(fmt)
    contents: str = raw.replace(",", "\\,")
    return contents
