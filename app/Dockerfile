FROM python:3.9

WORKDIR /app

#Need this for custom modules
ENV PYTHONPATH /app/

#Set up virtual environment
ENV VIRTUAL_ENV=/opt/venv

RUN python -m venv $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

#Install dependencies
COPY ./requirements.txt /app/requirements.txt

RUN pip3 install --upgrade pip

RUN pip3 install --no-cache-dir --upgrade -r /app/requirements.txt

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

#Copy source code
COPY ./ /app/

RUN cd /app

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]