#FROM python:3.7-alpine
FROM python:3.9.9-bullseye

# Version to use
ARG TESLA_CE_PROVIDER_VERSION

# Define the TeSLA CE package to install
ARG TESLA_CE_PROVIDER_PACKAGE="tesla-ce-provider-ks-tks==$TESLA_CE_PROVIDER_VERSION"

# Install build deps, then run `pip install`, then remove unneeded build deps all in a single step. Correct the path to your production requirements file, if needed.
RUN apt-get update && apt-get install nano -y

RUN python3 -m venv /venv \
    && /venv/bin/pip install -U pip \
    && /venv/bin/pip install --no-cache-dir $TESLA_CE_PROVIDER_PACKAGE

# Prepare environment
ENV PROVIDER_CLASS=tks.TKSProvider
ENV PROVIDER_VERSION=$TESLA_CE_PROVIDER_VERSION

# Create a user and group for Celery
RUN addgroup celery && \
    useradd -g celery celery && \
    usermod -a -G celery celery


ADD docker/check_health.sh /venv/bin/check_health.sh
RUN chmod +x /venv/bin/check_health.sh

USER celery

CMD ["/venv/bin/celery", "-A", "tesla_ce_provider", "worker", "-l", "warning", "-O", "fair"]
HEALTHCHECK --start-period=15s --retries=3 CMD "/venv/bin/check_health.sh"
ENTRYPOINT ["/venv/bin/python"]
