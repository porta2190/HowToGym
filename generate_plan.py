from pathlib import Path

from fpdf import FPDF


class PlanPDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 18)
        self.set_text_color(0, 168, 167)
        self.cell(0, 10, "HOW TO GYM", align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_font("Helvetica", "", 9)
        self.set_text_color(100, 100, 100)
        self.cell(0, 6, "Free Arm Workout Plan", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, "howtogym.com  |  For personal use only", align="C")


pdf = PlanPDF()
pdf.set_auto_page_break(auto=True, margin=20)
pdf.add_page()

pdf.set_font("Helvetica", "B", 14)
pdf.set_text_color(30, 30, 30)
pdf.cell(0, 10, "Free Arm Workout Plan", new_x="LMARGIN", new_y="NEXT")
pdf.ln(2)

pdf.set_font("Helvetica", "", 10)
pdf.set_text_color(60, 60, 60)
intro = (
    "Welcome to How To Gym! This free arm workout targets your biceps, triceps, "
    "and shoulders in one focused session. Use it as a standalone workout or add "
    "it to your existing training split. Rest 60-90 seconds between sets."
)
pdf.multi_cell(0, 5, intro)
pdf.ln(4)

sections = [
    ("WHAT YOU NEED", [
        "Dumbbells (moderate weight)",
        "Cable machine or resistance band (optional)",
        "Bench or sturdy chair",
        "15-20 minutes total",
    ]),
    ("WARM-UP (5 MIN)", [
        "30 sec arm circles (forward and backward)",
        "15 band pull-aparts or light rows",
        "10 push-ups (knees if needed)",
        "10 light dumbbell curls (warm-up weight)",
    ]),
    ("THE WORKOUT", [
        "1. Dumbbell Bicep Curl         3 sets x 10-12 reps   Rest 60s",
        "2. Overhead Tricep Extension   3 sets x 10-12 reps   Rest 60s",
        "3. Hammer Curl                 3 sets x 10-12 reps   Rest 60s",
        "4. Tricep Kickback             3 sets x 12-15 reps   Rest 60s",
        "5. Lateral Raise               3 sets x 12-15 reps   Rest 60s",
        "6. Alternating Curl            2 sets x 10/arm      Rest 60s",
    ]),
    ("EXERCISE NOTES", [
        "Bicep Curl: Elbows pinned at sides, full range of motion, no swinging.",
        "Overhead Extension: Keep elbows close to head, lower weight behind head.",
        "Hammer Curl: Neutral grip (palms facing each other), control the descent.",
        "Tricep Kickback: Hinge forward, upper arm parallel to floor, extend fully.",
        "Lateral Raise: Slight bend in elbows, raise to shoulder height, slow lower.",
        "Alternating Curl: One arm at a time, squeeze at the top of each rep.",
    ]),
    ("HOW TO PROGRESS", [
        "Week 1: Focus on form, use a weight you can control for all reps.",
        "Week 2: Add 1-2 reps per set before increasing weight.",
        "Week 3: Increase weight when you hit the top of the rep range easily.",
        "Repeat this workout 1-2x per week with at least 48 hours between sessions.",
    ]),
    ("COOL-DOWN", [
        "30 sec cross-body shoulder stretch each arm",
        "30 sec overhead tricep stretch each arm",
        "30 sec doorway chest stretch",
    ]),
    ("WANT A CUSTOM PLAN?", [
        "This arm workout is a sample of what How To Gym offers.",
        "For a fully personalized workout and nutrition plan built around",
        "your goals, equipment, and schedule, visit howtogym.com",
    ]),
]

for title, lines in sections:
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(0, 168, 167)
    pdf.cell(0, 8, title, new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(50, 50, 50)
    for line in lines:
        pdf.cell(0, 5, line, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)

out = Path(__file__).parent / "downloads" / "how-to-gym-arm-workout-plan.pdf"
out.parent.mkdir(exist_ok=True)
pdf.output(str(out))
print("PDF created")