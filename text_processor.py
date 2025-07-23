# text_processor.py
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download NLTK data if not already present
try:
    stopwords.words('english')
except LookupError:
    import nltk

    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('wordnet')
    nltk.download('omw-1.4')

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))


def preprocess_text(text):
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    # Remove mentions and hashtags
    text = re.sub(r'@\w+|#\w+', '', text)
    # Keep letters, numbers, dots, plus and dash
    text = re.sub(r'[^a-zA-Z0-9\s\.\+\-]', '', text)
    # Convert to lowercase
    text = text.lower()
    # Tokenize
    tokens = word_tokenize(text)
    # Remove stop words and lemmatize
    processed_tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return " ".join(processed_tokens)


def extract_skills_from_text(text):
    # This is a very basic rule-based skill extraction.
    # For a real application, you'd use a pre-trained NER model (e.g., SpaCy's 'en_core_web_lg' or a custom one)
    # or a comprehensive skill dictionary.

    # Expanded and refined common skills list
    common_skills = [
        "python", "java", "javascript", "react", "node.js", "sql", "aws", "docker",
        "kubernetes", "machine learning", "data analysis", "project management",
        "agile", "scrum", "communication", "leadership", "figma", "photoshop",
        "seo", "marketing", "finance", "hr", "sales", "engineering", "design",
        "cloud", "devops", "backend", "backend", "fullstack", "ui/ux", "data science",
        "artificial intelligence", "cybersecurity", "network", "database", "mobile development",
        "android", "ios", "web development", "content creation", "social media",
        "public relations", "brand management", "market research", "financial analysis",
        "accounting", "auditing", "investment", "recruitment", "employee relations",
        "training", "supply chain", "logistics", "operations management", "product management",
        "business development", "customer service", "technical support", "graphic design",
        "illustration", "video editing", "animation", "autocad", "solidworks",
        "excel", "powerpoint", "word", "microsoft office", "google suite", "tableau", "power bi",
        "sas", "r", "c++", "c#", "go", "ruby", "php", "swift", "kotlin", "typescript",
        "spring", "hibernate", "angular", "vue.js", "django", "flask", "laravel", "symfony",
        "express.js", "mongodb", "postgresql", "mysql", "oracle", "redis", "cassandra",
        "azure", "gcp", "terraform", "ansible", "jenkins", "gitlab ci", "jira", "confluence",
        "salesforce", "sap", "erp", "crm", "qa", "testing", "automation", "manual testing",
        "api", "rest", "graphql", "microservices", "blockchain", "iot", "robotics",
        "natural language processing", "computer vision", "deep learning", "neural networks",
        "statistical analysis", "quantitative analysis", "risk management", "compliance",
        "budgeting", "forecasting", "financial reporting", "tax preparation", "auditing",
        "talent acquisition", "employee engagement", "performance management", "compensation & benefits",
        "organizational development", "change management", "negotiation", "client management",
        "lead generation", "cold calling", "sales strategy", "customer relationship management",
        "autocad", "solidworks", "catia", "revit", "bim", "fea", "cfd", "matlab", "simulink",
        "circuit design", "embedded systems", "firmware", "hardware", "manufacturing processes",
        "supply chain optimization", "inventory management", "logistics planning",
        "user research", "wireframing", "prototyping", "usability testing", "information architecture",
        "interaction design", "visual design", "brand identity", "print design", "digital art",
        "video production", "motion graphics", "3d modeling", "maya", "blender", "cinema 4d",
        "content strategy", "copywriting", "editing", "proofreading", "storytelling",
        "email marketing", "ppc", "google analytics", "social media marketing", "influencer marketing",
        "public speaking", "presentation skills", "problem-solving", "critical thinking",
        "adaptability", "teamwork", "collaboration", "creativity", "innovation", "attention to detail"
    ]

    found_skills = []
    processed_text = text.lower()  # Ensure text is lowercased for matching

    for skill in common_skills:
        # Use word boundaries to avoid partial matches (e.g., 'hr' matching 'shred')
        # Added more robust regex for common variations (e.g., "node js", "node.js")
        if re.search(r'\b' + re.escape(skill).replace('\.', '[\.\s]?') + r'\b', processed_text):
            found_skills.append(skill.replace('.', ''))  # Clean up for display

    return list(set(found_skills))  # Return unique skills


def categorize_resume(text):
    text = text.lower()

    categories = {
        "Tech": ["software", "developer", "engineer", "python", "java", "javascript", "react", "node.js",
                 "sql", "aws", "cloud", "devops", "kubernetes", "machine learning", "data science",
                 "artificial intelligence", "cybersecurity", "network", "database", "backend", "backend",
                 "fullstack", "mobile development", "android", "ios", "web development", "algorithm",
                 "api", "microservices", "agile", "scrum", "git", "linux", "windows server", "azure", "gcp",
                 "programming", "development", "coding", "django", "flask", "typescript", "c++", "c#", "go",
                 "ruby", "php", "swift", "kotlin", "rest", "graphql", "blockchain", "iot", "nlp", "computer vision",
                 "deep learning", "neural networks", "big data", "hadoop", "spark", "kafka", "etl", "data warehousing",
                 "business intelligence", "devsecops", "site reliability engineer", "sre", "qa engineer", "test automation"],
        "Marketing": ["marketing", "seo", "sem", "content", "social media", "brand", "campaign",
                      "public relations", "pr", "advertisement", "analytics", "market research",
                      "digital marketing", "email marketing", "crm", "google ads", "facebook ads",
                      "copywriting", "strategy", "advertising", "ppc", "google analytics", "influencer marketing",
                      "content strategy", "storytelling", "media planning", "demand generation", "lead generation"],
        "Design": ["design", "ui/ux", "graphic", "photoshop", "illustrator", "figma", "sketch",
                   "adobe xd", "portfolio", "visual", "creative", "typography", "branding",
                   "user experience", "user interface", "web design", "product design", "animation",
                   "ux designer", "ui designer", "interaction design", "motion graphics", "3d modeling",
                   "industrial design", "fashion design", "interior design", "architectural design"],
        "Finance": ["finance", "accounting", "audit", "financial analysis", "investment", "banking",
                    "tax", "economics", "portfolio", "cpa", "cfa", "bookkeeping", "budget", "forecasting",
                    "risk management", "compliance", "financial reporting", "treasury", "corporate finance",
                    "wealth management", "financial planning", "equity research", "fixed income"],
        "HR": ["hr", "human resources", "recruitment", "talent acquisition", "employee relations",
               "onboarding", "payroll", "benefits", "hrms", "workforce", "compensation", "training",
               "organizational development", "performance management", "employee engagement", "hr business partner",
               "diversity and inclusion", "learning and development"],
        "Sales": ["sales", "business development", "account management", "client relations", "crm",
                  "negotiation", "lead generation", "quota", "revenue", "customer acquisition",
                  "sales strategy", "cold calling", "sales operations", "channel sales", "enterprise sales",
                  "solution selling", "key account management"],
        "Engineering": ["engineer", "mechanical", "electrical", "civil", "chemical", "aerospace",
                        "cad", "autocad", "solidworks", "matlab", "simulation", "design", "manufacturing",
                        "r&d", "research and development", "structural", "systems", "mechatronics",
                        "robotics", "automation", "circuit design", "embedded systems", "firmware", "hardware design",
                        "process engineering", "quality engineering", "industrial engineering", "biomedical engineering"],
        "Social Media": ["social media", "instagram", "facebook", "twitter", "linkedin", "tiktok",
                         "community management", "influencer", "content creation", "engagement", "hootsuite", "buffer",
                         "social media strategy", "social media marketing", "platform management", "online community"],
        "Operations": ["operations", "logistics", "supply chain", "procurement", "inventory management",
                       "process improvement", "lean manufacturing", "six sigma", "quality control",
                       "project management office", "pmo", "business operations", "operational excellence"],
        "Healthcare": ["healthcare", "medical", "clinical", "nurse", "doctor", "physician", "hospital",
                       "patient care", "pharmacist", "biotechnology", "pharmaceutical", "research", "dentist",
                       "therapist", "public health", "epidemiology", "health administration"],
        "Education": ["education", "teacher", "professor", "instructor", "curriculum development",
                      "e-learning", "academic advising", "student affairs", "higher education", "k-12",
                      "educational technology", "tutoring", "training development"],
        "Customer Service": ["customer service", "customer support", "client support", "help desk",
                             "technical support", "call center", "customer relations", "service desk",
                             "customer success", "client success", "support specialist"],
        "Legal": ["legal", "law", "attorney", "lawyer", "paralegal", "litigation", "corporate law",
                  "compliance", "intellectual property", "contract law", "legal research", "juris", "esq"],
        "Project Management": ["project management", "pmp", "scrum master", "agile coach", "product owner",
                               "program management", "portfolio management", "jira", "confluence", "trello",
                               "asana", "risk management", "stakeholder management", "budget management"]
    }

    # Check for category matches
    for category, keywords_list in categories.items():
        for keyword in keywords_list:
            if re.search(r'\b' + re.escape(keyword) + r'\b', text):
                return category

    # If no specific category matches, try to infer from general terms
    if any(k in text for k in ["analyst", "consultant", "specialist", "manager", "coordinator"]):
        return "Other"

    return "Uncategorized"

