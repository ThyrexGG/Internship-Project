"""Build FECO301 Gantt workbook. Run: py -3 _build_gantt.py"""
from openpyxl import Workbook
from openpyxl.styles import Font, Fill, PatternFill, Alignment, Border, Side, Protection
from openpyxl.utils import get_column_letter
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.chart import BarChart, Reference
from openpyxl.worksheet.datavalidation import DataValidation
from datetime import date, timedelta
from copy import copy

OUT = r"c:\Users\Asus\Desktop\Internship-Project-main\docs\feco301\HomeSweet_FECO301_Gantt_v2.xlsx"

wb = Workbook()

arial = Font(name="Arial", size=11)
arial_b = Font(name="Arial", size=11, bold=True)
arial_title = Font(name="Arial", size=16, bold=True, color="1F4E79")
arial_h = Font(name="Arial", size=12, bold=True, color="FFFFFF")
arial_small = Font(name="Arial", size=9, italic=True, color="666666")
arial_input = Font(name="Arial", size=11, color="0000FF")  # blue = inputs
arial_formula = Font(name="Arial", size=11, color="000000")
arial_link = Font(name="Arial", size=11, color="008000")

fill_navy = PatternFill("solid", fgColor="1F4E79")
fill_yellow = PatternFill("solid", fgColor="FFFF00")
fill_header = PatternFill("solid", fgColor="2E75B6")
fill_green = PatternFill("solid", fgColor="C6EFCE")
fill_red = PatternFill("solid", fgColor="FFC7CE")
fill_amber = PatternFill("solid", fgColor="FFEB9C")
fill_grey = PatternFill("solid", fgColor="F2F2F2")
fill_bar = PatternFill("solid", fgColor="5B9BD5")
fill_out = PatternFill("solid", fgColor="D9D9D9")
fill_white = PatternFill("solid", fgColor="FFFFFF")

thin = Border(
    left=Side(style="thin", color="B0B0B0"),
    right=Side(style="thin", color="B0B0B0"),
    top=Side(style="thin", color="B0B0B0"),
    bottom=Side(style="thin", color="B0B0B0"),
)
wrap = Alignment(wrap_text=True, vertical="center")
center = Alignment(horizontal="center", vertical="center", wrap_text=True)


def style_range(ws, cells, font=arial, fill=None, border=True, align=wrap):
    for addr in cells:
        c = ws[addr]
        c.font = font
        if fill:
            c.fill = fill
        if border:
            c.border = thin
        c.alignment = align


def apply_font_all(ws):
    for row in ws.iter_rows():
        for cell in row:
            if cell.font is None or cell.font.name != "Arial":
                cell.font = Font(
                    name="Arial",
                    size=cell.font.size or 11,
                    bold=cell.font.bold,
                    italic=cell.font.italic,
                    color=cell.font.color,
                )


# ───────────────────────────────────────── Assumptions
ws = wb.active
ws.title = "Assumptions"

ws["A1"] = "HomeSweet — FECO301 Gantt & plan assumptions"
ws["A1"].font = arial_title
ws.merge_cells("A1:F1")
ws["A2"] = (
    "Yellow + blue text = team edits. Black = formulas. "
    "Calendar assumes Week 1 starts Mon 20 Oct 2026 so Week 3 = Session 3 (3 Nov 2026). "
    "Correct the yellow date if your timetable differs. Capacity uses the course rule of ~5 hours/student/week."
)
ws["A2"].font = arial_small
ws.merge_cells("A2:F2")
ws.row_dimensions[2].height = 36

headers = ["ID", "Assumption", "Value", "Unit", "Source / note"]
for i, h in enumerate(headers, 1):
    cell = ws.cell(4, i, h)
    cell.font = arial_h
    cell.fill = fill_header
    cell.alignment = center
    cell.border = thin

# rows of assumptions: id, label, value, unit, note, input?
rows = [
    (1, "Team size", 6, "students", "Session 2: contract for 6 members. Edit if roster changes.", True),
    (2, "Hours per student per week", 5, "hours", "Thomas: about 5 hours per student per week.", True),
    (3, "Course length", 15, "weeks", "Weeks 1–15 as stated in Session 2 feedback.", True),
    (4, "Week 1 start (Monday)", date(2026, 10, 20), "date", "Back-calculated from Session 3 = 3 Nov 2026 = Week 3.", True),
    (5, "Weekly team capacity", None, "hours", "Formula: team size × hours/student.", False),
    (6, "Total course capacity", None, "hours", "Formula: weekly capacity × 15 weeks.", False),
    (7, "Hours currently planned (in-scope tasks)", None, "hours", "Formula: SUM of Gantt hours where In scope = Yes.", False),
    (8, "Capacity remaining", None, "hours", "Formula: total capacity − planned hours. Keep ≥ 0.", False),
    (9, "Named client (outside team)", "[TO CONFIRM]", "text", "CamTech Student Affairs OR a landlord group. i-Hub is sponsor only.", True),
    (10, "Sponsor", "i-Hub (Virtubis)", "text", "Session 2: real sponsor, not the client.", True),
    (11, "Who pays cloud during the course", "[TO CONFIRM]", "text", "Students / landlords / university / i-Hub. Open until interviews.", True),
    (12, "Cloud budget assumed (USD/month)", 0, "USD", "Set 0 until who-pays is confirmed. Session 2 cited $70–120 as unconfirmed.", True),
    (13, "Live site collects real ID photos?", "Must be No", "Yes/No", "Ethics red. Stop live KYC or confirm test data only.", True),
    (14, "Class project-council representative", "[TO CONFIRM]", "text", "One student. Same as all teams.", True),
    (15, "Advise: Flutter or web", "Web (recommended)", "choice", "Do not build Flutter this course. Decide in Advise, not in code.", True),
    (16, "Advise: identity approach", "Server-side + no live PII until consent", "choice", "Browser face-api is the ethics problem.", True),
]

for i, (aid, label, val, unit, note, is_input) in enumerate(rows):
    r = 5 + i
    ws.cell(r, 1, aid).font = arial
    ws.cell(r, 2, label).font = arial_b
    ws.cell(r, 4, unit).font = arial
    ws.cell(r, 5, note).font = Font(name="Arial", size=10)
    for c in range(1, 6):
        ws.cell(r, c).border = thin
        ws.cell(r, c).alignment = wrap
    if aid == 5:
        ws.cell(r, 3, "=C5*C6")
        ws.cell(r, 3).font = arial_formula
        ws.cell(r, 3).number_format = "0"
    elif aid == 6:
        ws.cell(r, 3, "=C9*C7")
        ws.cell(r, 3).font = arial_formula
        ws.cell(r, 3).number_format = "0"
    elif aid == 7:
        ws.cell(r, 3, '=SUMIF(Gantt[In scope],"Yes",Gantt[Est. hours])')
        # Tables might not work well with openpyxl table formulas in LibreOffice.
        # Use a simple SUMIF on a range instead after Gantt is built — placeholder then fix.
        ws.cell(r, 3, "=SUMIF(Gantt!H8:H40,\"Yes\",Gantt!G8:G40)")
        ws.cell(r, 3).font = arial_formula
        ws.cell(r, 3).number_format = "0"
    elif aid == 8:
        ws.cell(r, 3, "=C10-C11")
        ws.cell(r, 3).font = arial_formula
        ws.cell(r, 3).number_format = "0"
    else:
        ws.cell(r, 3, val)
        ws.cell(r, 3).font = arial_input
        ws.cell(r, 3).fill = fill_yellow
        if isinstance(val, date):
            ws.cell(r, 3).number_format = "YYYY-MM-DD"
        elif isinstance(val, (int, float)):
            ws.cell(r, 3).number_format = "0"

ws.cell(22, 2, "Week start dates (formula from C8)")
ws.cell(22, 2).font = arial_b
ws.merge_cells("B22:E22")

ws["A23"] = "Week"
ws["B23"] = "Label"
ws["C23"] = "Monday start"
ws["D23"] = "Notes"
for col in range(1, 5):
    ws.cell(23, col).font = arial_h
    ws.cell(23, col).fill = fill_header
    ws.cell(23, col).border = thin

notes = {
    2: "Session 2 feedback (27–28 Oct)",
    3: "Session 3 — charter conditions",
    5: "A1 integrated project plan due (end of Week 5)",
    6: "Realise cycle 1 starts",
    8: "Realise cycle 1 ends",
    9: "Realise cycle 2 starts",
    10: "Realise cycle 2 ends",
}
for w in range(1, 16):
    r = 23 + w
    ws.cell(r, 1, w).font = arial
    ws.cell(r, 2, f'=CONCATENATE("W",A{r})').font = arial_formula
    # Avoid CONCATENATE if we can use & 
    ws.cell(r, 2, f'="W"&A{r}')
    ws.cell(r, 3, f"=$C$8+7*(A{r}-1)")
    ws.cell(r, 3).number_format = "YYYY-MM-DD"
    ws.cell(r, 3).font = arial_formula
    ws.cell(r, 4, notes.get(w, ""))
    for c in range(1, 5):
        ws.cell(r, c).border = thin
        ws.cell(r, c).alignment = Alignment(vertical="center")
    if w in (3, 5):
        ws.cell(r, 4).fill = fill_amber
    if w in (6, 7, 8, 9, 10):
        ws.cell(r, 4).fill = fill_green

ws["A40"] = "Legend"
ws["A40"].font = arial_b
ws["B41"] = "Yellow + blue text"
ws["C41"] = "Type here (inputs). Do not type over black formula cells."
ws["C41"].font = arial
ws["B41"].fill = fill_yellow
ws["B41"].font = arial_input
ws["B42"] = "Black text"
ws["C42"] = "Formula — changes when inputs change."
ws["B43"] = "Green fill on Gantt"
ws["C43"] = "In-scope week"
ws["B43"].fill = fill_green
ws["B44"] = "Grey fill on Gantt"
ws["C44"] = "Out of course / deferred (shown so the cut is visible)"
ws["B44"].fill = fill_out

ws.column_dimensions["A"].width = 8
ws.column_dimensions["B"].width = 42
ws.column_dimensions["C"].width = 38
ws.column_dimensions["D"].width = 14
ws.column_dimensions["E"].width = 72
ws.row_dimensions[1].height = 24
ws.freeze_panes = "A5"

# ───────────────────────────────────────── Gantt
g = wb.create_sheet("Gantt")
g["A1"] = "HomeSweet FECO301 — first Gantt (what fits / what stays out)"
g["A1"].font = arial_title
g.merge_cells("A1:X1")
g["A2"] = (
    "Edit yellow: Owner, Start week, Duration (weeks), Est. hours, In scope. "
    "Week bars are formulas (1 = work that week). Do not paint bars by hand. "
    "Hours assume even spread across the duration. Capacity check is on Assumptions."
)
g["A2"].font = arial_small
g.merge_cells("A2:X2")
g.row_dimensions[2].height = 32

g["A4"] = "Week start →"
g["A4"].font = arial_small
for w in range(1, 16):
    cell = g.cell(4, 8 + w, f"=Assumptions!C{23+w}")
    cell.font = Font(name="Arial", size=8)
    cell.number_format = "D-MMM"
    cell.alignment = center
    cell.border = thin

# headers row 7 (row 6 labels W1-W15)
headers = [
    "ID", "Task", "Phase", "Owner (edit)", "Start week", "Duration (wks)",
    "Est. hours", "In scope",
]
for i, h in enumerate(headers, 1):
    cell = g.cell(6, i, h)
    cell.font = arial_h
    cell.fill = fill_header
    cell.alignment = center
    cell.border = thin
for w in range(1, 16):
    cell = g.cell(6, 8 + w, f"W{w}")
    cell.font = arial_h
    cell.fill = fill_header
    cell.alignment = center
    cell.border = thin
g.cell(6, 24, "End week")
g.cell(6, 24).font = arial_h
g.cell(6, 24).fill = fill_header
g.cell(6, 24).border = thin
g.cell(6, 25, "Hours / week")
g.cell(6, 25).font = arial_h
g.cell(6, 25).fill = fill_header
g.cell(6, 25).border = thin

# Task list: id, task, phase, owner, start, dur, hours, in_scope
tasks = [
    (1, "Team manifesto, contract, council rep", "Manage", "", 2, 1, 12, "Yes"),
    (2, "One-page charter (this pack)", "Analyse", "", 2, 2, 10, "Yes"),
    (3, "Competitor scan (Khmerhome, Bamnang, CamboRent, realestate.com.kh)", "Analyse", "", 2, 2, 12, "Yes"),
    (4, "Landlord interviews (≥3): list / verify / pay", "Analyse", "", 3, 3, 15, "Yes"),
    (5, "Named client — written review agreement", "Analyse", "", 3, 2, 8, "Yes"),
    (6, "Stakeholder power/interest map", "Analyse", "", 3, 1, 4, "Yes"),
    (7, "Data-protection: stop live ID photos; consent & retention draft", "Ethics", "", 4, 4, 12, "Yes"),
    (8, "Who pays cloud — decision log", "Advise", "", 4, 4, 6, "Yes"),
    (9, "Advise memo: web vs Flutter; identity approach; partner vs compete", "Advise", "", 4, 2, 10, "Yes"),
    (10, "A1 integrated plan (WBS, Gantt freeze, budget, risks)", "Manage", "", 4, 2, 16, "Yes"),
    (11, "Design: listing/landlord verification process (no new Flutter)", "Design", "", 5, 3, 15, "Yes"),
    (12, "Design: simple Trust Score (one score, not two)", "Design", "", 6, 2, 6, "Yes"),
    (13, "Design: server-side identity (architecture + consent UX, test data only)", "Design", "", 6, 3, 12, "Yes"),
    (14, "Usability backlog triage from existing protocol", "Design", "", 7, 2, 6, "Yes"),
    (15, "Realise cycle 1 — trust process on web MVP", "Realise C1", "", 6, 3, 30, "Yes"),
    (16, "Usability test cycle 1 (reuse protocol)", "Realise C1", "", 8, 1, 12, "Yes"),
    (17, "Realise cycle 2 — fixes from cycle 1", "Realise C2", "", 9, 2, 28, "Yes"),
    (18, "Usability test cycle 2", "Realise C2", "", 10, 1, 16, "Yes"),
    (19, "CamTech student pilot (small; only if client confirms)", "Realise C2", "", 11, 2, 16, "Yes"),
    (20, "Evaluation, report, handover (project not product)", "Evaluate", "", 11, 5, 30, "Yes"),
    (21, "OUT: Flutter mobile app", "Deferred", "", 7, 6, 0, "No"),
    (22, "OUT: Real payments / KHQR live money", "Deferred", "", 7, 6, 0, "No"),
    (23, "OUT: Push notifications", "Deferred", "", 7, 4, 0, "No"),
    (24, "OUT: Fraud-rule engine", "Deferred", "", 8, 4, 0, "No"),
    (25, "OUT: Roommate score (second score)", "Deferred", "", 8, 4, 0, "No"),
    (26, "OUT: 50-student operational pilot (unless client confirms)", "Deferred", "", 10, 3, 0, "No"),
    (27, "OUT: $70–120/mo Cloud Functions stack", "Deferred", "", 6, 8, 0, "No"),
]

dv_scope = DataValidation(type="list", formula1='"Yes,No"', allow_blank=False)
dv_scope.add("H8:H40")
g.add_data_validation(dv_scope)

dv_week = DataValidation(type="whole", operator="between", formula1="1", formula2="15")
dv_week.add("E8:F40")
g.add_data_validation(dv_week)

first_task = 8
for i, t in enumerate(tasks):
    r = first_task + i
    tid, name, phase, owner, start, dur, hours, scope = t
    g.cell(r, 1, tid).font = arial
    g.cell(r, 2, name).font = arial
    g.cell(r, 3, phase).font = arial
    g.cell(r, 4, owner if owner else "[name]")
    g.cell(r, 4).font = arial_input
    g.cell(r, 4).fill = fill_yellow
    g.cell(r, 5, start)
    g.cell(r, 5).font = arial_input
    g.cell(r, 5).fill = fill_yellow
    g.cell(r, 6, dur)
    g.cell(r, 6).font = arial_input
    g.cell(r, 6).fill = fill_yellow
    g.cell(r, 7, hours)
    g.cell(r, 7).font = arial_input
    g.cell(r, 7).fill = fill_yellow
    g.cell(r, 7).number_format = "0"
    g.cell(r, 8, scope)
    g.cell(r, 8).font = arial_input
    g.cell(r, 8).fill = fill_yellow
    g.cell(r, 24, f"=E{r}+F{r}-1")
    g.cell(r, 24).font = arial_formula
    g.cell(r, 25, f'=IF(F{r}=0,0,G{r}/F{r})')
    g.cell(r, 25).font = arial_formula
    g.cell(r, 25).number_format = "0.0"
    for c in range(1, 9):
        g.cell(r, c).border = thin
        g.cell(r, c).alignment = wrap
    g.cell(r, 24).border = thin
    g.cell(r, 25).border = thin
    g.row_dimensions[r].height = 22
    for w in range(1, 16):
        col = 8 + w
        # 1 if week in [start, start+dur)
        g.cell(r, col, f'=IF(AND({get_column_letter(col)}$6=CONCATENATE("W",{w}),$E{r}<={w},$E{r}+$F{r}-1>={w}),1,"")')
        # simpler: W columns are literally W1.. so compare week number
        g.cell(r, col, f'=IF(AND($E{r}<={w},$E{r}+$F{r}-1>={w}),1,"")')
        g.cell(r, col).font = Font(name="Arial", size=8, color="FFFFFF")
        g.cell(r, col).alignment = center
        g.cell(r, col).border = thin
        g.cell(r, col).number_format = "0"

last_task = first_task + len(tasks) - 1

# conditional formatting: in-scope bar vs out-of-scope bar
# If cell=1 and H=Yes -> green; if cell=1 and H=No -> grey
for w in range(1, 16):
    col = get_column_letter(8 + w)
    rng = f"{col}{first_task}:{col}{last_task}"
    g.conditional_formatting.add(
        rng,
        FormulaRule(formula=[f'AND({col}{first_task}=1,$H{first_task}="Yes")'], fill=fill_green),
    )
    g.conditional_formatting.add(
        rng,
        FormulaRule(formula=[f'AND({col}{first_task}=1,$H{first_task}="No")'], fill=fill_out),
    )

# weekly load row
load_row = last_task + 2
g.cell(load_row, 2, "Team hours that week (in-scope only)")
g.cell(load_row, 2).font = arial_b
for w in range(1, 16):
    col = get_column_letter(8 + w)
    # hours that week = sum of (bar * hours/duration) for in-scope
    g.cell(
        load_row,
        8 + w,
        f'=SUMPRODUCT(({col}{first_task}:{col}{last_task}=1)*($H{first_task}:$H{last_task}="Yes")*($Y{first_task}:$Y{last_task}))',
    )
    g.cell(load_row, 8 + w).font = arial_formula
    g.cell(load_row, 8 + w).number_format = "0.0"
    g.cell(load_row, 8 + w).border = thin

cap_row = load_row + 1
g.cell(cap_row, 2, "Weekly capacity (from Assumptions)")
g.cell(cap_row, 2).font = arial
for w in range(1, 16):
    g.cell(cap_row, 8 + w, "=Assumptions!C9")
    g.cell(cap_row, 8 + w).font = arial_link
    g.cell(cap_row, 8 + w).number_format = "0.0"
    g.cell(cap_row, 8 + w).border = thin

over_row = load_row + 2
g.cell(over_row, 2, "Over / (under) capacity")
g.cell(over_row, 2).font = arial_b
for w in range(1, 16):
    col = get_column_letter(8 + w)
    g.cell(over_row, 8 + w, f"={col}{load_row}-{col}{cap_row}")
    g.cell(over_row, 8 + w).font = arial_formula
    g.cell(over_row, 8 + w).number_format = "0.0"
    g.cell(over_row, 8 + w).border = thin
g.conditional_formatting.add(
    f"I{over_row}:W{over_row}",
    CellIsRule(operator="greaterThan", formula=["0"], fill=fill_red),
)
g.conditional_formatting.add(
    f"I{over_row}:W{over_row}",
    CellIsRule(operator="lessThanOrEqual", formula=["0"], fill=fill_green),
)

g.column_dimensions["A"].width = 5
g.column_dimensions["B"].width = 62
g.column_dimensions["C"].width = 14
g.column_dimensions["D"].width = 16
g.column_dimensions["E"].width = 12
g.column_dimensions["F"].width = 14
g.column_dimensions["G"].width = 12
g.column_dimensions["H"].width = 12
for w in range(1, 16):
    g.column_dimensions[get_column_letter(8 + w)].width = 5
g.column_dimensions["X"].width = 10
g.column_dimensions["Y"].width = 12
g.freeze_panes = "C8"
g.row_dimensions[6].height = 28

# ───────────────────────────────────────── In vs Out
io = wb.create_sheet("In vs Out")
io["A1"] = "What goes in this course / what stays out"
io["A1"].font = arial_title
io.merge_cells("A1:D1")
io["A2"] = "From Session 2 Keep / Decide / Defer. Counts pull from Gantt."
io["A2"].font = arial_small

for i, h in enumerate(["Decision", "Item", "Hours (if in Gantt)", "Why"], 1):
    c = io.cell(4, i, h)
    c.font = arial_h
    c.fill = fill_header
    c.border = thin

keep = [
    ("Keep", "Competitor and landlord analysis", "=SUMIF(Gantt!B8:B40,\"*Competitor*\",Gantt!G8:G40)+SUMIF(Gantt!B8:B40,\"*Landlord*\",Gantt!G8:G40)", "Analyse → Advise"),
    ("Keep", "Listing and landlord verification", "=Gantt!G18", "Core promise = trust"),
    ("Keep", "Server-side identity checks (design/prototype, test data)", "=Gantt!G20", "Ethics red if left in the browser"),
    ("Keep", "Simple Trust Score (one)", "=Gantt!G19", "Not two scores"),
    ("Keep", "Usability backlog + two test cycles", "=Gantt!G21+Gantt!G23+Gantt!G25", "Thomas: split Realise"),
    ("Decide in Advise, do not build", "Flutter vs web → web", 0, "MVP already exists"),
    ("Defer", "Real payments", 0, "Beyond course prototype"),
    ("Defer", "Push notifications", 0, "Beyond course prototype"),
    ("Defer", "Fraud rules", 0, "Beyond course prototype"),
    ("Defer", "Roommate score", 0, "Probably defer"),
    ("Defer", "50-student pilot as an operation", 0, "Access unconfirmed"),
]
for i, row in enumerate(keep):
    r = 5 + i
    for c, val in enumerate(row, 1):
        io.cell(r, c, val)
        io.cell(r, c).font = arial_formula if c == 3 else arial
        io.cell(r, c).border = thin
        io.cell(r, c).alignment = wrap
        if row[0] == "Keep":
            io.cell(r, 1).fill = fill_green
        elif row[0].startswith("Decide"):
            io.cell(r, 1).fill = fill_amber
        else:
            io.cell(r, 1).fill = fill_out
    io.row_dimensions[r].height = 28

io["A17"] = "Hours in scope (Gantt Yes)"
io["B17"] = "=Assumptions!C11"
io["B17"].font = arial_link
io["C17"] = "Total capacity"
io["D17"] = "=Assumptions!C10"
io["D17"].font = arial_link
io["A18"] = "If in-scope hours exceed capacity, cut hours on Gantt (yellow), do not add Flutter."
io["A18"].font = arial_small
io.merge_cells("A18:D18")

io.column_dimensions["A"].width = 32
io.column_dimensions["B"].width = 62
io.column_dimensions["C"].width = 22
io.column_dimensions["D"].width = 36

# ───────────────────────────────────────── Stakeholders
st = wb.create_sheet("Stakeholders")
st["A1"] = "Stakeholder power / interest map (draft — edit yellow)"
st["A1"].font = arial_title
st.merge_cells("A1:G1")
st["A2"] = (
    "Power 1–5 = ability to stop or resource the project. Interest 1–5 = how much they care this semester. "
    "Manage closely = power≥4 and interest≥4. Keep satisfied = high power, low interest. "
    "Replace example scores after you talk to people."
)
st["A2"].font = arial_small
st.merge_cells("A2:G2")
st.row_dimensions[2].height = 36

for i, h in enumerate(
    ["Stakeholder", "Role", "Power (1-5)", "Interest (1-5)", "Quadrant", "Interest this semester", "Action"],
    1,
):
    c = st.cell(4, i, h)
    c.font = arial_h
    c.fill = fill_header
    c.border = thin
    c.alignment = center

stakeholders = [
    ("[Named client — Student Affairs or landlords]", "Client (must be outside team)", 5, 4, "Must review progress in writing"),
    ("i-Hub (Virtubis)", "Sponsor", 4, 3, "Keep informed; not a substitute for a client"),
    ("CamTech students (from provinces)", "Users — tenants", 2, 5, "Usability cycles; 32 survey is directional only"),
    ("Independent landlords (n≥3)", "Users — supply side", 4, 3, "Interviews decide if idea works"),
    ("Thomas / FECO301 assessors", "Assessor", 5, 5, "Charter, A1, ethics, two cycles"),
    ("HomeSweet team (6)", "Delivery", 3, 5, "Fair work-share in contract"),
    ("Bamnang", "Possible partner / competitor", 3, 2, "Advise: partner vs compete; do not copy campuses"),
    ("Khmerhome / realestate.com.kh", "Incumbent portals", 2, 1, "Monitor; do not compete on volume"),
    ("CamboRent", "Similar trust-marketplace", 2, 2, "Check if CamTech students already use it"),
    ("CamTech ethics / data protection", "Gatekeeper", 5, 4, "No live ID photos until rules exist"),
    ("Class project council", "Peer governance", 2, 3, "One representative"),
]

for i, (name, role, pwr, interest, action) in enumerate(stakeholders):
    r = 5 + i
    st.cell(r, 1, name).font = arial_input
    st.cell(r, 1).fill = fill_yellow
    st.cell(r, 2, role).font = arial
    st.cell(r, 3, pwr).font = arial_input
    st.cell(r, 3).fill = fill_yellow
    st.cell(r, 4, interest).font = arial_input
    st.cell(r, 4).fill = fill_yellow
    # Quadrant formula
    st.cell(
        r,
        5,
        f'=IF(AND(C{r}>=4,D{r}>=4),"Manage closely",IF(AND(C{r}>=4,D{r}<4),"Keep satisfied",IF(AND(C{r}<4,D{r}>=4),"Keep informed","Monitor")))',
    )
    st.cell(r, 5).font = arial_formula
    st.cell(r, 6, action).font = arial
    st.cell(r, 7, "[edit after interviews]").font = arial_input
    st.cell(r, 7).fill = fill_yellow
    for c in range(1, 8):
        st.cell(r, c).border = thin
        st.cell(r, c).alignment = wrap
    st.row_dimensions[r].height = 28

st["A18"] = "How to plot: X = interest (col D), Y = power (col C). Yellow scores are hypotheses until Session 3 conversations."
st["A18"].font = arial_small
st.merge_cells("A18:G18")

st.column_dimensions["A"].width = 48
st.column_dimensions["B"].width = 28
st.column_dimensions["C"].width = 14
st.column_dimensions["D"].width = 14
st.column_dimensions["E"].width = 16
st.column_dimensions["F"].width = 52
st.column_dimensions["G"].width = 28

# ───────────────────────────────────────── Team
tm = wb.create_sheet("Team")
tm["A1"] = "Team contract sheet (6 members) — fill yellow"
tm["A1"].font = arial_title
tm["A2"] = (
    "Example split is even (16.7% each) so the share formula works. Replace names and hours. "
    "Fair share does not have to be equal hours if roles differ — explain in Notes. "
    "This is not a legal contract; paste into your manifesto."
)
tm["A2"].font = arial_small
tm.merge_cells("A2:F2")
tm.row_dimensions[2].height = 36

for i, h in enumerate(
    ["#", "Name", "Primary role this course", "Planned hours (15 wks)", "Share of team hours", "Notes"],
    1,
):
    c = tm.cell(4, i, h)
    c.font = arial_h
    c.fill = fill_header
    c.border = thin

for i in range(1, 7):
    r = 4 + i
    tm.cell(r, 1, i).font = arial
    tm.cell(r, 2, f"[Member {i}]").font = arial_input
    tm.cell(r, 2).fill = fill_yellow
    tm.cell(r, 3, "[role]").font = arial_input
    tm.cell(r, 3).fill = fill_yellow
    tm.cell(r, 4, "=Assumptions!$C$10/6")
    tm.cell(r, 4).font = arial_formula
    tm.cell(r, 4).number_format = "0.0"
    tm.cell(r, 4).fill = fill_yellow  # they may override formula with a number — skill says yellow for inputs
    # Actually if it's a formula it shouldn't be yellow input. Let them type planned hours as input.
    tm.cell(r, 4, 75)
    tm.cell(r, 4).font = arial_input
    tm.cell(r, 4).fill = fill_yellow
    tm.cell(r, 4).number_format = "0.0"
    tm.cell(r, 5, f"=IF(SUM($D$5:$D$10)=0,\"\",D{r}/SUM($D$5:$D$10))")
    tm.cell(r, 5).font = arial_formula
    tm.cell(r, 5).number_format = "0.0%"
    tm.cell(r, 6, "").font = arial_input
    tm.cell(r, 6).fill = fill_yellow
    for c in range(1, 7):
        tm.cell(r, c).border = thin

tm["C12"] = "Sum of planned hours"
tm["D12"] = "=SUM(D5:D10)"
tm["D12"].font = arial_formula
tm["E12"] = '=IF(ABS(D12-Assumptions!C10)<0.5,"Matches capacity","Does not match Assumptions total — fix yellow hours")'
tm["E12"].font = arial_formula
tm.merge_cells("E12:F12")
for c in range(3, 6):
    tm.cell(12, c).border = thin

tm["A14"] = "Working agreements (edit)"
tm["A14"].font = arial_b
agreements = [
    "Decisions: recorded in a shared log within 24 hours of the meeting.",
    "Missed work: tell the group before the deadline; another member covers and hours are rebalanced here.",
    "Client contact: one named person speaks to the client so messages stay consistent.",
    "No live ID photos on production until the data-protection row is closed.",
    "Code vs project: FECO301 hours go to analysis, landlords, tests, ethics — not Flutter.",
]
for i, a in enumerate(agreements):
    tm.cell(15 + i, 1, i + 1)
    tm.cell(15 + i, 2, a)
    tm.merge_cells(start_row=15 + i, start_column=2, end_row=15 + i, end_column=6)
    tm.cell(15 + i, 2).font = arial
    tm.cell(15 + i, 2).fill = fill_yellow
    tm.cell(15 + i, 2).alignment = wrap
    tm.row_dimensions[15 + i].height = 22

tm.column_dimensions["A"].width = 6
tm.column_dimensions["B"].width = 22
tm.column_dimensions["C"].width = 32
tm.column_dimensions["D"].width = 22
tm.column_dimensions["E"].width = 20
tm.column_dimensions["F"].width = 40

# ───────────────────────────────────────── Learning goals
lg = wb.create_sheet("Learning goals")
lg["A1"] = "Two personal learning goals and two professional activities per student"
lg["A1"].font = arial_title
lg.merge_cells("A1:F1")
lg["A2"] = "Replace the example wording. Pull names from the Team sheet."
lg["A2"].font = arial_small

for i, h in enumerate(
    ["Student (from Team)", "Learning goal 1", "Learning goal 2", "Professional activity 1", "Professional activity 2"],
    1,
):
    c = lg.cell(4, i, h)
    c.font = arial_h
    c.fill = fill_header
    c.border = thin
    c.alignment = center

examples_g = [
    "Run landlord interviews without leading the answers",
    "Write a one-page charter an assessor can mark",
]
examples_a = [
    "Moderate one usability session",
    "Keep the RAID log for two weeks",
]

for i in range(6):
    r = 5 + i
    lg.cell(r, 1, f"=Team!B{5+i}")
    lg.cell(r, 1).font = arial_link
    lg.cell(r, 2, examples_g[0] if i == 0 else "")
    lg.cell(r, 3, examples_g[1] if i == 0 else "")
    lg.cell(r, 4, examples_a[0] if i == 0 else "")
    lg.cell(r, 5, examples_a[1] if i == 0 else "")
    for c in range(1, 6):
        lg.cell(r, c).border = thin
        lg.cell(r, c).alignment = wrap
        if c > 1:
            lg.cell(r, c).fill = fill_yellow
            lg.cell(r, c).font = arial_input
    lg.row_dimensions[r].height = 36

lg.column_dimensions["A"].width = 22
for col in "BCDE":
    lg.column_dimensions[col].width = 38

# ───────────────────────────────────────── Skills
sk = wb.create_sheet("Skills self-assessment")
sk["A1"] = "Initial self-assessment — seven Professional Skills rows"
sk["A1"].font = arial_title
sk.merge_cells("A1:I1")
sk["A2"] = (
    "Labels below are placeholders. Replace row 4 with the exact seven names from the FECO301 rubric. "
    "Score 1 = not yet, 3 = developing, 5 = consistent. Yellow = each student. "
    "Team mean is a formula. This is the Week 3 baseline, not a grade."
)
sk["A2"].font = arial_small
sk.merge_cells("A2:I2")
sk.row_dimensions[2].height = 40

skills = [
    "1 Communication",
    "2 Collaboration",
    "3 Critical analysis",
    "4 Problem solving",
    "5 Professionalism & ethics",
    "6 Digital / tools",
    "7 Self-management",
]
sk["A4"] = "Student"
sk["A4"].font = arial_h
sk["A4"].fill = fill_header
sk["A4"].border = thin
for i, s in enumerate(skills):
    c = sk.cell(4, i + 2, s)
    c.font = arial_h
    c.fill = fill_header
    c.border = thin
    c.alignment = center

for i in range(6):
    r = 5 + i
    sk.cell(r, 1, f"=Team!B{5+i}")
    sk.cell(r, 1).font = arial_link
    sk.cell(r, 1).border = thin
    for c in range(2, 9):
        sk.cell(r, c, 3)  # example developing
        sk.cell(r, c).font = arial_input
        sk.cell(r, c).fill = fill_yellow
        sk.cell(r, c).border = thin
        sk.cell(r, c).alignment = center
        sk.cell(r, c).number_format = "0"

sk["A11"] = "Team mean"
sk["A11"].font = arial_b
sk["A11"].border = thin
for c in range(2, 9):
    col = get_column_letter(c)
    sk.cell(11, c, f"=AVERAGE({col}5:{col}10)")
    sk.cell(11, c).font = arial_formula
    sk.cell(11, c).border = thin
    sk.cell(11, c).number_format = "0.0"
    sk.cell(11, c).alignment = center

dv_score = DataValidation(type="whole", operator="between", formula1="1", formula2="5")
dv_score.add("B5:H10")
sk.add_data_validation(dv_score)

sk["A13"] = "Replace skill names if the module list differs. Keep seven columns. Re-score at close-out (Week 15) on a copy of this sheet."
sk["A13"].font = arial_small
sk.merge_cells("A13:I13")

sk.column_dimensions["A"].width = 22
for c in range(2, 9):
    sk.column_dimensions[get_column_letter(c)].width = 22

# print settings
for sheet in wb.worksheets:
    sheet.page_setup.orientation = "landscape"
    sheet.page_setup.fitToPage = True
    sheet.page_setup.fitToWidth = 1
    sheet.page_setup.fitToHeight = 1
    sheet.sheet_properties.pageSetUpPr.fitToPage = True
    sheet.page_setup.paperSize = sheet.PAPERSIZE_A4
    sheet.print_options.horizontalCentered = True
    sheet.page_setup.leftMargin = 0.4
    sheet.page_setup.rightMargin = 0.4
    sheet.page_setup.topMargin = 0.5
    sheet.page_setup.bottomMargin = 0.5
    apply_font_all(sheet)

wb.save(OUT)
print("Wrote", OUT)
