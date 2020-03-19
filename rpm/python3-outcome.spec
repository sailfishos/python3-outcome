# fixme: should be defined in base system side
%define python3_sitearch %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")

Name:       python3-outcome
Summary:    Capture the outcome of Python function calls
Version:    1.0.1
Release:    1
License:    MIT or ASL 2.0
URL:        https://pypi.org/project/outcome/
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.bz2
Requires:   python3-base
BuildRequires:  python3-setuptools

%description
%{summary}.
Extracted from the Trio project.

%prep
%setup -q -n %{name}-%{version}/outcome

%build
python3 ./setup.py build

%install
rm -rf %{buildroot}
python3 ./setup.py install --skip-build --root %{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitearch}/outcome
%{python3_sitearch}/outcome-*.egg-info
