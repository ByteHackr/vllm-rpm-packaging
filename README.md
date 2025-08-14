# vLLM RPM Packaging for Fedora

This repository contains the RPM packaging files for building vLLM packages for Fedora.

## Files

- `vllm-simple.spec` - RPM spec file for vLLM (CPU-only version)
- `.copr/Makefile` - Build instructions for Copr Build System
- `build-rpm.sh` - Local build script for testing

## Building

### Using Copr (Recommended)

This repository is configured for use with [Copr Build System](https://copr.fedorainfracloud.org/). 

1. Fork this repository
2. Create a new project in Copr
3. Use "SCM" source type with "make srpm" build method
4. Point to your repository

### Local Building

```bash
# Install build dependencies
sudo dnf install rpm-build rpmdevtools rpmlint

# Run the build script
./build-rpm.sh
```

## Package Information

- **Package Name**: `python-vllm`
- **Version**: 0.10.0
- **Summary**: High-throughput and memory-efficient LLM inference engine (CPU-only)
- **License**: Apache-2.0
- **URL**: https://github.com/vllm-project/vllm

## Current Status

This is a simplified CPU-only build that focuses on getting a basic vLLM package into Fedora. Many optional dependencies are commented out to ensure compatibility with current Fedora repositories.

## Contributing

Feel free to submit issues and pull requests to improve the packaging.
