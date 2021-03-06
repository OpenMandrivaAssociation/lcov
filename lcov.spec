Summary:	LTP GCOV extension code coverage tool
Name:		lcov
Version:	1.14
Release:	1
Group:		Development/Other
License:	GPLv2
URL:		http://ltp.sourceforge.net/coverage/lcov.php
Source:		https://sourceforge.net/projects/ltp/files/Coverage%20Analysis/LCOV-%{version}/lcov-%{version}.tar.gz
BuildArch:	noarch

%description
LCOV is an extension of GCOV, a GNU tool which provides information
about what parts of a program are actually executed (i.e. "covered")
while running a particular test case. The extension consists of a set
of PERL scripts which build on the textual GCOV output to implement
HTML output and support for large projects.

%prep
%setup -q

%build

%install
%makeinstall PREFIX=%{buildroot}
chmod -x %{buildroot}%{_sysconfdir}/lcovrc

%clean

%files
%config(noreplace) %{_sysconfdir}/lcovrc
%{_bindir}/*
%{_mandir}/man*/*


