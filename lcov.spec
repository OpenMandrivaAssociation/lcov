%define name	lcov
%define version	1.6
%define release	%mkrel 1

Summary:	LTP GCOV extension code coverage tool
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Development/Other
License:	GPL
URL:		http://ltp.sourceforge.net/coverage/lcov.php
Source:		http://ltp.sourceforge.net/coverage/tools/%{name}-%{version}.tar.gz
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
rm -rf $RPM_BUILD_ROOT
%makeinstall PREFIX=$RPM_BUILD_ROOT
chmod -x $RPM_BUILD_ROOT%{_sysconfdir}/lcovrc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/lcovrc
%{_bindir}/*
%{_mandir}/man*/*
