from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def cv_context():
    context = {
        'name': 'Linyi He',
        'linkedin': 'LinkedIn',
        'phone': '(206) 660-5737',
        'email': 'lh1505@nyu.edu',
        
        'education': [
            {
                'school': 'New York University',
                'degree': 'Master in Computer Science',
                'location': 'New York, NY',
                'period': '01/2024 – 05/2026'
            },
            {
                'school': 'Northeastern University',
                'degree': 'Master in Informatics',
                'location': 'Boston, MA',
                'period': '04/2019 - 12/2020'
            },
            {
                'school': 'University of Washington',
                'degree': 'Bachelor in Mathematics',
                'location': 'Seattle, WA',
                'period': '09/2012 - 08/2016'
            }
        ],
        
        'skills': [
            'Java', 'JavaScript', 'C++', 'C', 'Database Management', 'Kubernetes',
            'SQL Server', 'MySQL', 'PostgreSQL', 'MongoDB', 'GitLab CI',
            'Docker', 'GKE', 'AKS', 'Flux', 'Argo', 'Helm', 'Terraform',
            'R programming', 'Tableau', 'Excel', 'PowerBI', 'Python'
        ],
        
        'certification': 'CKA (Certified Kubernetes Administrator)',
        
        'professional_experience': [
            {
                'company': 'Concentrix Corporation',
                'title': 'DevOps Engineer / Database Administrator',
                'location': 'Farmington Hills, MI',
                'period': '04/2021 - Present',
                'projects': [
                    {
                        'name': 'Oncall management platform',
                        'details': [
                            'Led the deployment of Concentrix\'s first on-call management platform using ReactJS and Express within the Backstage Portal',
                            'Integrated PostgreSQL database with Crunchy Data operator within the Kubernetes environment on the GKE cluster',
                            'Set up alerts to monitor real-time system performance and health using Prometheus, Grafana and Alertmanager',
                            'Integrated Keycloak for secure user authn/authz and OAuth with Azure AD'
                        ]
                    },
                    {
                        'name': 'Community contribution',
                        'details': [
                            'Maintained cloud infrastructure on AWS/GCP/Azure using Terraform',
                            'Managed, monitored and optimized over 400 databases',
                            'Collaborated on database setup and design for key projects',
                            'Handled daily maintenance and operations'
                        ]
                    }
                ]
            },
            {
                'company': 'Analytics Consult LLC.',
                'title': 'Intern, Application Developer',
                'location': 'Boston, MA',
                'period': '07/2020 - 01/2021',
                'projects': [
                    {
                        'name': 'Development',
                        'details': [
                            'Conducted development and design of MyVrends and UBoostUs mobile applications',
                            'Designed and built user-friendly interfaces using React Native',
                            'Designed the database structure and managed data operations using SQL Server and Firebase'
                        ]
                    }
                ]
            }
        ],
        
        'other_experience': [
            {
                'title': 'Software Developer (Project Team Member) | TechCompare Web Application',
                'location': 'New York, NY',
                'details': [
                    'Collaborated in a team of 5 to develop "TechCompare" web app using ReactJS and Spring Boot',
                    'Built a responsive front-end with ReactJS and Tailwind CSS',
                    'Developed a robust back end with Spring Boot',
                    'Implemented user authentication with Amazon Cognito',
                    'Integrated Stripe API for e-commerce features',
                    'Conducted testing and debugging using Docker and Google Cloud Platform'
                ]
            }
        ]
    }
    return context

def cv_view(request):
    context = cv_context()
    return render(request, "render/index.html", context)
