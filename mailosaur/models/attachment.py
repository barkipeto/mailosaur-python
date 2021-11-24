class Attachment(object):
    """Attachment.

    :param id:
    :type id: str
    :param content_type:
    :type content_type: str
    :param file_name:
    :type file_name: str
    :param content_id:
    :type content_id: str
    :param content:
    :type content: str
    :param length:
    :type length: int
    :param url:
    :type url: str
    """

    def __init__(self, data=None):
        if data is None:
            data = {}

        self.id = data.get('id', None)
        self.content_type = data.get('contentType', None)
        self.file_name = data.get('fileName', None)
        self.content_id = data.get('contentId', None)
        self.content = data.get('content', None)
        self.length = data.get('length', None)
        self.url = data.get('url', None)

    def to_json(self):
        return {
            'contentType': self.content_type,
            'fileName': self.file_name,
            'contentId': self.content_id,
            'content': self.content
        }
