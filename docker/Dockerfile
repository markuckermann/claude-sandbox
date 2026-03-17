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
    git \
    git-lfs \
    gh 

RUN git lfs install 

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


# Copy init script
COPY post_create.sh /usr/local/bin/post_create.sh
RUN chmod +x /usr/local/bin/post_create.sh

# Copy Claude skills
COPY claude-skills/ /home/agent/.claude/skills/
RUN chown -R agent:agent /home/agent/.claude/skills

# Create /build directory and set permissions
RUN mkdir -p /build && chown agent:agent /build
ENV ROOT_BUILD_DIR=/build

USER agent