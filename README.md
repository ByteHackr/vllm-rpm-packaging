# vLLM RPM Packaging for Fedora

This repository contains RPM packaging files for [vLLM](https://github.com/vllm-project/vllm) to build packages for Fedora Linux via [Copr Build System](https://copr.fedorainfracloud.org/).

## Quick Start with Copr

### For End Users
```bash
# Add the Copr repository
sudo dnf copr enable bytehackr/vLLM

# Install vLLM
sudo dnf install python3-vllm
```

### For Copr Build System

**Copr Settings:**
- **Package name:** `python-vllm`
- **Source type:** SCM  
- **Clone URL:** `https://github.com/ByteHackr/vllm-rpm-packaging.git`
- **Spec file:** `vllm-simple.spec`
- **Build method:** `make srpm`

## Files

- **`.copr/Makefile`** - Tells Copr how to build the SRPM
- **`vllm-simple.spec`** - RPM spec file for CPU-only build
- **`README.md`** - This file

## License

Apache-2.0 (same as vLLM)
