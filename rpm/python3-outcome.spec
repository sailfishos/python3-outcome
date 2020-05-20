Name:       python3-outcome
Summary:    Capture the outcome of Python function calls
Version:    1.0.1
Release:    1
License:    MIT or ASL 2.0
URL:        https://pypi.org/project/outcome/
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.bz2
Requires:   python3-base
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{summary}.
Extracted from the Trio project.

%prep
%setup -q -n %{name}-%{version}/outcome

%build
%py3_build

%install
rm -rf %{buildroot}
%py3_install

%files
%defattr(-,root,root,-)
%{python3_sitelib}/outcome
%{python3_sitelib}/outcome-*.egg-info
