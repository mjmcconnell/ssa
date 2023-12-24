# https://catalog.redhat.com/software/containers/ubi9/python-311
FROM registry.access.redhat.com/ubi9/python-311:1-41 as builder

ARG PIPENV_VENV_IN_PROJECT=1

USER 0

WORKDIR /opt/app-root/

RUN dnf update -y
RUN yum -y update-minimal --security --sec-severity=Important --sec-severity=Critical

RUN pip install pipenv==2023.11.15

### install dependencies
COPY Pipfile            ./Pipfile
COPY Pipfile.lock       ./Pipfile.lock

RUN pipenv install --deploy

# https://catalog.redhat.com/software/containers/ubi9/ubi-minimal
FROM registry.access.redhat.com/ubi9/ubi-minimal:9.3

MAINTAINER NAME mjmcconnell.dev@gmail.com

ARG user=1001

ENV PATH="/opt/app-root/.venv/bin:$PATH"
ENV PYTHONPATH="${PYTHONPATH}:/opt/app-root/src"

RUN INSTALL_PKGS="python311" && \
    microdnf \
      install -y --nodocs ${INSTALL_PKGS} && \
    microdnf clean all

WORKDIR /opt/app-root

COPY --from=builder /opt/app-root/.venv /opt/app-root/.venv

COPY src                                    /opt/app-root/src
COPY docker/cmds                            /opt/app-root

RUN chown -R ${user}:0 ./

USER ${user}
