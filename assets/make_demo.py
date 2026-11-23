"""One-off demo document for LEGALGUARD 2.0 with MADE-UP data. Written to the scratchpad only."""
import sys
from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_COLOR_INDEX

out = sys.argv[1]
d = Document()
d.styles["Normal"].font.name = "Calibri"
d.styles["Normal"].font.size = Pt(10.5)
sec = d.sections[0]
sec.header.paragraphs[0].text = "FICTIONAL DEMO - all names, legal rules and data are synthetic"
sec.footer.paragraphs[0].text = "Demo only. Fictional legal rules. Not legal advice."


def table(rows, header=True):
    t = d.add_table(rows=len(rows), cols=len(rows[0]))
    t.style = "Light Grid Accent 1"
    for i, r in enumerate(rows):
        for j, v in enumerate(r):
            cell = t.cell(i, j)
            cell.text = v
            if header and i == 0:
                cell.paragraphs[0].runs[0].bold = True
    d.add_paragraph()


def label(p, text, colour):
    r = p.add_run(f" [{text}]")
    r.bold = True
    r.font.color.rgb = colour


GREEN, BLUE, RED = RGBColor(0x1E, 0x7B, 0x34), RGBColor(0x1F, 0x4E, 0x99), RGBColor(0xB0, 0x24, 0x18)

d.add_heading("LEGALGUARD 2.0 - Demo", level=0)
d.add_paragraph("Company: Sunrise Nutrition Pvt Ltd (fictional). Laws: the \"Demo Food Labelling Rules\" and "
                "\"Demo Claims Rules\" (fictional for illustration only). Approver: the company's legal lead.")
d.add_paragraph("This demonstration uses fictional rules and provisions. It does not quote or interpret Indian law and must not be used to make a real compliance decision.")

# 1 ----------------------------------------------------------------
d.add_heading("1. Ask a compliance question", level=1)
p = d.add_paragraph()
p.add_run("Question: ").bold = True
p.add_run("Can we print \"boosts immunity\" on our new vitamin C gummy label?")
p = d.add_paragraph()
p.add_run("Answer: ").bold = True
p.add_run("Only if the claim is on the approved claims list or has prior approval. "
          "\"Boosts immunity\" is not on the list, so it should not be printed without approval.")
p = d.add_paragraph(style="List Bullet")
p.add_run("Demo Claims Rules, rule 6(1): \"No health claim shall be made unless it appears in Schedule II "
          "or has been approved by the Authority.\"")
label(p, "QUOTE MATCHED", GREEN)
p = d.add_paragraph(style="List Bullet")
p.add_run("Schedule II lists \"supports normal immune function\" for vitamin C, not \"boosts immunity\". "
          "The listed wording is the safer option.")
label(p, "INTERPRETATION - relies on rule 6(1) and Schedule II", BLUE)
p = d.add_paragraph(style="List Bullet")
p.add_run("Whether a pending amendment widens the list.")
label(p, "UNVERIFIED - amendment not yet approved into the library", RED)
d.add_paragraph("All instruments, provisions, versions, and audit events shown in this demonstration are fictional.")

# 2 ----------------------------------------------------------------
d.add_heading("2. Weekly law watch", level=1)
table([["Found", "Source", "Status", "Next step"],
       ["Demo Labelling (Amendment) Rules, 2026: new allergen font size", "Official Gazette (demo)",
        "Waiting for approval", "Approver reviews the change pack"],
       ["Demo Claims Rules: no change", "Regulator website (demo)", "Unchanged", "-"]])
d.add_paragraph("Nothing enters the library until the approver says yes. The approval is recorded with name, "
                "date, decision and source.")

# 3 ----------------------------------------------------------------
d.add_heading("3. Compliance register (extract)", level=1).paragraph_format.page_break_before = True
table([["Product", "Obligation", "Provision", "Owner", "Status"],
       ["Vitamin C gummies", "Allergen statement on label", "Demo Labelling r.5(3)", "Regulatory", "Done"],
       ["Vitamin C gummies", "Use only listed health claims", "Demo Claims r.6(1)", "Marketing", "Open"],
       ["Whey protein 1 kg", "Licence number on label", "Demo Labelling r.4(2)", "Regulatory", "Done"]])

# 4 ----------------------------------------------------------------
d.add_heading("4. Contract review (redline extract)", level=1)
d.add_paragraph("Incoming: mutual NDA from Acme Packaging Ltd (made up). Clause 9 as marked up:")
p = d.add_paragraph()
p.add_run("9. Disputes. Disputes will be settled by arbitration ")
r = p.add_run("in the city chosen by Acme")
r.font.strike = True
r.font.color.rgb = RED
r = p.add_run("seated at Gurgaon, before a sole arbitrator, in English")
r.underline = True
r.font.color.rgb = BLUE
p.add_run(".")
p = d.add_paragraph()
r = p.add_run("Comment: One-sided seat. Company playbook position: fixed neutral seat.")
r.italic = True
r.font.highlight_color = WD_COLOR_INDEX.YELLOW
table([["#", "Clause", "Issue", "Severity", "Proposed fix"],
       ["1", "3", "Only marked documents are protected", "High", "Cover information obviously confidential"],
       ["2", "9", "Seat chosen by the other side", "High", "Fixed seat (Gurgaon)"],
       ["3", "-", "No personal-data clause", "Medium", "Insert standard clause"]])

# 5 ----------------------------------------------------------------
d.add_heading("5. Draft a contract from one line", level=1).paragraph_format.page_break_before = True
p = d.add_paragraph()
p.add_run("Instruction: ").bold = True
p.add_run("\"Draft a supply agreement for whey protein from a raw-material supplier.\"")
d.add_paragraph("Result: 32 clauses built from approved standard clauses, a product schedule, and this "
                "internal list at the end:")
for x in ["Clause 14 (Price): fill in [price per kg].",
          "Clause 22 (Liability): choose one option - Option A (cap of 2 x annual value); Option B (no cap).",
          "Schedule 1 (Product schedule): complete Quality limits, Shelf life.",
          "Not included - affiliates: ordering by group companies was not agreed."]:
    d.add_paragraph(x, style="List Bullet")

# 6 ----------------------------------------------------------------
d.add_heading("6. Audit trail", level=1)
table([["#", "Date", "Decision", "What", "By"],
       ["101", "02 Nov 2026", "APPROVED", "Demo Labelling Amendment 2026 into the library", "Legal lead"],
       ["102", "03 Nov 2026", "APPROVED", "Acme NDA redline sent to counterparty", "Legal lead"],
       ["103", "04 Nov 2026", "EDITED", "Whey supply draft: liability Option A chosen", "Legal lead"]])
d.add_paragraph("Every output: \"Draft for internal legal review. Not final advice.\" until lawyer sign-off.")
d.save(out)
print("saved", out)
