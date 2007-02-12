# TODO:
# - some icon for desktop
Summary:	Visual management of SSH connections
Summary(pl.UTF-8):	Wizualna nakładka na klienta SSH
Name:		secpanel
Version:	0.5.1
Release:	2
Epoch:		1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://www.pingx.net/secpanel/%{name}-%{version}.tar.gz
# Source0-md5:	c0694dbc5c1970e12eba552c2755482f
Source1:	%{name}.desktop
Patch0:		%{name}-data_location.patch
Patch1:		%{name}-title.patch
URL:		http://www.pingx.net/secpanel/
Requires:	tcl
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
%setup -q
%patch0 -p1
%patch1 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_appdir},%{_desktopdir}}

install src/bin/secpanel $RPM_BUILD_ROOT%{_bindir}
cp -r src/lib/secpanel/* $RPM_BUILD_ROOT%{_appdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
%attr(755,root,root) %{_bindir}/*
%dir %{_appdir}
%attr(755,root,root) %{_appdir}/convert_profile.tcl
%attr(755,root,root) %{_appdir}/listserver.tcl
%attr(755,root,root) %{_appdir}/gui.tcl
%attr(755,root,root) %{_appdir}/secpanel*
%{_appdir}/convert_history.tcl
%{_appdir}/default*
%{_appdir}/export_profiles.tcl
%{_appdir}/images
%{_appdir}/sp_scp.tcl
%{_desktopdir}/*.desktop
