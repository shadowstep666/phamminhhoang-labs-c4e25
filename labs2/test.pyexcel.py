import pyexcel
from collections  import OrderedDict



list_dictionaries=[
    OrderedDict({
    "name":"adam",
    "age":28,
    }),
    OrderedDict({
    "name":"beatrice",
    "age":29,
    }),
    OrderedDict({
    "name":"ceri",
    "age":30,
    })
]
pyexcel.save_as(records=list_dictionaries,dest_file_name="test.xls")
