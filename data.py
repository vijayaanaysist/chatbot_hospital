import pandas as pd

# Patient Visits
patients = pd.DataFrame({
    "name": ["John", "Sara", "Mike", "Emma", "Raj"],
    "department": ["Cardiology", "Ortho", "ENT", "Cardiology", "Neurology"],
    "date": ["2026-04-01", "2026-04-02", "2026-04-02", "2026-04-03", "2026-04-03"]
})

# Doctor Schedule
doctors = pd.DataFrame({
    "doctor": ["Dr. A", "Dr. B", "Dr. C"],
    "speciality": ["Cardiology", "Ortho", "Neurology"],
    "available": ["Mon-Wed", "Thu-Fri", "Mon-Fri"]
})

# Medicine Stock
stock = pd.DataFrame({
    "medicine": ["Paracetamol", "Aspirin", "Amoxicillin"],
    "quantity": [100, 50, 200]
})