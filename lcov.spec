%define name	lcov
%define version	1.9
%define release	2

Summary:	LTP GCOV extension code coverage tool
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Development/Other
License:	GPLv2
URL:		http://ltp.sourceforge.net/coverage/lcov.php
Source:		http://ltp.sourceforge.net/coverage/tools/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
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


%changelog
* Sun Oct 24 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.9-1mdv2011.0
+ Revision: 588021
- new version 1.9

* Sun Mar 07 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.8-1mdv2010.1
+ Revision: 515524
- update to 1.8

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.6-4mdv2010.0
+ Revision: 429706
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 1.6-3mdv2009.0
+ Revision: 248328
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Oct 22 2007 Pascal Terjan <pterjan@mandriva.org> 1.6-1mdv2008.1
+ Revision: 101355
- 1.6

* Fri Jul 20 2007 Pascal Terjan <pterjan@mandriva.org> 1.5-1mdv2008.0
+ Revision: 53920
- Import lcov



* Fri Jul 20 2007 Pascal Terjan <pterjan@mandriva.org> 1.5-1mdv2008.0
- 1.5

* Mon May 09 2005 Pascal Terjan <pterjan@mandriva.org> 1.4-1mdk
- First Mandriva version
