Summary:	Typing stubs for setuptools
Summary(pl.UTF-8):	Zaślepki typów dla modułu setuptools
Name:		python3-types-setuptools
Version:	80.9.0.20250529
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/types-setuptools/
Source0:	https://files.pythonhosted.org/packages/source/t/types-setuptools/types_setuptools-%{version}.tar.gz
# Source0-md5:	5675f98d7d6f12ab3ac5a07cddb3350a
URL:		https://pypi.org/project/types-setuptools/
BuildRequires:	python3-modules >= 1:3.9
BuildRequires:	python3-setuptools >= 1:77.0.3
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a PEP 561 type stub package for the setuptools package. It can
be used by type-checking tools like mypy, pyright, pytype, Pyre, etc.
to check code that uses setuptools.

%description -l pl.UTF-8
Ten pakiet zawiera zaślepki typów zgodne z PEP 561 dla pakietu
setuptools. Mogą one być używany przez narzędzia sprawdzające typy,
takie jak mypy, pyright, pytype, Pyre itp. do sprawdzania kodu
wykorzystującego setuptools.

%prep
%setup -q -n types_setuptools-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md README.md
%{py3_sitescriptdir}/distutils-stubs
%{py3_sitescriptdir}/setuptools-stubs
%{py3_sitescriptdir}/types_setuptools-%{version}-py*.egg-info
