FROM python
WORKDIR /weather_web_proj
COPY ./ /weather_web_proj
RUN pip install -r requirements.txt
EXPOSE 8081
CMD gunicorn --bind 0.0.0.0:8081 webpage:app
