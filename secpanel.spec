# TODO:
# - there is nothing binary in that package - maybe better put
#   it to %{datadir}, not %{libdir} ?
Summary:	Visual management of SSH connections
Summary(pl):	Wizualna nak³adka na klienta SSH
Name:		secpanel
Version:	0.4.3
Release:	4
Epoch:		1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://www.pingx.net/secpanel/%{name}-%{version}.tar.gz
# Source0-md5:	99f8e26f882e95399322e75ad777eacf
Source1:	%{name}.desktop
URL:		http://www.pingx.net/secpanel/
Requires:	tcl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		/usr/lib

%description
SecPanel serves as a graphical user interface for managing and running
SSH (Secure Shell) and SCP (Secure Copy) connections. Note: SecPanel
is not a new implementation of the SecureShell protocol or the ssh
software-suite.

%description -l pl
SecPanel jest graficznym interfejsem pozwalaj±cym uruchamiaæ i
zarz±dzaæ sesjami SSH (Secure Shell) i SCP (Secure Copy). Uwaga:
SecPanel nie jest now± implementacj± protoko³u SecureShell.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/secpanel,%{_desktopdir}}

install src/bin/secpanel $RPM_BUILD_ROOT%{_bindir}
cp -r src/lib/secpanel/* $RPM_BUILD_ROOT%{_libdir}/secpanel
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

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
%{_libdir}/secpanel/default*
%{_libdir}/secpanel/images
%{_desktopdir}/*.desktop
