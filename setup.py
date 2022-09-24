
from distutils.core import setup
setup(
  name = 'caladan',         # How you named your package folder (MyLib)
  packages = ['caladan'],   # Chose the same as "name"
  version = '0.0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Python library for processing satetile images.',   # Give a short description about your library
  author = 'Caladan Team',                   # Type in your name
  author_email = 'caladan@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/The-AI-Book/caladan.git',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/The-AI-Book/caladan.git/archive/refs/tags/0.0.1.tar.gz',    # I explain this later on
  keywords = ['SATETILE', 'IMAGES'],   # Keywords that define your package best
  
  install_requires=[       
          'numpy',
          'pandas',
          'requests',
          'urllib3',
          'caladan', 
          "pyspark", 
          "osgeo"
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.9',
  ],
)