# check=skip=SecretsUsedInArgOrEnv
FROM docker/sandbox-templates:claude-code

USER root

# Install system packages
RUN apt-get update -y && apt-get install -y \
    build-essential \
    mingw-w64 \
    srecord \
    cmake \
    curl \
    libgl1 \
    libglib2.0-0 \
    neovim \
    gh 

# Install clang-tidy and clang-format from LLVM apt repos
ARG LLVM_VERSION=21
RUN apt-get update -y && apt-get -y install \
    lsb-release \
    software-properties-common \
    gnupg \
    && curl -fsSL https://apt.llvm.org/llvm.sh -o /tmp/llvm.sh \
    && chmod +x /tmp/llvm.sh \
    && /tmp/llvm.sh ${LLVM_VERSION} \
    && apt-get -y install clang-format-${LLVM_VERSION} clang-tidy-${LLVM_VERSION} \
    && ln -sf /usr/bin/clang-format-${LLVM_VERSION} /usr/bin/clang-format \
    && ln -sf /usr/bin/clang-tidy-${LLVM_VERSION} /usr/bin/clang-tidy \
    && ln -sf /usr/bin/run-clang-tidy-${LLVM_VERSION} /usr/bin/run-clang-tidy \
    && rm /tmp/llvm.sh 

RUN uv python install 3.13.9


# Setting up tokens
ARG CLAUDE_CODE_OAUTH_TOKEN
ENV CLAUDE_CODE_OAUTH_TOKEN=$CLAUDE_CODE_OAUTH_TOKEN

ARG GH_TOKEN
ENV GH_TOKEN=$GH_TOKEN


USER agent

# Copy and register init script
USER root
COPY shell_init.sh /usr/local/bin/shell_init.sh
RUN chmod +x /usr/local/bin/shell_init.sh \
    && echo '. /usr/local/bin/shell_init.sh' >> /etc/sandbox-persistent.sh

# Copy Claude skills
COPY claude-skills/ /home/agent/.claude/skills/
RUN chown -R agent:agent /home/agent/.claude/skills

USER agent