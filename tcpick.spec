Summary:	Network analyzer
Summary(pl):	Analizator sieci
Name:		tcpick
Version:	0.2.1
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	bb94f2f9ea81aeb645619fbe9b3b9a29
URL:		http://tcpick.sourceforge.net/
BuildRequires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tcpick is a textmode sniffer libpcap-based that can track tcp streams
and saves the captured data in files or displays them in the terminal.

%description -l pl
tcpick jest sniferem opartym o bibliotekê libpcap. Wykrywa strumienie
tcp i zapisuje zdobyte dane do pliku lub wy¶wietla je w terminalu.

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
%doc AUTHORS ChangeLog EXAMPLES README doc/*.html
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man8/*
