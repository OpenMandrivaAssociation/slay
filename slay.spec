%define name	slay
%define Name	Slay
%define version	1.2
%define release	%mkrel 11

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Utility to kill all processes belonging to a user
Source:		%{Name}-%{version}.tar.bz2
License:	GPL
Group:		Monitoring
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

