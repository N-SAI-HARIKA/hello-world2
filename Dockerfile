# 1. Python
# 2. Packages
# 3. All the files in the current directory
# 4. Streamlit run app.py


# Pull base image from official Python image
FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["streamlit", "run", "app.py" ]
