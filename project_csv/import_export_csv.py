from os.path import exists

class ImportExportCSV:

	# FILE_CSV_PATH = "data.csv"
	FILE_CSV_PATH = "savnw.csv"
	MODE_READ_FILE = "r"
	MODE_WRITE_FILE = "w"
	SUCCESS = "Success"
	ERROR = "Error"
	INDEX_TABLE_NAME_START = -1

	# def __init__(self):

	# 	try:
	# 		self.csv_file = open(self.FILE_CSV_PATH, self.MODE_READ_FILE)

	# 		self.csv_file.close()
	# 	except Exception as e:
	# 		print(e)

	def open_file_csv(self, file_name, open_mode):
		try:
			self.csv_file = open(file_name, open_mode)
			# print(self.csv_file)
			return True
		except:
			# print("Error")
			return False

	def close_file_csv(self):
		if self.csv_file:
			self.csv_file.close()

	def get_table_names(self):
		try:
			self.table_names = []

			list = self.csv_file.readline().split(",")[1].split(") (")
		
			for i in range(1, len(list)):
				text = list[i]
				if i == len(list) - 1:
					table_name = text[(text.find(":") + 1):text.rfind(")")].strip()
				else:
					table_name = text[(text.find(":") + 1):].strip()

				self.table_names.append(table_name)

			print(self.table_names)
			return True

		except:

			return False

	def convert_csv_to_dict(self, file_name):

		if self.open_file_csv(file_name, self.MODE_READ_FILE):

			if self.get_table_names():

				data = {}
				for table_name in self.table_names:
					data[table_name] = []

				current_index = self.INDEX_TABLE_NAME_START
				for line in self.csv_file.readlines():
				    if line[0] == "0":
				        field_list = []

				        current_index += 1

				        temp_list = line[line.find("(")+1:line.rfind(')')].split(",")

				        for text in temp_list:
				            field_list.append(text.strip())

				        print(field_list)

				    else:
				        # value_list = []
				        value_list = line.replace("\n", "").strip(",").split(",")

				        value_list.pop(0)

				        dictionary = {}

				        for field, value in zip(field_list, value_list):
				            dictionary[field] = value.strip()

				        data[self.table_names[current_index]].append(dictionary)

				print(len(data))
				return data

			else:

				return self.ERROR

			self.close_file_csv(self.csv_file)

			# return self.SUCCESS

		else:

			return self.ERROR

	def write_title_to_csv(self, table_name, values_in_table):
		fields = []
		for field in values_in_table[0].keys():
			fields.append(field)
		table_name = table_name.replace(" ", "_")
		row = ", ".join(fields)
		line = f"0,{table_name} ({row})"
		self.csv_file.write(line + "\n")

	def write_value_to_csv(self, values_in_table, index):
		for dict_one_value in values_in_table:
			row = ",".join(value for value in dict_one_value.values())
			line = f"{str(index)},{row}"
			self.csv_file.write(line + "\n")

	def export_data_to_csv(self, data, file_name):
		try:
			self.open_file_csv(file_name, open_mode=self.MODE_WRITE_FILE)
			# print(data)
			# -------------------------------------------------
			index = 1
			table_names = ["(0:Comment)"]
			for table_name in data.keys():
				# print(table_name)
				table_names.append(f"({str(index)}:{table_name})")
				index += 1
			table_names = ",".join(["0", " ".join(table_names)])
			print(table_names)
			self.csv_file.write(table_names + "\n")
			# ---------------------------------------------------
			
			index = 1
			for table_name, values_in_table in data.items():
				self.write_title_to_csv(table_name, values_in_table)
				self.write_value_to_csv(values_in_table, index)
				index += 1

			return self.SUCCESS
		except:
			return self.ERROR
		finally:
			self.close_file_csv()


if __name__ == '__main__':
	# csv_object = ImportExportCSV()
	# data = csv_object.convert_csv_to_dict(ImportExportCSV.FILE_CSV_PATH)
	# print(data)
	# 
	from data_export_test import data
	csv_object1 = ImportExportCSV()
	csv_object1.export_data_to_csv(data, "file_export.csv")