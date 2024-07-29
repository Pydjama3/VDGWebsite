# from typing import List
#
# from django.db.models import Model
# from django.contrib.auth import get_user_model
# from wagtail.rich_text import EmbedHandler
#
#
# class IframeEmbedHandler(EmbedHandler):
#     identifier = "iframe"
#
#     @staticmethod
#     def get_model():
#         pass
#
#     @classmethod
#     def get_instance(cls, attrs: dict) -> Model:
#         return super().get_instance(attrs)
#
#     @classmethod
#     def get_many(cls, attrs_list: List[dict]) -> List[Model]:
#         return super().get_many(attrs_list)
#
#     @staticmethod
#     def expand_db_attributes(attrs: dict) -> str:
#         pass
#
#     @classmethod
#     def expand_db_attributes_many(cls, attrs_list: List[dict]) -> List[str]:
#         return super().expand_db_attributes_many(attrs_list)
#
#     @classmethod
#     def extract_references(cls, attrs):
#         return super().extract_references(attrs)
