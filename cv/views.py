from django.conf import settings

from django_pdf_view.pdf import PDF
from django_pdf_view.views import PDFView


class CVPDFView(PDFView):

    def create_pdf(self) -> PDF:
        pdf = PDF(
            title='CV | Miloš Roknić',
            filename='CV-Milos-Roknic-08-2024.pdf',
        )

        pdf.add_page(
            template_name='cv/cv.html',
            context=self._get_first_page_context(),
        )

        return pdf

    def _get_first_page_context(self):
        address_url = (
            'https://www.google.rs/maps/place/Kornelija+Stankovi%C4%87a+39,'
            '+Novi+Sad/@45.2600114,19.8085096,15.91z/data=!4m6!3m5!1s0x475b'
            '11b16298fc2d:0xa5444cbbc3bf8f26!8m2!3d45.2605492!4d19.8103612!'
            '16s%2Fg%2F11fx0qw3pz?hl=hr&entry=ttu'
        )
        avatar_url = self.request.build_absolute_uri(
            f'{settings.STATIC_URL}cv/img/milos-roknic.png'
        )
        about_me = (
            'After completing programming courses and internships at two '
            'companies, I secured a permanent Software Engineer role in the '
            'second one, working primarily with PHP technologies. I later '
            'transitioned to Python/Django and led two internal hackathon '
            'projects in the past two years. I also gained experience with '
            'Docker, CI tools, testing frameworks and mentored colleagues '
            'and students in Python/Django and React. I also took on a '
            'Development Lead role, managing six colleagues\' career '
            'progression.'
        )
        employments = [
            {
                'title': 'Software Engineer & Development Lead',
                'company': 'Vega IT',
                'from': 'Aug 2023',
                'until': 'Present',
                'location': 'Novi Sad, Serbia',
                'description': (
                    'In Aug 2023, I assumed the role of Development Lead, '
                    'taking on the responsibility of managing the career '
                    'progression and work satisfaction of six colleagues. '
                    'In addition the mentioned duties, I continued to work on '
                    'Python/Django and Next.js projects while also gaining '
                    'significant experience with Cypress in one of my latest '
                    'projects. I also continued mentoring colleagues and '
                    'students in Python/Django and React, while my experience '
                    'with Docker and various CI tools has further grown '
                    'during this period.'
                )
            },
            {
                'title': 'Software Engineer',
                'company': 'Vega IT',
                'from': 'Jan 2019',
                'until': 'Aug 2023',
                'location': 'Novi Sad, Serbia',
                'description': (
                    'During this period, I began my journey as a Software '
                    'Engineer, where I initially worked extensively with PHP '
                    'technologies, including Drupal, WordPress, and Symfony. '
                    'After the first one and a half years, I transitioned to '
                    'working on Python/Django and Next.js projects, a focus '
                    'that spanned over four years. In addition to my '
                    'development work, I took on leadership roles in two '
                    'internal hackathon projects and mentored colleagues and '
                    'students in Python/Django and React. I also gained '
                    'valuable experience with Docker and various CI tools. '
                    'For the last three years of this period, I exclusively '
                    'worked on Ubuntu, solidifying my proficiency with this '
                    'operating system.'
                )
            }
        ]
        links = [
            {
                'label': 'LinkedIn',
                'url': (
                    'https://www.linkedin.com/in/'
                    'milo%C5%A1-rokni%C4%87-30853bb8/'
                ),
                'type': 'linkedin',
            },
            {
                'label': 'GitHub',
                'url': 'https://github.com/roknicmilos',
                'type': 'github',
            },
        ]
        return {
            'avatar_url': avatar_url,
            'first_name': 'Miloš',
            'last_name': 'Roknić',
            'role': 'Software Engineer',
            'email': 'roknic.milos.994@gmail.com',
            'phone': '+385638455742',
            'address': {
                'label': 'Kornelija Stankovića 39, Novi Sad, 21000, Serbia',
                'url': address_url
            },
            'about_me': about_me,
            'employments': employments,
            'links': links,
        }
