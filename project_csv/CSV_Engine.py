from os.path import exists

class CSV_Engine:
	
	# FILE_CSV_PATH = "data.csv"
	FILE_CSV_PATH = "savnw.csv"

	MODE_READ_FILE = "r"
	MODE_WRITE_FILE = "w"

	SUCCESS = "Success"
	ERROR = "Error"
	
	# INDEX_START = -1

	def __init__(self, path: str):
		# file path
		self.path = path

		# save data in csv . file
		self.data = {}
		
		# save table names in csv . file
		self.table_names = []


	def open_file_csv(self, path, open_mode: str):
		'''
		this function will open csv . file anf save file object to self.csv_file
		- path: file path
		- open_mode: file open mode
		- @return true if the opening is successful otherwise return false
		'''
		try:
			self.csv_file = open(path, open_mode)
			# print(self.csv_file)
			return True
		except:
			# print("Error")
			return False

	def close_file_csv(self):
		'''
		This function is used to close the csv . file if it is opening
		'''
		if self.csv_file:
			self.csv_file.close()

	def get_table_names(self):
		'''
		This function is used to get the names of the tables in the csv file
		and save to self.table_names
		- if successful return true otherwise return false
		'''
		try:
			second_index = 1 # second index in list
			# read from csv file and process string to list
			# example: "0,(0:Comment) (1:Bus ) ( 2:Bus Data)"
			# => list = ["(0:Comment", " 1:Bus ", " 2:Bus Data)"]
			list = self.csv_file.readline().split(",")[second_index].split(") (")

			# ------------------------------------------------------------------
			# process the list above and append to self.table_names
			# example: list = ["(0:Comment", " 1:Bus ", " 2:Bus Data)"]
			# => table_names = ["Bus", "Bus Data"]
			for index in range(second_index, len(list)):
				text = list[index]
				if index == len(list) - 1: # "len(list) - 1" is the final list
					table_name = text[(text.find(":") + 1):text.rfind(")")].strip()
				else:
					table_name = text[(text.find(":") + 1):].strip()

				self.table_names.append(table_name)
			# ------------------------------------------------------------------

			return True
		except:
			return False

	def import_csv(self):
		'''
		This function import from csv file and save data to 
		self.data = {"table 1": [{}, {}, ...], "table 2": [{}, {}, ...], ...}
		- if successful return true otherwise return false
		'''

		if self.open_file_csv(self.path, self.MODE_READ_FILE):
			if self.get_table_names():

				# generate key and value pairs in self.data in there:
				# - key is the name of the table as a string
				# - value is an empty list
				for table_name in self.table_names:
					self.data[table_name] = []

				# ----------------- save data to self.data ----------------
				current_index = -1 # index = -1 because each time the program enters the if block, 
				                   # the current_index will increase by 1
								   # then will get the corresponding table name in self.table_names

				# read each line in the file, there will be two forms
				# form1: "0,Bus (Bus Number, Bus Name)\n"
				# form2: "1,101,NUC-A,,,,,,,,\n"
				for line in self.csv_file.readlines():

					# if block will process form one to list of data fields
					# example: line = "0,Bus (Bus Number, Bus Name)"
					# => field_list = ["Bus Number", "Bus Name"]
					if line[0] == "0":
						field_list = []
						current_index += 1
						temp_list = line[line.find("(")+1:line.rfind(')')].split(",")
						for text in temp_list:
							field_list.append(text.strip())

					else:
						# "1,101,NUC-A,,,,,,,,\n" => value_list = ["1", "101", "NUC-A"]
						value_list = line.replace("\n", "").strip(",").split(",")

						# remove first element in list
						value_list.pop(0)

						dictionary = {}

						# get each corresponding element in the two lists in turn and store it in dict
						for field, value in zip(field_list, value_list):
							dictionary[field] = value.strip()

						self.data[self.table_names[current_index]].append(dictionary)
				# -------------------------------------------------------
				#print(len(data))
			else:
				return self.ERROR

			# close file
			self.close_file_csv()
		else:
			return self.ERROR

	def write_title_to_csv(self, table_name, table_fields):
		'''
		This function is used to write the title of the table to the csv file
		- table_name: name of a table
		- table_fields: fields of a table
		'''

		# save the data fields of a table
		fields = []

		# browse the fields
		first_index = 0 # get the first in list
		for field in table_fields[first_index].keys():
			fields.append(field)

		# example: "bus number" => "bus_number"
		table_name = table_name.replace(" ", "_")

		# example: fields = ["one", "two"], table_name = "number"
		# => line = "0,number (one, two)"
		row = ", ".join(fields)
		line = f"0,{table_name} ({row})"

		# write line in csv file and add '\n' at the end
		self.csv_file.write(line + "\n")

	def write_value_to_csv(self, values_in_table, index):
		'''
		This function is used to write the value of the table to the csv file
		- values_in_table: fields of a table
		- index: order of tables in csv . file
		'''

		# write the value lines corresponding to the field in the csv . file 
		# and add '\n' at the end
		for dict_one_value in values_in_table:
			# use list comprehension
			row = ",".join(value for value in dict_one_value.values())
			line = f"{str(index)},{row}"
			self.csv_file.write(line + "\n")

	def export_csv(self, path):
		'''
		This function is used to export from self.data or data passed in to a new csv file
		- path: the file path you want to save
		- if successful return true otherwise return false
		'''

		try:
			self.open_file_csv(path, open_mode=self.MODE_WRITE_FILE)
			# -------------------------------------------------
			# The target needs to create a string of the following form:
			# "0,(0:Comment) (1:Bus ) ( 2:Bus Data)"
			index = 1 # order of tables in csv . file
			table_names = ["(0:Comment)"]
			for table_name in self.data.keys():
				# print(table_name)
				table_names.append(f"({str(index)}:{table_name})")
				index += 1
			table_names = ",".join(["0", " ".join(table_names)])
			# ---------------------------------------------------

			# write data to first line in csv . file
			self.csv_file.write(table_names + "\n")
			
			# ----------------------------------------------
			# write a data table to the csv . file
			index = 1 # order of tables in csv . file
			for table_name, values_in_table in self.data.items():
				self.write_title_to_csv(table_name, values_in_table)
				self.write_value_to_csv(values_in_table, index)
				index += 1
			# ----------------------------------------------

			return self.SUCCESS
		except:
			return self.ERROR
		finally:
			# close csv file
			self.close_file_csv()


if __name__ == '__main__':
	csv_object = CSV_Engine(CSV_Engine.FILE_CSV_PATH)
	csv_object.import_csv()
	# print(csv_object.data)
	csv_object.export_csv("export_file.csv")
	# from data_export_test import data
	# csv_object1 = CSV_Engine(CSV_Engine.FILE_CSV_PATH)
	# csv_object1.export_csv("file_export.csv")