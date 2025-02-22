import json
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, HRFlowable
from reportlab.lib.units import inch
from reportlab.lib.colors import black, gray

def generate_ats_friendly_pdf(resume_data, output_filename="Professional_Resume.pdf"):
    """
    Generates a comprehensive, professional PDF resume with multiple sections
    and a clean, modern design.
    """
    try:
        # Custom Styles
        styles = getSampleStyleSheet()
        
        # Name Style
        name_style = ParagraphStyle(
            'NameStyle',
            parent=styles['Title'],
            fontSize=16,
            textColor=black,
            alignment=TA_CENTER,
            spaceAfter=6
        )
        
        # Contact Info Style
        contact_style = ParagraphStyle(
            'ContactStyle',
            parent=styles['Normal'],
            alignment=TA_CENTER,
            fontSize=10,
            spaceAfter=12
        )
        
        # Section Header Style
        section_header_style = ParagraphStyle(
            'SectionHeader',
            parent=styles['Heading2'],
            borderBottomWidth=1,
            borderBottomColor=gray,
            borderBottomPadding=3,
            spaceAfter=6,
            fontSize=12,
            textColor=black
        )
        
        # Job/Education Entry Style
        entry_header_style = ParagraphStyle(
            'EntryHeader',
            parent=styles['Normal'],
            fontSize=10,
            textColor=black,
            spaceAfter=2
        )
        
        # Job Description Style
        description_style = ParagraphStyle(
            'Description',
            parent=styles['Normal'],
            fontSize=9,
            textColor=black,
            spaceAfter=6
        )
        
        # Create PDF document
        doc = SimpleDocTemplate(
            output_filename, 
            pagesize=letter, 
            leftMargin=0.5*inch, 
            rightMargin=0.5*inch, 
            topMargin=0.5*inch, 
            bottomMargin=0.5*inch
        )
        
        content = []
        
        # Name and Job Title
        content.append(Paragraph(resume_data['user_information']['name'], name_style))
        content.append(Paragraph(resume_data['user_information']['main_job_title'], contact_style))
        
        # Contact Information
        contact_info = f"{resume_data['user_information']['email']} | " + \
                       f"LinkedIn: {resume_data['user_information']['linkedin']} | "  + \
                       f" {resume_data['user_information']['location']} | " 
                    #    f"GitHub: {resume_data['user_information'].get('github', 'N/A')}"
        content.append(Paragraph(contact_info, contact_style))
        
        content.append(Spacer(1, 6))
        content.append(HRFlowable(width="100%", thickness=0.5, color=gray))
        content.append(Spacer(1, 12))
        
        # Profile Summary
        content.append(Paragraph("PROFESSIONAL SUMMARY", section_header_style))
        content.append(Paragraph(resume_data['user_information']['profile_description'], description_style))
        content.append(Spacer(1, 6))
        
        # Work Experience
        content.append(Paragraph("PROFESSIONAL EXPERIENCE", section_header_style))
        for exp in resume_data["user_information"]["experiences"]:
            # Job Title and Company
            job_header = f"{exp['job_title']}, {exp['company']} | {exp['start_date']} - {exp['end_date']}"
            content.append(Paragraph(job_header, entry_header_style))
            
            # Job Tasks
            for task in exp["four_tasks"]:
                content.append(Paragraph(f"• {task}", description_style))
            content.append(Spacer(1, 6))
        
        # Education
        content.append(Paragraph("EDUCATION", section_header_style))
        for edu in resume_data["user_information"]["education"]:
            # Degree and Institution
            edu_header = f"{edu['degree']}, {edu['institution']} | {edu['start_date']} - {edu['end_date']}"
            content.append(Paragraph(edu_header, entry_header_style))
            content.append(Paragraph(edu['description'], description_style))
            content.append(Spacer(1, 6))
        
        # Skills
        content.append(Paragraph("TECHNICAL SKILLS", section_header_style))
        hard_skills = " • ".join(resume_data["user_information"]["skills"]["hard_skills"])
        soft_skills = " • ".join(resume_data["user_information"]["skills"].get("soft_skills", []))
        
        content.append(Paragraph(f"Hard Skills: • {hard_skills}", description_style))
        content.append(Paragraph(f"Soft Skills: • {soft_skills}", description_style))
        content.append(Spacer(1, 6))
        
        # Projects
        if resume_data.get("projects"):
            content.append(Paragraph("PROJECTS", section_header_style))
            for project in resume_data["projects"]:
                project_header = f"{project['project_name']}"
                content.append(Paragraph(project_header, entry_header_style))
                
                for goal in project["two_goals_of_the_project"]:
                    content.append(Paragraph(f"• {goal}", description_style))
                
                content.append(Paragraph(f"Result: {project['project_end_result']}", description_style))
                content.append(Spacer(1, 6))
        
        # # Certificates
        # if resume_data.get("certificate"):
        #     content.append(Paragraph("CERTIFICATIONS", section_header_style))
        #     for cert in resume_data["certificate"]:
        #         cert_header = f"{cert['name']}, {cert['institution']} | {cert['date']}"
        #         content.append(Paragraph(cert_header, entry_header_style))
        #         content.append(Paragraph(cert['description'], description_style))
        #         content.append(Spacer(1, 6))
        
        # # Extra-Curricular Activities
        # if resume_data.get("extra_curricular_activities"):
        #     content.append(Paragraph("EXTRA-CURRICULAR ACTIVITIES", section_header_style))
        #     for activity in resume_data["extra_curricular_activities"]:
        #         content.append(Paragraph(activity['name'], entry_header_style))
        #         content.append(Paragraph(activity['description'], description_style))
        #         content.append(Spacer(1, 6))
        
        # # Hobbies
        # if resume_data["user_information"].get("hobbies"):
        #     content.append(Paragraph("INTERESTS", section_header_style))
        #     hobbies = " • ".join(resume_data["user_information"]["hobbies"])
        #     content.append(Paragraph(f"• {hobbies}", description_style))
        
        # Build the PDF
        doc.build(content)
        
        print(f"✅ Comprehensive Professional PDF Resume successfully generated: {output_filename}")
        return True
    
    except Exception as e:
        print(f"❌ Failed to generate PDF: {e}")
        return False

# Uncomment to generate resume
# Example Usage
# with open("test.json", "r") as file:
#     resume_data = json.load(file)

# result = generate_ats_friendly_pdf(resume_data)
# print(result)  # True if successful, False if failed