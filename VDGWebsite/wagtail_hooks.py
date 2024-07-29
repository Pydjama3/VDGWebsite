# from wagtail import hooks
#
#
# @hooks.register("register_rich_text_features")
# def tables_in_rich_text(feature):
#     feature_name = "table"
#     type_ = ""
#
#
# # @hooks.register('register_rich_text_features')
# # def html_in_rich_text(features):
# #     """
# #     Registering the `mark` feature, which uses the `MARK` Draft.js inline style type,
# #     and is stored as HTML with a `<mark>` tag.
# #     """
# #     feature_name = 'iframe'
# #     type_ = 'MARK'
# #     tag = 'iframe'
# #
# #     # 2. Configure how Draftail handles the feature in its toolbar.
# #     control = {
# #         'type': type_,
# #         'label': '🖽',
# #         'description': 'Iframe',
# #         # This isn’t even required – Draftail has predefined styles for MARK.
# #         # 'style': {'textDecoration': 'line-through'},
# #     }
# #
# #     # 3. Call register_editor_plugin to register the configuration for Draftail.
# #     features.register_editor_plugin(
# #         'draftail', feature_name, draftail_features.InlineStyleFeature(control)
# #     )
# #
# #     # 4.configure the content transform from the DB to the editor and back.
# #     db_conversion = {
# #         'from_database_format': {tag: InlineStyleElementHandler(type_)},
# #         'to_database_format': {'style_map': {type_: tag}},
# #     }
# #
# #     # 5. Call register_converter_rule to register the content transformation conversion.
# #     features.register_converter_rule('contentstate', feature_name, db_conversion)
# #
# #     # 6. (optional) Add the feature to the default features list to make it available
# #     # on rich text fields that do not specify an explicit 'features' list
# #     features.default_features.append('mark')
