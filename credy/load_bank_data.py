import os
import json
from validate.models import Bank,Branch

for filename in os.listdir("/home/anusha/Downloads/ifsc-api-master/data"):
	f = open("/home/anusha/Downloads/ifsc-api-master/data/" + filename)
	bank_code = filename.replace('.json','')
	data = []
	json_data = json.loads(f.read())
	for _, value in json_data.items():
		data.append(value)
	bank_obj = Bank.objects.get(code=bank_code)
	for branch in data:
		Branch.objects.create(
			bank=bank_obj,
			ifsc=branch.get('IFSC'),
			name=branch.get('BRANCH',None),
			contact=branch.get('CONTACT',None),
			city=branch.get('CITY',None),
			district=branch.get('DISTRICT',None),
			state=branch.get('STATE',None)
		)
	print("{} inserted".format(bank_code))


