from data import patients, doctors, stock

def get_response(msg):
    msg = msg.lower()

    # Patient analytics
    if "patient" in msg or "visit" in msg:
        return f"Total patient visits: {len(patients)}"

    # Doctor schedule
    elif "doctor" in msg or "schedule" in msg:
        return doctors.to_string(index=False)

    # Medicine stock
    elif "medicine" in msg or "stock" in msg:
        return stock.to_string(index=False)

    # Department-wise patients
    elif "cardiology" in msg:
        count = len(patients[patients["department"] == "Cardiology"])
        return f"Cardiology patients: {count}"

    elif "ortho" in msg:
        count = len(patients[patients["department"] == "Ortho"])
        return f"Ortho patients: {count}"

    return "Ask about patients, doctors, or medicine stock."