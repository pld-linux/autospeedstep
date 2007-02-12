Summary:	autospeedstep controls the speed on Intel Speedstep CPUs
Summary(pl.UTF-8):	autospeedstep - kontrola szybkości procesorów Intel Speedstep
Name:		autospeedstep
Version:	0.2
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://gpsdrive.kraftvoll.at/%{name}-%{version}.tar.gz
# Source0-md5:	b3f22896dcb04cf269666e2d9060a654
URL:		http://gpsdrive.kraftvoll.at/speedstep.shtml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
autospeedstep is a daemon that controls power consumption and
processor speed depending of the CPU load. It works ONLY with Intel
Speedstep CPUs and Linux kernels running the 2.5 ACPI backport.

%description -l pl.UTF-8
autospeedstep to demon kontrolujący zużycie energii i szybkość
procesora w zależności od obciążenia. Działa TYLKO z procesorami
Intel Speedstep i jądrami Linuksa zawierającymi obsługę ACPI z serii
2.5.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(754,root,root) %{_sbindir}/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
