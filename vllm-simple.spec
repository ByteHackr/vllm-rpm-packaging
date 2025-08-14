# Simplified RPM spec file for vLLM - CPU-only initial package
%global srcname vllm

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
BuildRequires:  python3-torch
BuildRequires:  python3-jinja2
BuildRequires:  python3-packaging
BuildRequires:  python3-regex

%description
vLLM is a fast and easy-to-use library for LLM inference and serving.
This package provides CPU-only inference capabilities.

%package -n python3-%{srcname}
Summary:        %{summary}
Requires:       python3-torch
Requires:       python3-numpy
Requires:       python3-requests

%description -n python3-%{srcname}
vLLM is a fast and easy-to-use library for LLM inference and serving.

%prep
%autosetup -n %{srcname}-%{version}

%build
export VLLM_TARGET_DEVICE=cpu
%py3_build

%install
export VLLM_TARGET_DEVICE=cpu
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.dist-info/
%{_bindir}/vllm

%changelog
* Mon Jan 27 2025 Fedora Packager <packager@fedora.org> - 0.10.0-1
- Initial simplified package for Fedora
