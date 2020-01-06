from typing import Optional

from cloudfoundry_client.v3.entities import EntityManager, Entity


class UserManager(EntityManager):
    def __init__(self, target_endpoint: str, client: 'CloudfoundryClient'):
        super(UserManager, self).__init__(target_endpoint, client, '/v3/users')

    def create(self, guid: str,
               meta_labels: Optional[dict] = None,
               meta_annotations: Optional[dict] = None) -> Entity:
        data = {
            'guid': guid,
            'metadata': {
                'labels': meta_labels,
                'annotations': meta_annotations
            }
        }
        return super(UserManager, self)._create(data)

    def remove(self, guid: str):
        super(UserManager, self)._remove(guid)

    def update(self, guid: str,
               meta_labels: Optional[dict] = None,
               meta_annotations: Optional[dict] = None) -> Entity:
        data = {
            'metadata': {
                'labels': meta_labels,
                'annotations': meta_annotations
            }
        }
        return super(UserManager, self)._update(guid, data)
