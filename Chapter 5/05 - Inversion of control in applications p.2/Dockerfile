FROM python:3.11-slim
WORKDIR app

RUN pip install Flask redis


ADD *.py ./
CMD python3 tracking.py --reload