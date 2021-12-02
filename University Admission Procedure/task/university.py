class Physics:
    physics_list = []

    def __init__(self, gpa, n, priority):
        self.priority = priority
        self.gpa_physics = list(filter(lambda x: 'Physics' in x[self.priority + 6], gpa))
        self.n = n
        self.accepted_applicants = []
        self.sorted_candidates = []
        self.meas_score = []
        self.sorted_meas_score = []
        self.accepted_mean_score = []

    def sort_applicants(self):
        self.meas_score.extend(
            list(map(lambda x: [x[0], x[1], max((float(x[2]) + float(x[4])) / 2, float(x[6]))], self.gpa_physics)))
        self.sorted_meas_score.extend(sorted(self.meas_score, key=lambda x: (-(float(x[2])), x[0], x[1])))
        self.sorted_candidates.extend(
            sorted(self.gpa_physics, key=lambda x: (-(max((float(x[2]) + float(x[4])) / 2, float(x[6]))), x[0], x[1])))
        return self.sorted_candidates

    def accepted(self):
        self.accepted_applicants.extend(Physics.sort_applicants(self)[:self.n])
        self.accepted_mean_score.extend(self.sorted_meas_score[:self.n])
        Physics.physics_list.extend(self.accepted_mean_score)
        return self.accepted_applicants


class Mathematics:
    mathematics_list = []

    def __init__(self, gpa, n, priority):
        self.gpa_mathematics = list(filter(lambda x: 'Mathematics' in x[priority + 6], gpa))
        self.n = n
        self.accepted_applicants = []
        self.sorted_candidates = []
        self.meas_score = []
        self.sorted_meas_score = []
        self.accepted_mean_score = []

    def sort_applicants(self):
        self.sorted_candidates.extend(
            sorted(self.gpa_mathematics, key=lambda x: (-(max(float(x[4]), float(x[6]))), x[0], x[1])))
        self.meas_score.extend(
            list(map(lambda x: [x[0], x[1], max(float(x[4]), float(x[6]))], self.gpa_mathematics)))
        self.sorted_meas_score.extend(sorted(self.meas_score, key=lambda x: (-(float(x[2])), x[0], x[1])))
        return self.sorted_candidates

    def accepted(self):
        self.accepted_applicants.extend(Mathematics.sort_applicants(self)[:self.n])
        self.accepted_mean_score.extend(self.sorted_meas_score[:self.n])
        Mathematics.mathematics_list.extend(self.accepted_mean_score)
        return self.accepted_applicants


class Biotech:
    biotech_list = []

    def __init__(self, gpa, n, priority):
        self.gpa_biotech = list(filter(lambda x: 'Biotech' in x[priority + 6], gpa))
        self.n = n
        self.accepted_applicants = []
        self.sorted_candidates = []
        self.meas_score = []
        self.sorted_meas_score = []
        self.accepted_mean_score = []

    def sort_applicants(self):
        self.meas_score.extend(
            list(map(lambda x: [x[0], x[1], max((float(x[2]) + float(x[3])) / 2, float(x[6]))], self.gpa_biotech)))
        self.sorted_candidates.extend(
            sorted(self.gpa_biotech, key=lambda x: (-(max((float(x[2]) + float(x[3])) / 2, float(x[6]))), x[0], x[1])))
        self.sorted_meas_score.extend(sorted(self.meas_score, key=lambda x: (-(float(x[2])), x[0], x[1])))
        return self.sorted_candidates

    def accepted(self):
        self.accepted_applicants.extend(Biotech.sort_applicants(self)[:self.n])
        self.accepted_mean_score.extend(self.sorted_meas_score[:self.n])
        Biotech.biotech_list.extend(self.accepted_mean_score)
        return self.accepted_applicants


class Chemistry:
    chemistry_list = []

    def __init__(self, gpa, n, priority):
        self.gpa_chemistry = list(filter(lambda x: 'Chemistry' in x[priority + 6], gpa))
        self.n = n
        self.accepted_applicants = []
        self.sorted_candidates = []
        self.meas_score = []
        self.sorted_meas_score = []
        self.accepted_mean_score = []

    def sort_applicants(self):
        self.sorted_candidates.extend(
            sorted(self.gpa_chemistry, key=lambda x: (-(max(float(x[3]), float(x[6]))), x[0], x[1])))
        self.meas_score.extend(
            list(map(lambda x: [x[0], x[1], max(float(x[3]), float(x[6]))], self.gpa_chemistry)))
        self.sorted_meas_score.extend(sorted(self.meas_score, key=lambda x: (-(float(x[2])), x[0], x[1])))
        return self.sorted_candidates

    def accepted(self):
        self.accepted_applicants.extend(Chemistry.sort_applicants(self)[:self.n])
        self.accepted_mean_score.extend(self.sorted_meas_score[:self.n])
        Chemistry.chemistry_list.extend(self.accepted_mean_score)
        return self.accepted_applicants


class Engineering:
    engineering_list = []

    def __init__(self, gpa, n, priority):
        self.gpa_engineering = list(filter(lambda x: 'Engineering' in x[priority + 6], gpa))
        self.n = n
        self.accepted_applicants = []
        self.sorted_candidates = []
        self.meas_score = []
        self.sorted_meas_score = []
        self.accepted_mean_score = []

    def sort_applicants(self):
        self.sorted_candidates.extend(
            sorted(self.gpa_engineering, key=lambda x: (-(max((float(x[4]) + float(x[5])) / 2, float(x[6]))), x[0], x[1])))
        self.meas_score.extend(
            list(map(lambda x: [x[0], x[1], max((float(x[4]) + float(x[5])) / 2, float(x[6]))], self.gpa_engineering)))
        self.sorted_meas_score.extend(sorted(self.meas_score, key=lambda x: (-(float(x[2])), x[0], x[1])))
        return self.sorted_candidates

    def accepted(self):
        self.accepted_applicants.extend(Engineering.sort_applicants(self)[:self.n])
        self.accepted_mean_score.extend(self.sorted_meas_score[:self.n])
        Engineering.engineering_list.extend(self.accepted_mean_score)
        return self.accepted_applicants


def remove_gpa(department_1_accepted, n, department_class, gpa, priority, department_2_accepted=None):
    # remove the accepted applicants from gpa list of candidates
    if priority == 2:
        if len(department_1_accepted) < n:
            department_n = n - len(department_1_accepted)
            department_accepted = department_class(gpa, department_n, priority).accepted()
            for accepted in department_accepted:
                gpa.remove(accepted)
            return department_accepted
        return []
    elif priority == 3:
        if (len(department_1_accepted) + len(department_2_accepted)) < n:
            department_n = n - len(department_1_accepted) - len(department_2_accepted)
            department_accepted = department_class(gpa, department_n, priority).accepted()
            for accepted in department_accepted:
                gpa.remove(accepted)
            return department_accepted
        return None


def main():
    # number_of_grades = 3
    # grades = [int(input()) for _ in range(number_of_grades)]
    # mean = sum(grades) / len(grades)
    # print(mean)
    # if mean >= 60:
    #     print("Congratulations, you are accepted!")
    # else:
    #     print("We regret to inform you that we will not be able to offer you admission.")

    # n = int(input())
    # m = int(input())
    # gpa = [input().split() for _ in range(n)]
    # # print(gpa)
    # sorted_candidates = sorted(gpa, key=lambda x: (-float(x[2]), x[0], x[1]))
    # # print(sorted_candidates)
    #
    # print("Successful applicants:")
    # for index in range(m):
    #     print(sorted_candidates[index][0], sorted_candidates[index][1])

    # maximum number of students for each department
    n = int(input())
    gpa = []
    # with open("applicant_list_7.txt", "r", encoding="utf-8") as f:
    with open("applicants.txt", "r", encoding="utf-8") as f:
        for applicant in f:
            gpa.append(applicant.strip().split())

    physics_1 = Physics(gpa, n, 1)
    mathematics_1 = Mathematics(gpa, n, 1)
    biotech_1 = Biotech(gpa, n, 1)
    chemistry_1 = Chemistry(gpa, n, 1)
    engineering_1 = Engineering(gpa, n, 1)

    # remove accepted candidates from gpa
    physics_1_accepted = physics_1.accepted()
    for physics_accepted in physics_1_accepted:
        gpa.remove(physics_accepted)

    mathematics_1_accepted = mathematics_1.accepted()
    for mathematics_accepted in mathematics_1_accepted:
        gpa.remove(mathematics_accepted)

    biotech_1_accepted = biotech_1.accepted()
    for biotech_accepted in biotech_1_accepted:
        gpa.remove(biotech_accepted)

    chemistry_1_accepted = chemistry_1.accepted()
    for chemistry_accepted in chemistry_1_accepted:
        gpa.remove(chemistry_accepted)

    engineering_1_accepted = engineering_1.accepted()
    for engineering_accepted in engineering_1_accepted:
        gpa.remove(engineering_accepted)

    # second priorities
    physics_2_accepted = remove_gpa(physics_1_accepted, n, Physics, gpa, 2)
    mathematics_2_accepted = remove_gpa(mathematics_1_accepted, n, Mathematics, gpa, 2)
    biotech_2_accepted = remove_gpa(biotech_1_accepted, n, Biotech, gpa, 2)
    chemistry_2_accepted = remove_gpa(chemistry_1_accepted, n, Chemistry, gpa, 2)
    engineering_2_accepted = remove_gpa(engineering_1_accepted, n, Engineering, gpa, 2)

    # third priorities
    physics_3_accepted = remove_gpa(physics_1_accepted, n, Physics, gpa, 3, physics_2_accepted)
    mathematics_3_accepted = remove_gpa(mathematics_1_accepted, n, Mathematics, gpa, 3, mathematics_2_accepted)
    biotech_3_accepted = remove_gpa(biotech_1_accepted, n, Biotech, gpa, 3, biotech_2_accepted)
    chemistry_3_accepted = remove_gpa(chemistry_1_accepted, n, Chemistry, gpa, 3, chemistry_2_accepted)
    engineering_3_accepted = remove_gpa(engineering_1_accepted, n, Engineering, gpa, 3, engineering_2_accepted)

    # Print/write to file the departments approved in the alphabetic order
    departments = {"Biotech": Biotech.biotech_list, "Chemistry": Chemistry.chemistry_list,
                   "Engineering": Engineering.engineering_list, "Mathematics": Mathematics.mathematics_list,
                   "Physics": Physics.physics_list}
    # grades = {"Biotech": 2, "Chemistry": 3, "Engineering": 2, "Mathematics": 4, "Physics": 2}

    for department, department_list in departments.items():
        print(department)
        file_name = f"{department}.txt"
        with open(file_name, "w", encoding="utf-8") as f:
            count = 0
            # grade = grades[department]
            # for successful_applicant in sorted(department_list, key=lambda x: (-float(x[grade]), x[0], x[1])):
            for successful_applicant in sorted(department_list, key=lambda x: (-float(x[2]), x[0], x[1])):
                count += 1
                # f.write(f"{successful_applicant[0]} {successful_applicant[1]} {successful_applicant[grade]}\n")
                f.write(f"{successful_applicant[0]} {successful_applicant[1]} {successful_applicant[2]}\n")
                # print(successful_applicant[0], successful_applicant[1], successful_applicant[grade])
                print(count, successful_applicant)
            print()


if __name__ == "__main__":
    main()