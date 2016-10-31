PKG_NAME := jdk-bonecp
URL := https://repo1.maven.org/maven2/com/jolbox/bonecp/0.8.0.RELEASE/bonecp-0.8.0.RELEASE.jar
ARCHIVES := https://repo1.maven.org/maven2/com/jolbox/bonecp/0.8.0.RELEASE/bonecp-0.8.0.RELEASE.pom %{buildroot}

include ../common/Makefile.common
