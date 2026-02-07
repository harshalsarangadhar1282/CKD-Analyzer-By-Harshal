import streamlit as st
import numpy as np

import streamlit as st

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Chronic Kidney Disease Prediction",
    layout="wide",
    page_icon="🩺"
)

# ================= CSS =================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #e3f2fd, #ffffff);
}

/* Title */
.main-title {
    text-align:center;
    font-size:40px;
    font-weight:800;
    color:#0d47a1;
    margin-bottom:20px;
}

/* Section headings */
.section {
    font-size:22px;
    font-weight:700;
    color:#1565c0;
    margin-bottom:10px;
}

/* Labels */
label {
    color:#0d47a1 !important;
    font-weight:600 !important;
}

/* Cards */
.card {
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0 6px 20px rgba(0,0,0,0.15);
}

/* Result colors */
.good { color:#2e7d32; font-weight:700; }
.bad  { color:#c62828; font-weight:700; }
</style>
""", unsafe_allow_html=True)

# ================= TITLE =================
st.markdown('<div class="main-title">🩺 Chronic Kidney Disease Prediction System</div>', unsafe_allow_html=True)
st.markdown("---")

# ================= INPUT SECTION =================
st.subheader("🔍 Patient Medical Details")

col1, col2, col3 = st.columns(3)

# -------- BASIC INFO --------
with col1:
    st.markdown('<div class="section">👤 Basic Info</div>', unsafe_allow_html=True)
    age = st.slider("Age (years)", 1, 100, 45, key="age")
    bp = st.slider("Blood Pressure (mmHg)", 50, 180, 80, key="bp")
    sg = st.selectbox("Specific Gravity", [1.005, 1.010, 1.015, 1.020, 1.025], key="sg")
    al = st.slider("Albumin Level", 0, 5, 1, key="al")
    su = st.slider("Sugar Level", 0, 5, 0, key="su")

# -------- URINE TEST --------
with col2:
    st.markdown('<div class="section">🧪 Urine Test</div>', unsafe_allow_html=True)
    rbc = st.selectbox("Red Blood Cells", ["normal", "abnormal"], key="rbc")
    pc = st.selectbox("Pus Cell", ["normal", "abnormal"], key="pc")
    pcc = st.selectbox("Pus Cell Clumps", ["present", "notpresent"], key="pcc")
    ba = st.selectbox("Bacteria", ["present", "notpresent"], key="ba")
    bgr = st.slider("Blood Glucose Random (mg/dl)", 70, 500, 120, key="bgr")

# -------- BLOOD TEST --------
with col3:
    st.markdown('<div class="section">🧬 Blood Test</div>', unsafe_allow_html=True)
    bu = st.slider("Blood Urea (mg/dl)", 10, 200, 40, key="bu")
    sc = st.slider("Serum Creatinine (mg/dl)", 0.4, 15.0, 1.2, key="sc")
    sod = st.slider("Sodium (mEq/L)", 110, 160, 135, key="sod")
    pot = st.slider("Potassium (mEq/L)", 2.0, 7.0, 4.5, key="pot")
    hemo = st.slider("Hemoglobin (g/dl)", 3.0, 17.0, 12.0, key="hemo")

st.markdown("---")

# -------- MEDICAL HISTORY --------
st.subheader("❤️ Medical History")
c1, c2, c3 = st.columns(3)

with c1:
    htn = st.selectbox("Hypertension", ["yes", "no"], key="htn")
    dm = st.selectbox("Diabetes Mellitus", ["yes", "no"], key="dm")

with c2:
    cad = st.selectbox("Coronary Artery Disease", ["yes", "no"], key="cad")
    appet = st.selectbox("Appetite", ["good", "poor"], key="appet")

with c3:
    pe = st.selectbox("Pedal Edema", ["yes", "no"], key="pe")
    ane = st.selectbox("Anemia", ["yes", "no"], key="ane")

# ================= PREDICTION LOGIC =================
risk_score = 0
if sc > 1.5: risk_score += 2
if bu > 50: risk_score += 1
if hemo < 11: risk_score += 1
if bp > 140: risk_score += 1
if dm == "yes": risk_score += 1
if htn == "yes": risk_score += 1
if ane == "yes": risk_score += 1

def generate_report(result):
    return f"""
CHRONIC KIDNEY DISEASE MEDICAL REPORT
-----------------------------------
Age               : {age}
Blood Pressure    : {bp}
Blood Urea        : {bu}
Serum Creatinine  : {sc}
Hemoglobin        : {hemo}
Diabetes          : {dm}
Hypertension      : {htn}

Final Assessment  : {result}
"""

# ================= RESULT =================
st.markdown("---")
st.subheader("📊 Prediction Result")

if st.button("🔍 Predict CKD"):
    if risk_score >= 4:
        result = "HIGH RISK OF CKD"

        st.markdown("""
        <div class="card bad">
        ❌ High Risk of Chronic Kidney Disease detected.<br>
        Immediate medical consultation recommended.
        </div>
        """, unsafe_allow_html=True)

        st.warning("""
⚠️ **Doctor Recommendation**
- Consult a **Nephrologist immediately**
- Avoid high salt & protein intake
- Regular kidney function tests required
        """)

    else:
        result = "LOW RISK OF CKD"

        st.markdown("""
        <div class="card good">
        ✅ Low Risk of Chronic Kidney Disease.<br>
        Patient condition appears stable.
        </div>
        """, unsafe_allow_html=True)

        st.info("""
💊 **General Health Suggestions**
- Stay hydrated
- Balanced low-salt diet
- Regular exercise
- Periodic health checkups
        """)

    report = generate_report(result)

    st.download_button(
        "📄 Download Medical Report",
        report,
        file_name="CKD_Report.txt",
        mime="text/plain"
    )

# ================= FOOTER =================
st.markdown("---")
st.markdown(
    "<center><b>CKD Classification Project | Machine Learning & Streamlit</b></center>",
    unsafe_allow_html=True
)
