import json
from pokazniku import nounlist2
from odunuzi import nounlist1

def convertToJSON():
    with open ( "//фінальна лабараторна//odunuzi_json.json","w") as write_file:
        json.dump(nounlist1,write_file)
def convertInJSON():
    with open("//фінальна лабараторна//pokazniku_json.json","w") as write_file:
        json.dump(nounlist2,write_file)