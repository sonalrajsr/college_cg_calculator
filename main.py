#Update the cg and credit according to your college system.
sem_1_cg = 0
sem_1_cred = 0

sem_2_cg = 0
sem_2_cred = 0

sem_3_cg = 0
sem_3_cred = 0

sem_4_cg = 0
sem_4_cred = 0

sem_5_cg = 0
sem_5_cred = 0

sem_6_cg = 0
sem_6_cred = 0

sem_7_cg = 0
sem_7_cred = 0

sem_8_cg = 0
sem_8_cred = 0

sem_cred_list = [sem_1_cred, sem_2_cred, sem_3_cred, sem_4_cred, sem_5_cred, sem_6_cred, sem_7_cred, sem_8_cred]

sem_cg_list = [sem_1_cg, sem_2_cg, sem_3_cg, sem_4_cg,sem_5_cg,sem_6_cg,sem_7_cg,sem_8_cg]

def sgpa(sem_number):
    credit = sem_cred_list[sem_number-1]
    cg = sem_cg_list[sem_number-1]
    sgpa = (cg*credit)/credit
    return sgpa

def cgpa(sem_number):
    total_cred = 0
    total_cg = 0
    for i in range(0,sem_number):
        total_cg = total_cg + (sem_cg_list[i] * sem_cred_list[i])
        total_cred = total_cred + sem_cred_list[i]
        comm_cg = total_cg / total_cred
    return comm_cg

print("Your cgpa = ",cgpa(1))
print("Your sgpa = "sgpa(1))
