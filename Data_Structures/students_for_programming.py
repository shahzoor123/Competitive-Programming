def pick_up_guide(students_list):
    mx = max(students_list)
    student_pickup_list = [i for i in students_list if i < mx ]
    total_number_of_students = len(student_pickup_list)
    for s in student_pickup_list:
        if s < student_pickup_list[s] - 1 :
            student_pickup_list.remove(s)
    print(student_pickup_list)
            

# pick_up_guide([7,10,1,2,3,4,8,5,9])    
pick_up_guide([5,10,1,6,3,5,8])    