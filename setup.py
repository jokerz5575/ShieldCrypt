from distutils.core import setup
setup(
  name = 'ShieldCrypt',        
  packages = ['ShieldCrypt'],   
  version = '0.1',     
  license='GPL-3.0',       
  description = 'Encrypt and Decrypt, Store keys, with AES',   # Give a short description about your library
  author = 'jokerz5575',                   # Type in your name
  author_email = 'peterschmidt5575@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/jokerz/shieldcrypt',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/jokerz5575/ShieldCrypt/archive/refs/tags/Beta.tar.gz',    # I explain this later on
  keywords = ['python3', 'encryption', 'AES'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'cryptography'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Developers',    
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',  
    'Programming Language :: Python :: 3',     
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11'
  ],
)