class Patient(object):
    PATIENT_COUNT = 0
    def __init__(self, name, allergies):
        self.name = name
        self.allergies = allergies
        self.id = Patient.PATIENT_COUNT
        self.bed_num = None
        Patient.PATIENT_COUNT += 1

class Hospital(object):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.patients = []
        self.total_beds = self.initialize_total_beds()

    def initialize_total_beds(self):
        total_beds = []
        for i in range(0, self.capacity):
            total_beds.append({
                "bed_id": i,
                "Available": True
            })
        return total_beds
    
    def admit(self, patient):
        if len(self.patients) <= self.capacity:
            self.patients.append(patient)
            for i in range(0, len(self.total_beds)):
                if self.total_beds[i]["Available"]:
                    patient.bed_num = self.total_beds[i]["bed_id"]
                    self.total_beds[i]["Available"] = False
                    break
            print "Patient #{} admitted to bed #{}".format(patient.id, patient.bed_num)
        else:
            "Hospital is at full capacity"

    def discharge(self, patient_id):
        for patient in self.patients:
            if patient.id == patient_id:
                for bed in self.total_beds:
                    if bed["bed_id"] == patient.bed_num:
                        bed["Available"] = True
                        break

                self.patients.remove(patient)
                return "Patient {} successfully discharged. Bed #{} now available.". format(patient.id, patient.bed_num)
            return"Patient not found"


ken = Patient("Ken", "Potato")
daniel = Patient("Daniel", "Peanuts")
indhu = Patient("Indhu", "Meat")
everett = Patient("Everett", "Women")
wendy = Patient("Wendy", "Fish")
gabrielle = Patient("Gabrielle", "Perfume")
print ken.name
print ken.allergies
print daniel.name
print daniel.allergies
print indhu.name
print indhu.allergies
print everett.name
print everett.allergies
print wendy.name
print wendy.allergies
print gabrielle.name
print gabrielle.allergies
harbor = Hospital("Harborview", 100)
print harbor.name
print harbor.capacity
harbor.initialize_total_beds
print harbor.admit(ken)
print harbor.admit(daniel)
print harbor.admit(indhu)
print harbor.admit(everett)
print harbor.admit(wendy)
print harbor.admit(gabrielle)
print harbor.discharge(ken)