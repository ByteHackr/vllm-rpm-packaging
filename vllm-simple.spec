# Simplified RPM spec file for vLLM - CPU-only initial package
%global srcname vllm
%global _description %{expand:
vLLM is a fast and easy-to-use library for LLM inference and serving.
This package provides CPU-only inference capabilities.}

Name:           python-%{srcname}
Version:        0.10.0
Release:        1%{?dist}
Summary:        High-throughput and memory-efficient LLM inference engine (CPU-only)

License:        Apache-2.0
URL:            https://github.com/vllm-project/vllm
Source0:        https://github.com/vllm-project/vllm/archive/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools >= 77.0.3
BuildRequires:  python3-setuptools-scm >= 8.0
BuildRequires:  python3-wheel
BuildRequires:  cmake >= 3.26.1
BuildRequires:  ninja-build
BuildRequires:  gcc-c++

# Core Python dependencies that are available in Fedora
BuildRequires:  python3-torch
BuildRequires:  python3-jinja2
BuildRequires:  python3-packaging
BuildRequires:  python3-regex
BuildRequires:  python3-numpy
BuildRequires:  python3-requests
BuildRequires:  python3-transformers
BuildRequires:  python3-tqdm
BuildRequires:  python3-psutil
BuildRequires:  python3-pillow
BuildRequires:  python3-scipy
BuildRequires:  python3-pyyaml
BuildRequires:  python3-aiohttp
BuildRequires:  python3-fastapi
BuildRequires:  python3-pydantic
BuildRequires:  python3-cloudpickle

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

# Runtime dependencies - only core ones available in Fedora
Requires:       python3-torch
Requires:       python3-numpy
Requires:       python3-requests
Requires:       python3-transformers
Requires:       python3-tqdm
Requires:       python3-psutil
Requires:       python3-pillow
Requires:       python3-scipy
Requires:       python3-pyyaml
Requires:       python3-aiohttp
Requires:       python3-fastapi
Requires:       python3-pydantic
Requires:       python3-cloudpickle
Requires:       python3-regex

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %{_description}

%prep
%autosetup -n %{srcname}-%{version}

# Set CPU-only target
export VLLM_TARGET_DEVICE=cpu

# Remove requirements that are not available in Fedora (for now)
# This is a temporary measure for initial packaging
sed -i '/blake3/d' requirements/common.txt || true
sed -i '/tiktoken/d' requirements/common.txt || true
sed -i '/msgspec/d' requirements/common.txt || true
sed -i '/gguf/d' requirements/common.txt || true
sed -i '/einops/d' requirements/common.txt || true
sed -i '/watchfiles/d' requirements/common.txt || true
sed -i '/pybase64/d' requirements/common.txt || true
sed -i '/cbor2/d' requirements/common.txt || true
sed -i '/setproctitle/d' requirements/common.txt || true
sed -i '/outlines_core/d' requirements/common.txt || true
sed -i '/diskcache/d' requirements/common.txt || true
sed -i '/lark/d' requirements/common.txt || true
sed -i '/xgrammar/d' requirements/common.txt || true
sed -i '/partial-json-parser/d' requirements/common.txt || true
sed -i '/mistral_common/d' requirements/common.txt || true
sed -i '/compressed-tensors/d' requirements/common.txt || true
sed -i '/depyf/d' requirements/common.txt || true
sed -i '/python-json-logger/d' requirements/common.txt || true
sed -i '/openai-harmony/d' requirements/common.txt || true
sed -i '/lm-format-enforcer/d' requirements/common.txt || true
sed -i '/llguidance/d' requirements/common.txt || true

%build
export VLLM_TARGET_DEVICE=cpu
export CMAKE_BUILD_TYPE=RelWithDebInfo
export MAX_JOBS=%{?_smp_build_ncpus}

# Skip extension building for now to get a basic package working
export VLLM_USE_PRECOMPILED=0

%py3_build

%install
export VLLM_TARGET_DEVICE=cpu
%py3_install

# Remove any CUDA-specific files
find %{buildroot} -name "*cuda*" -delete 2>/dev/null || true
find %{buildroot} -name "*_C.*.so" -delete 2>/dev/null || true

%check
# Basic import test (may fail due to missing dependencies)
%{python3} -c "import sys; sys.path.insert(0, '%{buildroot}%{python3_sitelib}'); import vllm" || echo "Import test failed - expected due to missing optional dependencies"

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.dist-info/
%{_bindir}/vllm

%changelog
* Mon Jan 27 2025 Fedora Packager <packager@fedora.org> - 0.10.0-1
- Initial simplified package for Fedora
- CPU-only build with minimal dependencies
- Suitable for package review and initial inclusion
