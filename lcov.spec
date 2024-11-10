Summary:	LTP GCOV extension code coverage tool
Name:		lcov
Version:	2.2
Release:	1
Group:		Development/Other
License:	GPLv2
URL:		https://ltp.sourceforge.net/coverage/lcov.php
Source:		https://github.com/linux-test-project/lcov/releases/download/v%{version}/lcov-%{version}.tar.gz
BuildArch:	noarch

%description
LCOV is an extension of GCOV, a GNU tool which provides information
about what parts of a program are actually executed (i.e. "covered")
while running a particular test case. The extension consists of a set
of PERL scripts which build on the textual GCOV output to implement
HTML output and support for large projects.

%prep
%autosetup -p1

%build

%install
%make_install DESTDIR=$RPM_BUILD_ROOT BIN_DIR=%{_bindir} MAN_DIR=%{_mandir} CFG_DIR=%{_sysconfdir}
chmod -x $RPM_BUILD_ROOT%{_sysconfdir}/lcovrc

%files
%config(noreplace) %{_sysconfdir}/lcovrc
%{_bindir}/*
%{_mandir}/man*/*
