%define name	slay
%define Name	Slay
%define version	1.2
%define release	16

Name:		%{name}
Version:	%{version}
Release:	1
Summary:	Utility to kill all processes belonging to a user
Source:		%{Name}-%{version}.tar.bz2
License:	GPL
Group:		Monitoring
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Obsoletes:	Slay
Provides:	Slay
BuildArch:	noarch

%description 
Slay sends given signal (KILL by default) to all processes belonging to user(s)
given on the command line. 

%prep
%setup -q -n %{Name}-%{version}

%build
# do nothing

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
install -m 755 slay %{buildroot}/%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Slay.1.2.lsm
%{_bindir}/slay



%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.2-15mdv2010.0
+ Revision: 433924
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.2-14mdv2009.0
+ Revision: 260786
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.2-13mdv2009.0
+ Revision: 252565
- rebuild
- fix no-buildroot-tag
- fix description-line-too-long

* Thu Dec 20 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.2-11mdv2008.1
+ Revision: 136009
- rebuild

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - import slay


* Tue Aug 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.2-10mdv2007.0
- %%mkrel
- clean buildroot before installation

* Thu Jul 28 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.2-9mdk 
- spec cleanup

* Fri Jul 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.2-8mdk 
- rebuild

* Mon Sep 08 2003 Guillaume Rousse <guillomovitch@linux-mandrake.com> 1.2-7mdk
- capitalization sux
- removed implicit requires

* Thu Jan 30 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.2-6mdk
- rebuild

* Thu Feb 28 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.2-5mdk
- rebuild

* Tue Mar 13 2001 Jeff Garzik <jgarzik@mandrakesoft.com> 1.2-4mdk
- This package is not arch specific, declare it noarch.

* Fri Mar  9 2001 Jeff Garzik <jgarzik@mandrakesoft.com> 1.2-3mdk
- add docs
- fix rpmlint warnings

* Mon Jul 31 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.2-2mdk
- macros
- clean spec

* Thu Jul 07 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.2-1mdk
- new in contribs
- here to celebrate the resurrection of the well known "titi sucks script"

* Thu Jul 7 2000 Bryan Paxton <evil7@bellsouth.net> 
- Initial build
