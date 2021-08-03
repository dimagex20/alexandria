FROM python:3.8

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get -y install --no-install-recommends \
      libpq-dev=9.6.22-0+deb9u1 \
      g++=4:6.3.0-4 \
      gcc=4:6.3.0-4 && \
    rm -rf /var/cache/apt /var/lib/apt/lists && \
    groupadd -g 4321 alexandria && \
    useradd -ms /bin/bash alexandria -g alexandria -u 4321

USER alexandria
WORKDIR /home/alexandria

COPY --chown=alexandria:xpvx . .

RUN python -m pip install --upgrade pip --no-cache-dir && \
    pip install --no-cache-dir -r requirements.txt

WORKDIR /home/alexandria/alexandria

CMD ["/home/alexandria/.local/bin/gunicorn", "--bind", "0.0.0.0:8000", "-w", "3", "-m", "007", "alexandria.wsgi"]
