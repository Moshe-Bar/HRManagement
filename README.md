## Installation

Install HRManagement with git

```bash
  git clone https://github.com/Moshe-Bar/HRManagement.git
  cd HRManagement
  git init 
  git fetch
  git checkout db_models
  
```
## Deployment

To deploy this project run

first time windows:
```bash
  python -m venv venv
  .\venv\Scripts\activate
  pip install requirements.txt
```
first time linux:
```bash
  python3 -m venv venv
  source venv/bin/activate
  pip install requirements.txt
```
run in windows:
```bash
    python manage.py runserver
```
run in linux:
```bash
    python3 manage.py runserver
```