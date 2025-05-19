FROM python:3.12-slim

# Install dependencies
RUN pip install docker requests pyyaml

WORKDIR /app
COPY . /app
RUN chmod +x entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
