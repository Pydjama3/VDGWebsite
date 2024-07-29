from wagtail.blocks import StreamBlock
from wagtail.contrib.table_block.blocks import TableBlock


new_table_options = {
    'minSpareRows': 0,
    'startRows': 6,
    'startCols': 4,
    'colHeaders': False,
    'rowHeaders': False,
    'contextMenu': True,
    'editor': 'text',
    'stretchH': 'all',
    'height': 216,
    'language': 'en',
    'renderer': 'text',
    'autoColumnSize': False,
}


class VDGTableBlock(StreamBlock):
    table = TableBlock(table_options=new_table_options)

    class Meta:
        icon = "table"
