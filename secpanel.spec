Summary:	Visual management of SSH connections
Summary(pl):	Wizualna nakładka na klienta SSH
Name:		secpanel
Version:	0.32
Release:	1
License:	GPL
Group:		X11/Utilities
Source0:	http://www.pingx.net/secpanel/%{name}-%{version}.tar.gz
Requires:	tcl
URL:		http://www.pingx.net/secpanel/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	tcl

%description
SecPanel serves as a graphical user interface for managing and running SSH
(Secure Shell) and SCP (Secure Copy) connections.
Note: SecPanel is not a new implementation of the SecureShell protocol or
the ssh software-suite sh software-suite.

%description -l pl
SecPanel jest graficznym interfejsem pozwalającym uruchamiać i zarządzać
sesjami SSH(Secure Shell) i SCP (Secure Copy).
Uwaga: SecPanel nie jest nową implementacją protokołu SecureShell.

%prep
%setup -q

%build

%install
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_libdir}/secpanel}

cp src/bin/secpanel $RPM_BUILD_ROOT%{_sbindir}
cp -r src/lib/secpanel/* $RPM_BUILD_ROOT%{_libdir}/secpanel

gzip -9nf README CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}
%attr(755,root,root) %{_libdir}/secpanel/listserver.tcl
%{_libdir}/secpanel/secpanel*
%%attr(644,root,root)  %{_libdir}/secpanel/images 

%doc *.gz
