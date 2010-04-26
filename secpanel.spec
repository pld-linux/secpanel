Summary:	Visual management of SSH connections
Summary(pl.UTF-8):	Wizualna nakładka na klienta SSH
Name:		secpanel
Version:	0.6.1
Release:	1
Epoch:		1
License:	GPL v2+
Group:		X11/Applications/Networking
Source0:	http://downloads.sourceforge.net/secpanel/%{name}-%{version}.tgz
# Source0-md5:	c94e598bc66d38421333b74a28abaa17
Source1:	%{name}.desktop
Patch0:		%{name}-data_location.patch
Patch1:		%{name}-title.patch
Patch2:		%{name}-distkeys_with_port.patch
URL:		http://themediahost.de/secpanel/
Requires:	tk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_datadir}/%{name}

%description
SecPanel serves as a graphical user interface for managing and running
SSH (Secure Shell) and SCP (Secure Copy) connections. Note: SecPanel
is not a new implementation of the SecureShell protocol or the ssh
software-suite.

%description -l pl.UTF-8
SecPanel jest graficznym interfejsem pozwalającym uruchamiać i
zarządzać sesjami SSH (Secure Shell) i SCP (Secure Copy). Uwaga:
SecPanel nie jest nową implementacją protokołu SecureShell.

%prep
%setup -c -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_appdir},%{_desktopdir}}

cd usr/local
install bin/secpanel $RPM_BUILD_ROOT%{_bindir}
cp -r lib/secpanel/* $RPM_BUILD_ROOT%{_appdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/secpanel
%dir %{_appdir}
%attr(755,root,root) %{_appdir}/convert_profile.tcl
%attr(755,root,root) %{_appdir}/dppw.tcl
%attr(755,root,root) %{_appdir}/gui.tcl
%attr(755,root,root) %{_appdir}/secpanel*
%{_appdir}/convert_history.tcl
%{_appdir}/default*
%{_appdir}/export_profiles.tcl
%{_appdir}/images
%{_appdir}/spdistkey
%{_appdir}/termdefs.txt
%{_desktopdir}/secpanel.desktop
