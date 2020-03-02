FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

RUN addgroup -S appgroup && adduser -S pytest -G appgroup
USER pytest

WORKDIR /home/pytest

ADD . .

ENTRYPOINT ["python", "pytest.py"]
CMD []