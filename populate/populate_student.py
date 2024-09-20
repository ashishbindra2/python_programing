# import random
from random import choice

# import docx
#
# # Load the document
# doc = docx.Document('attendance.docx')
# doc_2 = docx.Document("./MCA SECTION A(1st year) Workshop day 1 attendence.docx")
# # # Read all paragraphs
# # for para in doc.paragraphs:
# #     print(para.text)
#
# MCA_1_SEC_B = {}
#
# # Iterate over each table in the document
# for table in doc.tables:
#     for row in table.rows:
#         # Extract each cell's text in the row
#         row_data = [cell.text for cell in row.cells]
#
#         if row_data[1]:
#             MCA_1_SEC_B[row_data[1]] = row_data[2]
#
# print(MCA_1_SEC_B)
# MCA_1_SEC_A = {}
#
# for table in doc_2.tables:
#     for row in table.rows[1:]:
#         # Extract each cell's text in the row
#         row_data = [cell.text for cell in row.cells]
#
#         if row_data[0]:
#             MCA_1_SEC_A[row_data[0]] = row_data[1]
# print(MCA_1_SEC_A)

data = {'24071247': 'AMANJOT KAUR', '24071249': 'NANDITA', '24071251': 'AMANDEEP SINGH', '24071253': 'KHUSHBOO',
        '24071254': 'MANPREET KAUR', '24071255': 'SHARNJEET KAUR', '24071256': 'KULDEEP SINGH',
        '24071258': 'AMANDEEP SINGH', '24071261': 'MAMTA', '24071263': 'VARINDER KAUR', '24071264': 'NIKITA RANI',
        '24071265': 'ISHA SAINI', '24071268': 'ABHINEET MIROCK', '24071269': 'JASPREET KAUR',
        '24071270': 'GARIMA SHARMA', '24071272': 'KANIKA BHATIA', '24071273': 'YOGITA SHARMA', '24071274': 'MUSKAN',
        '24071276': 'ARPANPREET KAUR', '24071277': 'ARUSHI THAKUR', '24071278': 'AASTHA SHARMA',
        '24071279': 'ANJALI THAKUR', '24071280': 'URVI BANSAL', '24071281': 'NAMAN SHARMA', '24071282': 'SARBJEET KAUR',
        '24071284': 'SIMRAN DHANJU', '24071285': 'JASHANPREET KAUR', '24071286': 'SUKHDEEP SINGH'}

data_1 = {'1': 'JASKARN SINGH', '2': 'KIRANDEEP KAUR', '3': 'JASMEET KAUR', '4': 'MANJINDER SINGH',
          '5': 'SIMARNOOR KAUR', '6': 'JASHANPREET SINGH', '7': 'TANVEER SINGH REEHAL', '8': 'ALISHA RANI',
          '9': 'JASKARAN SINGH', '10': 'HIMANSHU SAGGU', '11': 'SIMRANJEET KAUR', '12': 'KOMALPREET KAUR',
          '13': 'NANDINI GABA', '14': 'REETIKA JASWAL', '15': 'JASHANJOT KAUR', '16': 'PURVAK', '17': 'JASKIRAT KAUR',
          '18': 'RIYA', '19': 'BABITA SHARMA', '20': 'SAMANPREET SINGH', '21': 'ALISH', '22': 'PARVEEN KAUR',
          '23': 'BHAVNA', '24': 'HARDEEP SINGH', '25': 'JASWINDER SINGH', '26': 'JAHNVI', '27': 'PARBHJOT KAUR',
          '28': 'SUKHVEER KAUR', '29': 'ARSHDEEP SINGH', '30': 'JASMEEN KAUR', '31': 'VASUDEV SHARMA',
          '32': 'AMNINDER SINGH', '33': 'NAUNIDHI'}

role_number = list(data.keys())

name_sec_a = list(data.values())
name_sec_b = list(data_1.values())

names_list = name_sec_a + name_sec_b


def random_name_sec_a():
    return choice(name_sec_a)


def random_name_sec_b():
    return choice(name_sec_b)


def random_name_mca():
    return choice(names_list)


def random_roll_number():
    choice(list(data.keys()))


