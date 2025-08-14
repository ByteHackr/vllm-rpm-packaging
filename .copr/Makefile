# Copr Makefile for vLLM package
# This file tells Copr how to build the SRPM

srpm:
	# Download the vLLM source
	curl -L -o vllm-0.10.0.tar.gz https://github.com/vllm-project/vllm/archive/v0.10.0.tar.gz
	
	# Create RPM build environment
	mkdir -p rpmbuild/{SOURCES,SPECS}
	
	# Copy source and spec file
	cp vllm-0.10.0.tar.gz rpmbuild/SOURCES/
	cp vllm-simple.spec rpmbuild/SPECS/vllm.spec
	
	# Build SRPM
	rpmbuild --define "_topdir $(PWD)/rpmbuild" -bs rpmbuild/SPECS/vllm.spec
	
	# Copy SRPM to expected location
	cp rpmbuild/SRPMS/*.src.rpm ./
