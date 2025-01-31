import openai
from resumePDF import create_pdf
# from generatePDF import generate_pdf
from score import get_resume_match_score
from utils import create_prompt, extract_json_from_text 


def generate_resume(prompt: str, resume_content: str, tone: str, language: str,
                        key_words: str = "", additional_info: str = None, missing_skills: str=None) -> str:
        """
        Generates a resume using OpenAI API.

        Parameters:
        ----------
        - prompt (str): Instruction for the AI model.
        - resume_content (str): The current resume content.
        - tone (str): Tone of the resume (e.g., professional, conversational).
        - language (str): Language of the resume.
        - key_words (str): Keywords extracted from the job description.
        - additional_info (str): Any additional information provided by the user.

        Returns:
        -------
        - str: The generated resume content.
        """
        messages = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": f"""
            User's Resume:
            {resume_content}
            Job Description:
            {job_description}
            Job Description Keywords:
            {key_words}
            Tone to be applied:
            {tone}
            Language of the new resume:
            {language}
            User's Additional Information:
            {additional_info}
            Missing skills:
            {missing_skills}
            """}
        ]

        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            max_tokens=4000
        )
        return response.choices[0].message.content
    

def extract_keywords_ai(prompt: str, job_description) -> str:
        """
        Extracts keywords from the job description using OpenAI API.

        Parameters:
        ----------
        - prompt (str): The prompt to extract keywords.

        Returns:
        -------
        - str: The extracted keywords as a string.
        """
        messages = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": job_description}
        ]

        response = openai.chat.completions.create(
            model='gpt-4o',
            messages=messages,
            max_tokens=600
        )

        # Return the response content directly or extract keywords from it
        return response.choices[0].message.content.strip()


system_prompt = create_prompt("generate_resume_prompt.txt")
keywords_prompt = create_prompt("keywords_prompt.txt")

job_description = """
Skip to main content
careers

Sign In
Search for Jobs

Software Development Engineer III page is loaded
Software Development Engineer III
Apply
Software Development Engineer III
Apply
locations
Washington - Seattle Campus
time type
Full time
posted on
Posted Today
time left to apply
End Date: March 31, 2025 (30+ days left to apply)
job requisition id
R-93674
Expedia Group brands power global travel for everyone, everywhere. We design cutting-edge tech to make travel smoother and more memorable, and we create groundbreaking solutions for our partners. Our diverse, vibrant, and welcoming community is essential in driving our success.

Why Join Us?

To shape the future of travel, people must come first. Guided by our Values and Leadership Agreements, we foster an open culture where everyone belongs, differences are celebrated and know that when one of us wins, we all win.

We provide a full benefits package, including exciting travel perks, generous time-off, parental leave, a global hybrid work setup (with some pretty cool offices), and career development resources, all to fuel our employees' passion for travel and ensure a rewarding career journey. We’re building a more open world. Join us.

Software Development Engineer III 

 

Meet the Team!

The Air Connectivity Organization at Expedia Group is seeking an experienced backend developer passionate about building robust, scalable, and high-performance applications that help millions of people plan their travels and create lifelong memories. Join us as we revolutionize the travel industry! 

The Air Connectivity Organization at Expedia Group is at the forefront of innovation in the travel industry. We leverage our cutting-edge, in-house platform to seamlessly integrate with airlines worldwide, delivering exceptional travel experiences to millions of users annually. Through APIs that adhere to NDC standards, we enable travelers to access top-tier content, enjoy an immersive ticket shopping experience, and add convenient ancillaries to their journeys with ease. 

We are part of the partner connectivity platform that serves as the backbone of Expedia’s business, powering an efficient two-way marketplace that bridges supply and demand. Leveraging diverse integration methods—ranging from direct connections to NDC and GDS sourcing—our platform processes over 50 Tier-1 services and generates more than 8TB of data each month. Built with modern technologies like Java, Kotlin, Spring, MSSQL, DynamoDB, and Redis, our ecosystem supports millions of travelers in finding the best travel products tailored to their needs. 

What Sets Us Apart 

Global Scale: We operate a platform that impacts millions of users worldwide, making air travel more accessible, seamless, and personalized. 

Innovation-Driven: We thrive on solving complex challenges, continuously improving our technology stack, and staying ahead in the fast-paced travel industry. 

Collaborative Culture: Our geographically distributed team is empowered to drive high-priority initiatives independently while fostering a culture of collaboration, inclusivity, and shared success. 

If you’re passionate about creating transformative solutions, tackling large-scale engineering challenges, and shaping the future of air travel, we’d love to have you on our team. Join us, and let’s redefine the way the world travels together! 

 

 

What You'll Do

Lead design and implement products and solutions that are highly scalable with high-quality, clean, maintainable, and well-documented code.  

Find opportunities for process and technology improvements, and work towards adoption and implementation. 

Assist with supporting Production systems (includes investigating issues and working towards resolution) 

Exercise creativity and provide alternative solutions to a given problem removing roadblocks and driving issues to closure 

Create/update documentation for the purpose of sharing knowledge between team members 

Actively participate in group technology reviews to critique the work of self and others 

Participate and formulate user story creation in partnership with the team, product managers.  

Closely collaborate with Senior and Principal Developers, as well as the Product Manager, to find effective solutions to problems. 

 

 Who You Are

Bachelor's or Master’s in a related technical field; or equivalent related professional experience 
4+ years of experience with Bachelor's degree or 3+ years with Master’s degree 

A high performing individual contributor who acts as a mentor to more junior engineers, applies new engineering principles to improve existing systems, and is responsible for complex, well-defined projects. 

Worked on projects based on Java or Kotlin  

Good understanding of OOPS Concepts, SOLID Principles, Domain driven design systems. 

Designed and Create REST APIs for your projects 

Demonstrates the ability to select among technology available to implement and solve. 

Able to understand and design moderately complex systems 

Implemented code that uses both relational and non-relational data stores. You understand the difference between a data store and a cache and have experience using both 

Have a solid understanding of code promotion, CI/CD methodologies, and using Git for source control. Splunk / Datadog integration for logging / metrics 

Experience with cloud-computing platforms such as Amazon Web Services 

Understanding of testing and monitoring tools 

Ability to debug applications 

Have experience working in an agile team environment conducting code walkthroughs, peer reviews, and producing user documentation 

Maintained projects in production environments (bug fixing, troubleshooting, monitoring etc.) 

Understanding how teams’ goals fit a business need. 

 

 

The total cash range for this position in Seattle is $137,500.00 to $192,500.00. Employees in this role have the potential to increase their pay up to $220,000.00, which is the top of the range, based on ongoing, demonstrated, and sustained performance in the role.
Starting pay for this role will vary based on multiple factors, including location, available budget, and an individual’s knowledge, skills, and experience. Pay ranges may be modified in the future.

Accommodation requests

If you need assistance with any part of the application or recruiting process due to a disability, or other physical or mental health conditions, please reach out to our Recruiting Accommodations Team through the Accommodation Request.

We are proud to be named as a Best Place to Work on Glassdoor in 2024 and be recognized for award-winning culture by organizations like Forbes, TIME, Disability:IN, and others.

Expedia Group's family of brands includes: Brand Expedia®, Hotels.com®, Expedia® Partner Solutions, Vrbo®, trivago®, Orbitz®, Travelocity®, Hotwire®, Wotif®, ebookers®, CheapTickets®, Expedia Group™ Media Solutions, Expedia Local Expert®, CarRentals.com™, and Expedia Cruises™. © 2024 Expedia, Inc. All rights reserved. Trademarks and logos are the property of their respective owners. CST: 2029030-50

Employment opportunities and job offers at Expedia Group will always come from Expedia Group’s Talent Acquisition and hiring teams. Never provide sensitive, personal information to someone unless you’re confident who the recipient is. Expedia Group does not extend job offers via email or any other messaging tools to individuals with whom we have not made prior contact. Our email domain is @expediagroup.com. The official website to find and apply for job openings at Expedia Group is careers.expediagroup.com/jobs.

Expedia is committed to creating an inclusive work environment with a diverse workforce. All qualified applicants will receive consideration for employment without regard to race, color, religion, gender, gender identity or expression, sexual orientation, national origin, genetics, disability, age, or veteran status. This employer participates in E-Verify. The employer will provide the Social Security Administration (SSA) and, if necessary, the Department of Homeland Security (DHS) with information from each new employee's I-9 to confirm work authorization.
About Us
Logo
Expedia Group (NASDAQ: EXPE) powers travel for everyone, everywhere through our global platform. Driven by the core belief that travel is a force for good, we help people experience the world in new ways and build lasting connections. We provide industry-leading technology solutions to fuel partner growth and success, while facilitating memorable experiences for travelers. Expedia Group's family of brands includes: Brand Expedia®, Hotels.com®, Expedia® Partner Solutions, Vrbo®, trivago®, Orbitz®, Travelocity®, Hotwire®, Wotif®, ebookers®, CheapTickets®, Expedia Group™ Media Solutions, Expedia Local Expert®, CarRentals.com™, and Expedia Cruises™.

For more information, visit  www.expediagroup.com.

Employment opportunities and job offers at Expedia Group will always come from Expedia Group’s Talent Acquisition and hiring teams. Never provide sensitive, personal information to someone unless you’re confident who the recipient is. Expedia Group does not extend job offers via email or any other messaging tools to individuals to whom we have not made prior contact. Our email domain is @expediagroup.com. The official website to find and apply for job openings at Expedia Group is lifeatexpediagroup.com/jobs.


Read More
Follow Us
Privacy Policy
© 2025 Workday, Inc. All rights reserved.


"""

resume = """
GIRIPRANAY KONA
Dallas, TX
+1-469-583-9601 giripranay.kona@gmail.com linkedin.com/in/giripranaykona/
OBJECTIVE
Experienced Software Engineer with 5 years of experience specializing in full-stack development and cloud computing.
Successfully developed a 'Know Your Food' mobile app and automated a system for downloading SDS PDFs, significantly
improving efficiency. Adept at building scalable applications and deploying solutions in cloud environments. Seeking to
leverage expertise in software engineering to contribute to innovative projects and dynamic teams.
EDUCATION
University of Texas, Dallas Aug 2022 - May 2024
Master of Computer Science, Data Science
Indian Institute of Information Technology, Sricity Aug 2015 - May 2019
Bachelor of Science, Electronics and Communication
SKILLS
• Programming Languages: Java, Python, JavaScript, TypeScript, C++, Dart, SQL, Bash
• Frontend: HTML, CSS, React, Angular, Bootstrap, jQuery, Flutter, Figma
• Backend: Nodejs, Express.js, Spring Boot, Django, Flask, PHP
• Cloud and DevOps: AWS, Azure, Google Cloud, Docker, Kubernetes, Nginx, Firebase, OpenShift, CI/CD with Jenkins, terraform,
lambda, distributed system, cloud computing
• Databases: MySQL, PostgreSQL, MongoDB, Redis, Cassandra, DBSCAN, DynamoDB, Oracle
• APIs and Microservices: RESTful APIs, APHqDB, Microservices Architecture, OAuth2, JWT
• Data Processing: Apache Kafka, Apache Spark, Pandas, NumPy, Elasticsearch, Zookeeper
• Version Control: Git, GitHub, GitLab, Bitbucket, Perforce, SVN, CI/CD integration, code reviews
• Core Concepts: Computer Science, Software Development, Programming, Algorithm Design, Debugging, Back-End Web Development, Data Structures, Object-Oriented Programming (OOP), Software Testing, UNIX, LINUX
EXPERIENCE
Erik Johnson School of Engineering and Computer Science May 2023 - May 2024
Software Engineer Dallas, TX
• Developed and automated a system for downloading SDS PDFs using Node.js, reducing manual effort by 50% and improving overall
efficiency.
• Built and deployed RESTful APIs using Node.js and Express.js, ensuring smooth data flow and integration with frontend systems.
• Implemented asynchronous programming paradigms using Promises, async/await, and event-driven architectures, enhancing application responsiveness and performance
• Extracted data from dynamic and static web pages using Puppeteer, Selenium, BeautifulSoup, and Scrapy, efficiently handling
challenges like CAPTCHAs, pagination, and JavaScript-rendered content
The Live Green Company Oct 2020 - Aug 2022
Sr. Software Developer Bengaluru, India
• Spearheaded the development of the 'Know Your Food' mobile app, managing everything from wireframe design to infrastructure setup,
which enhanced user engagement. Implemented Firebase for real-time data storage, set up a Django server on Google Cloud for API
management, and configured an Nginx proxy server to efficiently handle incoming requests
• Created dynamic and user-friendly web applications with React, which improved user satisfaction and engagement by enhancing UI/UX
• Developed an API that accepts images as input, integrates with the Google Vision API to extract text, and processes food label images
to isolate and retrieve the ingredients section, streamlining data extraction for improved efficiency
• Built cross-platform mobile applications using Flutter and Dart, enhancing app performance for Android and iOS platforms. Managed
state with Provider and Bloc, integrated RESTful APIs, and implemented Firebase for real-time data synchronization
• Innovated the 'Food Analyzer' tool, resulting in a 75% increase in research productivity among food researchers
• Designed and deployed scalable microservices using Docker and Kubernetes, managing containerized applications on AWS and GCP
to improve scalability, system reliability, and availability.
Dvara Solutions May 2019 - Sep 2020
Software Developer Bengapuru, India
• Developed and maintained RESTful APIs and microservices with SpringBoot, ensuring scalable, efficient backend services.
• Optimized complex SQL queries using joins, subqueries, CTEs, and window functions for efficient data retrieval and manipulation in
MySQL and PostgreSQL, leading to faster query execution and improved database performance
• Debugged and resolved frontend issues in AngularJS applications using browser developer tools, improving user experience by
inspecting DOM, network requests, and JavaScript performance
PROJECTS
University of Texas, Dallas
Visualization with Spark Streaming, Kafka, Elasticsearch, and Kibana
• Developed a Python application that continuously fetched real-time data from sources like Reddit and ingested this information into
Apache Kafka.
• Utilized PySpark Structured Streaming to process the data, extract named entities, and maintain a running count.
• Triggered periodic updates to another Kafka topic with the counts of the named entities.
• Configured Logstash, Elasticsearch, and Kibana to visualize the top 10 most frequent named entities using bar plots.
"""


result = get_resume_match_score(job_description, resume)

response = generate_resume(system_prompt,resume,"Expert", 'English', result['keywords'], result['suggestions'], '.'.join(result['missing_skills']))


resume = extract_json_from_text(response)


print(create_pdf(resume, "PDFs/weasy_resume.pdf", ['Experiences', 'Education', 'Skills', 'Projects'] , color_code="#000000"))