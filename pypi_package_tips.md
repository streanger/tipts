
### build and upload commands

- install dependencies: `pip install twine wheel`
- to build package localy: `python setup.py bdist_wheel`
- to check dist before upload: `python -m twine check dist/*`
- to upload package to test pypi: `python -m twine upload --repository testpypi dist/*`
- to upload package to pypi: `python -m twine upload dist/*`
- to install localy: `python setup.py install`
- to install with pip: `pip install package_name`
- to update dist: `python setup.py sdist`
- to create dist in specified format: `python setup.py sdist --formats=gztar,zip`

### related stuff
- if you want to add non-python files to dist, include it in MANIFEST.in. Example below:
```
# Include the data files
recursive-include happy_couple/lines_only *
recursive-include happy_couple/sounds *
```
- if you want to add non-python file to site-packages directory in your python, specify it in setup.py. Example below:
```
'happy_couple': ['sounds/smb_jump.wav', 'lines_only/small_head.png'],	# for single file
'happy_couple': images + sounds,					# for predefined list of files
```
- https://dzone.com/articles/executable-package-pip-install
- line -> scripts=["justi"],	in setup.py caused Permission denied Errno 13; remove this line
