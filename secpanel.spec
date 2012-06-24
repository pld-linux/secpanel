Summary:	Visual management of SSH connections
Summary(pl):	Wizualna nak�adka na klienta SSH
Name:		secpanel
Version:	0.32
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.pingx.net/secpanel/%{name}-%{version}.tar.gz
URL:		http://www.pingx.net/secpanel/
Requires:	tcl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
SecPanel serves as a graphical user interface for managing and running
SSH (Secure Shell) and SCP (Secure Copy) connections. Note: SecPanel
is not a new implementation of the SecureShell protocol or the ssh
software-suite sh software-suite.

%description -l pl
SecPanel jest graficznym interfejsem pozwalaj�cym uruchamia� i
zarz�dza� sesjami SSH (Secure Shell) i SCP (Secure Copy). Uwaga:
SecPanel nie jest now� implementacj� protoko�u SecureShell.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/secpanel}

install src/bin/secpanel $RPM_BUILD_ROOT%{_bindir}
cp -r src/lib/secpanel/* $RPM_BUILD_ROOT%{_libdir}/secpanel


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/secpanel
%attr(755,root,root) %{_libdir}/secpanel/listserver.tcl
%attr(755,root,root) %{_libdir}/secpanel/secpanel*
%{_libdir}/secpanel/gui.tcl
%{_libdir}/secpanel/default*
%{_libdir}/secpanel/images
