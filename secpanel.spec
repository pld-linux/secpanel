Summary:	Visual management of SSH connections
Summary(pl):	Wizualna nakładka na klienta SSH
Name:		secpanel
Version:	0.41
Release:	2
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://www.pingx.net/secpanel/%{name}-%{version}.tar.gz
# Source0-md5:	3d0df052986506edd05905be854c2a3a
Source1:	%{name}.desktop
URL:		http://www.pingx.net/secpanel/
Requires:	tcl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SecPanel serves as a graphical user interface for managing and running
SSH (Secure Shell) and SCP (Secure Copy) connections. Note: SecPanel
is not a new implementation of the SecureShell protocol or the ssh
software-suite sh software-suite.

%description -l pl
SecPanel jest graficznym interfejsem pozwalającym uruchamiać i
zarządzać sesjami SSH (Secure Shell) i SCP (Secure Copy). Uwaga:
SecPanel nie jest nową implementacją protokołu SecureShell.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/secpanel,%{_applnkdir}/Network/Communications}

install src/bin/secpanel $RPM_BUILD_ROOT%{_bindir}
cp -r src/lib/secpanel/* $RPM_BUILD_ROOT%{_libdir}/secpanel
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/secpanel
%attr(755,root,root) %{_libdir}/secpanel/listserver.tcl
%attr(755,root,root) %{_libdir}/secpanel/secpanel*
%{_libdir}/secpanel/convert_history.tcl
%{_libdir}/secpanel/gui.tcl
%{_libdir}/secpanel/keydistribute.tcl
%{_libdir}/secpanel/default*
%{_libdir}/secpanel/images
%{_applnkdir}/Network/Communications/*.desktop
