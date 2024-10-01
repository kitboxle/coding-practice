

import csv

def read_csv(fname):
    entire_list = []
    try:
        with open(fname, 'r') as sheet:
            student_list = sheet.readlines()

        if not student_list:
            print(f"Error: new_list '{fname}' is empty.")
            return None
        
        for student in student_list:
            x = student.strip().split(',')
            dct ={
                'name': x[0],
                'section': x[1],
                'scores': [float(score) for score in x[2:]],
            }
            dct['average'] = round(sum(dct['scores']) / len(dct['scores']), 3)
            entire_list.append(dct)

        return entire_list
    except:
        print('Error occurred when opening', fname,'to read')

#done

    
def write_csv(fname, student_data):
    try:
        nl = '\n'
        with open(fname, 'w') as nsheet:
            for data in student_data:
                
                stu_name = data['name']
                stu_sect = data['section']
                stu_scores = data['scores']
                nsheet.write(f'{stu_name},{stu_sect},{stu_scores[0]},{stu_scores[1]},{stu_scores[2]},{stu_scores[3]},{stu_scores[4]},{stu_scores[5]},{stu_scores[6]},{stu_scores[7]},{stu_scores[8]},{stu_scores[9]}{nl}')
    except:
        print(f"Error occurred when opening {fname} to write")
        return
        
                

students = read_csv('students.csv')
write_csv('output.csv', students)



def filter_section(student_data, section_name):
    return [filter for filter in student_data if filter['section'] == section_name]

#done



def filter_average(student_data, min_inc, max_exc):
    return[list for list in student_data if list['average'] <= max_exc and list['average']>=min_inc]

#done

def split_section(fname):
    sheet = read_csv(fname)

