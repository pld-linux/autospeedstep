Summary:	autospeedstep controls the speed on Intel Speedstep CPUs
Summary(pl):	autospeedstep - kontrola szybko¶ci procesorów Intel Speedstep
Name:		autospeedstep
Version:	0.2
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://gpsdrive.kraftvoll.at/%{name}-%{version}.tar.gz
URL:		http://gpsdrive.kraftvoll.at/speedstep.shtml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
autospeedstep is a daemon that controls power consumption and
processor speed depending of the CPU load. It works ONLY with Intel
Speedstep CPUs and Linux kernels running the 2.5 ACPI backport.

%description -l pl
autospeedstep to demon kontroluj±cy zu¿ycie energii i szybko¶æ
procesora w zale¿no¶ci od obci±¿enia. Dzia³a TYLKO z procesorami
Intel Speedstep i j±drami Linuksa zawieraj±cymi obs³ugê ACPI z serii
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
